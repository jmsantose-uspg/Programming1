from __future__ import annotations

from datetime import datetime
import csv
import io
import json
from pathlib import Path
import sqlite3

from flask import Flask, flash, g, jsonify, redirect, render_template, request, send_file, url_for

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "inspecciones.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "cambia-esta-clave-en-produccion"

CHECKLIST_FIELDS = [
    {"name": "documentacion", "label": "Documentacion completa"},
    {"name": "estado_general", "label": "Estado general de la unidad"},
    {"name": "llantas", "label": "Revision de llantas"},
    {"name": "luces", "label": "Revision de luces"},
    {"name": "fugas", "label": "Sin fugas o derrames"},
    {"name": "limpieza", "label": "Limpieza de la unidad"},
    {"name": "sellos", "label": "Sellos o cierres de seguridad"},
    {"name": "equipo_seguridad", "label": "Equipo de seguridad requerido"},
]

STATUS_LABELS = {
    "ok": "Cumple",
    "warning": "Con observacion",
    "fail": "No cumple",
}

RESULT_OPTIONS = ["Aprobado", "Condicional", "Rechazado"]


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_error: Exception | None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db() -> None:
    db = get_db()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS inspecciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            numero_unidad TEXT NOT NULL,
            placa TEXT NOT NULL,
            piloto TEXT NOT NULL,
            empresa TEXT NOT NULL,
            producto TEXT NOT NULL,
            documento_referencia TEXT,
            origen TEXT,
            destino TEXT,
            inspector TEXT NOT NULL,
            resultado_final TEXT NOT NULL,
            checklist_json TEXT NOT NULL,
            observaciones_generales TEXT
        )
        """
    )
    db.commit()


def parse_checklist(form_data: dict[str, str]) -> tuple[list[dict[str, str]], list[str]]:
    checklist: list[dict[str, str]] = []
    errors: list[str] = []

    for field in CHECKLIST_FIELDS:
        status = form_data.get(field["name"], "").strip()
        note = form_data.get(f"{field['name']}_nota", "").strip()
        if status not in STATUS_LABELS:
            errors.append(f"Debes indicar el estado de: {field['label']}.")
            continue
        checklist.append(
            {
                "name": field["name"],
                "label": field["label"],
                "status": status,
                "status_label": STATUS_LABELS[status],
                "note": note,
            }
        )

    return checklist, errors


def validate_form(form_data: dict[str, str]) -> tuple[dict[str, str], list[dict[str, str]], list[str]]:
    payload = {
        "numero_unidad": form_data.get("numero_unidad", "").strip(),
        "placa": form_data.get("placa", "").strip(),
        "piloto": form_data.get("piloto", "").strip(),
        "empresa": form_data.get("empresa", "").strip(),
        "producto": form_data.get("producto", "").strip(),
        "documento_referencia": form_data.get("documento_referencia", "").strip(),
        "origen": form_data.get("origen", "").strip(),
        "destino": form_data.get("destino", "").strip(),
        "inspector": form_data.get("inspector", "").strip(),
        "resultado_final": form_data.get("resultado_final", "").strip(),
        "observaciones_generales": form_data.get("observaciones_generales", "").strip(),
    }

    required_fields = {
        "numero_unidad": "Numero de unidad",
        "placa": "Placa",
        "piloto": "Nombre del piloto",
        "empresa": "Empresa transportista",
        "producto": "Producto o carga",
        "inspector": "Nombre del inspector",
        "resultado_final": "Resultado final",
    }

    errors = [
        f"El campo '{label}' es obligatorio."
        for key, label in required_fields.items()
        if not payload[key]
    ]

    if payload["resultado_final"] and payload["resultado_final"] not in RESULT_OPTIONS:
        errors.append("El resultado final no es valido.")

    checklist, checklist_errors = parse_checklist(form_data)
    errors.extend(checklist_errors)

    return payload, checklist, errors


def create_inspection(payload: dict[str, str], checklist: list[dict[str, str]]) -> int:
    db = get_db()
    cursor = db.execute(
        """
        INSERT INTO inspecciones (
            created_at,
            numero_unidad,
            placa,
            piloto,
            empresa,
            producto,
            documento_referencia,
            origen,
            destino,
            inspector,
            resultado_final,
            checklist_json,
            observaciones_generales
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            payload["numero_unidad"],
            payload["placa"],
            payload["piloto"],
            payload["empresa"],
            payload["producto"],
            payload["documento_referencia"],
            payload["origen"],
            payload["destino"],
            payload["inspector"],
            payload["resultado_final"],
            json.dumps(checklist, ensure_ascii=False),
            payload["observaciones_generales"],
        ),
    )
    db.commit()
    return int(cursor.lastrowid)


def fetch_recent_inspections(limit: int = 20) -> list[dict]:
    rows = get_db().execute(
        """
        SELECT *
        FROM inspecciones
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()

    inspections: list[dict] = []
    for row in rows:
        item = dict(row)
        item["checklist"] = json.loads(item["checklist_json"])
        inspections.append(item)
    return inspections


def fetch_dashboard_stats() -> dict[str, int]:
    today = datetime.now().strftime("%Y-%m-%d")
    db = get_db()
    total_today = db.execute(
        "SELECT COUNT(*) FROM inspecciones WHERE substr(created_at, 1, 10) = ?",
        (today,),
    ).fetchone()[0]
    approved = db.execute(
        "SELECT COUNT(*) FROM inspecciones WHERE substr(created_at, 1, 10) = ? AND resultado_final = 'Aprobado'",
        (today,),
    ).fetchone()[0]
    conditional = db.execute(
        "SELECT COUNT(*) FROM inspecciones WHERE substr(created_at, 1, 10) = ? AND resultado_final = 'Condicional'",
        (today,),
    ).fetchone()[0]
    rejected = db.execute(
        "SELECT COUNT(*) FROM inspecciones WHERE substr(created_at, 1, 10) = ? AND resultado_final = 'Rechazado'",
        (today,),
    ).fetchone()[0]
    return {
        "total_today": total_today,
        "approved": approved,
        "conditional": conditional,
        "rejected": rejected,
    }


@app.before_request
def ensure_database() -> None:
    init_db()


@app.get("/")
def home():
    return render_template(
        "index.html",
        checklist_fields=CHECKLIST_FIELDS,
        result_options=RESULT_OPTIONS,
        inspections=fetch_recent_inspections(),
        stats=fetch_dashboard_stats(),
        status_labels=STATUS_LABELS,
        now=datetime.now().strftime("%d/%m/%Y"),
        form_data={},
    )


@app.post("/inspecciones")
def save_inspection():
    form_data = request.form.to_dict()
    payload, checklist, errors = validate_form(form_data)

    if errors:
        for error in errors:
            flash(error, "error")
        return render_template(
            "index.html",
            checklist_fields=CHECKLIST_FIELDS,
            result_options=RESULT_OPTIONS,
            inspections=fetch_recent_inspections(),
            stats=fetch_dashboard_stats(),
            status_labels=STATUS_LABELS,
            now=datetime.now().strftime("%d/%m/%Y"),
            form_data=form_data,
        ), 400

    new_id = create_inspection(payload, checklist)
    flash(f"Inspeccion #{new_id} guardada correctamente.", "success")
    return redirect(url_for("home"))


@app.get("/api/inspecciones")
def list_inspections_api():
    return jsonify(fetch_recent_inspections(limit=100))


@app.get("/api/inspecciones/<int:inspection_id>")
def inspection_detail_api(inspection_id: int):
    row = get_db().execute(
        "SELECT * FROM inspecciones WHERE id = ?",
        (inspection_id,),
    ).fetchone()
    if row is None:
        return jsonify({"error": "Inspeccion no encontrada."}), 404

    item = dict(row)
    item["checklist"] = json.loads(item["checklist_json"])
    return jsonify(item)


@app.get("/export/csv")
def export_csv():
    inspections = fetch_recent_inspections(limit=1000)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(
        [
            "ID",
            "Fecha",
            "Unidad",
            "Placa",
            "Piloto",
            "Empresa",
            "Producto",
            "Documento",
            "Origen",
            "Destino",
            "Inspector",
            "Resultado",
            "Observaciones",
            "Checklist",
        ]
    )

    for item in inspections:
        checklist_summary = " | ".join(
            f"{check['label']}: {check['status_label']}" + (f" ({check['note']})" if check["note"] else "")
            for check in item["checklist"]
        )
        writer.writerow(
            [
                item["id"],
                item["created_at"],
                item["numero_unidad"],
                item["placa"],
                item["piloto"],
                item["empresa"],
                item["producto"],
                item["documento_referencia"],
                item["origen"],
                item["destino"],
                item["inspector"],
                item["resultado_final"],
                item["observaciones_generales"],
                checklist_summary,
            ]
        )

    bytes_io = io.BytesIO(output.getvalue().encode("utf-8-sig"))
    bytes_io.seek(0)
    filename = f"inspecciones_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    return send_file(bytes_io, as_attachment=True, download_name=filename, mimetype="text/csv")


if __name__ == "__main__":
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with app.app_context():
        init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
