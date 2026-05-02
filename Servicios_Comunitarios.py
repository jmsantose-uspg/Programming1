from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import unicodedata

from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
REPORTES_FILE = BASE_DIR / "reportes.json"
NOTIFICACIONES_FILE = BASE_DIR / "notificaciones.json"
TIPOS_VALIDOS = [
    "Seguridad",
    "Mantenimiento",
    "Mascotas",
    "Quejas",
    "Ruta de camion",
]

PANEL_TEMPLATE = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Servicios Comunitarios</title>
    <style>
        :root {
            --fondo: #f4efe6;
            --panel: #fffdf8;
            --principal: #205072;
            --secundario: #329d9c;
            --acento: #f18f01;
            --texto: #1b1b1b;
            --borde: #d9d1c7;
            --alerta: #fff4d6;
        }

        * { box-sizing: border-box; }

        body {
            margin: 0;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background:
                radial-gradient(circle at top right, rgba(241, 143, 1, 0.16), transparent 22rem),
                linear-gradient(180deg, #f7f3ec 0%, var(--fondo) 100%);
            color: var(--texto);
        }

        .contenedor {
            width: min(1100px, calc(100% - 2rem));
            margin: 0 auto;
            padding: 2rem 0 3rem;
        }

        .hero {
            background: linear-gradient(135deg, var(--principal), var(--secundario));
            color: white;
            border-radius: 24px;
            padding: 2rem;
            box-shadow: 0 18px 40px rgba(32, 80, 114, 0.2);
        }

        .hero h1 {
            margin: 0 0 0.5rem;
            font-size: clamp(2rem, 4vw, 3rem);
        }

        .hero p {
            margin: 0;
            max-width: 45rem;
            line-height: 1.5;
        }

        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-top: 1.5rem;
        }

        .tarjeta {
            background: var(--panel);
            border: 1px solid rgba(217, 209, 199, 0.9);
            border-radius: 20px;
            padding: 1.35rem;
            box-shadow: 0 14px 30px rgba(41, 44, 61, 0.08);
        }

        .tarjeta h2 {
            margin: 0 0 1rem;
            color: var(--principal);
        }

        form {
            display: grid;
            gap: 0.9rem;
        }

        label {
            display: grid;
            gap: 0.35rem;
            font-weight: 600;
        }

        input, select, textarea, button {
            font: inherit;
        }

        input, select, textarea {
            width: 100%;
            border: 1px solid var(--borde);
            border-radius: 12px;
            padding: 0.8rem 0.9rem;
            background: white;
        }

        textarea {
            min-height: 110px;
            resize: vertical;
        }

        .acciones {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
        }

        button {
            border: 0;
            border-radius: 999px;
            padding: 0.85rem 1.15rem;
            cursor: pointer;
            font-weight: 700;
            transition: transform 0.15s ease, opacity 0.15s ease;
        }

        button:hover { transform: translateY(-1px); }

        .btn-principal {
            background: var(--principal);
            color: white;
        }

        .btn-secundario {
            background: #e7edf2;
            color: var(--principal);
        }

        .btn-alerta {
            background: #fff0da;
            color: #b35a00;
        }

        .estado {
            min-height: 1.4rem;
            font-weight: 600;
        }

        .panel-alertas {
            margin-top: 1.5rem;
        }

        .lista {
            display: grid;
            gap: 0.9rem;
        }

        .item {
            border: 1px solid var(--borde);
            border-radius: 16px;
            padding: 1rem;
            background: #fff;
        }

        .item-alerta {
            background: var(--alerta);
            border-color: #f3d382;
        }

        .item header {
            display: flex;
            gap: 0.75rem;
            justify-content: space-between;
            align-items: baseline;
            flex-wrap: wrap;
        }

        .item h3 {
            margin: 0;
            font-size: 1rem;
            color: var(--principal);
        }

        .item p {
            margin: 0.5rem 0 0;
            line-height: 1.45;
        }

        .meta {
            color: #575757;
            font-size: 0.95rem;
        }

        .item .acciones {
            margin-top: 0.9rem;
        }

        .vacio {
            margin: 0;
            color: #666;
        }

        @media (max-width: 860px) {
            .grid {
                grid-template-columns: 1fr;
            }

            .contenedor {
                width: min(100% - 1rem, 1100px);
            }

            .hero, .tarjeta {
                border-radius: 18px;
            }
        }
    </style>
</head>
<body>
    <div class="contenedor">
        <section class="hero">
            <h1>Servicios Comunitarios</h1>
            <p>Panel web para registrar reportes vecinales y mostrar notificaciones importantes para la comunidad.</p>
        </section>

        <section class="grid">
            <article class="tarjeta">
                <h2>Nuevo reporte</h2>
                <form id="form-reporte">
                    <input type="hidden" id="reporte-id">

                    <label for="vecino">
                        Nombre o numero de casa
                        <input id="vecino" name="vecino" placeholder="Ejemplo: Casa 12 o Jose Santos" required>
                    </label>

                    <label for="tipo">
                        Tipo de reporte
                        <select id="tipo" name="tipo" required>
                            <option value="">Seleccione una opcion</option>
                            {% for tipo in tipos_validos %}
                            <option value="{{ tipo }}">{{ tipo }}</option>
                            {% endfor %}
                        </select>
                    </label>

                    <label for="descripcion">
                        Descripcion
                        <textarea id="descripcion" name="descripcion" placeholder="Describe el reporte o la notificacion" required></textarea>
                    </label>

                    <div class="acciones">
                        <button class="btn-principal" type="submit" id="boton-guardar">Guardar reporte</button>
                        <button class="btn-secundario" type="button" id="boton-cancelar" hidden>Cancelar edicion</button>
                    </div>
                    <div class="estado" id="estado"></div>
                </form>
            </article>

            <article class="tarjeta panel-alertas">
                <h2>Notificaciones activas</h2>
                <div class="lista" id="lista-notificaciones"></div>
            </article>
        </section>

        <section class="tarjeta" style="margin-top: 1.5rem;">
            <h2>Reportes registrados</h2>
            <div class="lista" id="lista-reportes"></div>
        </section>
    </div>

    <script>
        const form = document.getElementById("form-reporte");
        const estado = document.getElementById("estado");
        const listaReportes = document.getElementById("lista-reportes");
        const listaNotificaciones = document.getElementById("lista-notificaciones");
        const botonGuardar = document.getElementById("boton-guardar");
        const botonCancelar = document.getElementById("boton-cancelar");
        const campoId = document.getElementById("reporte-id");
        const campoVecino = document.getElementById("vecino");
        const campoTipo = document.getElementById("tipo");
        const campoDescripcion = document.getElementById("descripcion");

        function mostrarEstado(mensaje, error = false) {
            estado.textContent = mensaje;
            estado.style.color = error ? "#b00020" : "#205072";
        }

        function limpiarFormulario() {
            campoId.value = "";
            form.reset();
            botonGuardar.textContent = "Guardar reporte";
            botonCancelar.hidden = true;
            mostrarEstado("");
        }

        function escapeHtml(valor) {
            return String(valor)
                .replaceAll("&", "&amp;")
                .replaceAll("<", "&lt;")
                .replaceAll(">", "&gt;")
                .replaceAll('"', "&quot;")
                .replaceAll("'", "&#39;");
        }

        function renderNotificaciones(items) {
            if (!items.length) {
                listaNotificaciones.innerHTML = '<p class="vacio">No hay notificaciones activas.</p>';
                return;
            }

            listaNotificaciones.innerHTML = items.map((item) => `
                <article class="item item-alerta">
                    <header>
                        <h3>${escapeHtml(item.vecino)}</h3>
                        <span class="meta">${escapeHtml(item.fecha)}</span>
                    </header>
                    <p>${escapeHtml(item.mensaje)}</p>
                </article>
            `).join("");
        }

        function cargarEnFormulario(item) {
            campoId.value = item.id;
            campoVecino.value = item.vecino;
            campoTipo.value = item.tipo;
            campoDescripcion.value = item.descripcion;
            botonGuardar.textContent = "Actualizar reporte";
            botonCancelar.hidden = false;
            mostrarEstado("Editando reporte #" + item.id);
            window.scrollTo({ top: 0, behavior: "smooth" });
        }

        async function eliminarReporte(id) {
            const confirmado = window.confirm("Deseas eliminar este reporte?");
            if (!confirmado) return;

            const respuesta = await fetch(`/api/reportes/${id}`, { method: "DELETE" });
            const data = await respuesta.json();

            if (!respuesta.ok) {
                mostrarEstado(data.error || "No se pudo eliminar el reporte.", true);
                return;
            }

            mostrarEstado(data.mensaje);
            if (Number(campoId.value) === id) {
                limpiarFormulario();
            }
            await cargarDatos();
        }

        function renderReportes(items) {
            if (!items.length) {
                listaReportes.innerHTML = '<p class="vacio">Todavia no hay reportes registrados.</p>';
                return;
            }

            listaReportes.innerHTML = items.map((item) => `
                <article class="item">
                    <header>
                        <h3>${escapeHtml(item.tipo)} - ${escapeHtml(item.vecino)}</h3>
                        <span class="meta">${escapeHtml(item.fecha)}</span>
                    </header>
                    <p>${escapeHtml(item.descripcion)}</p>
                    <div class="acciones">
                        <button class="btn-secundario" type="button" data-editar="${item.id}">Editar</button>
                        <button class="btn-alerta" type="button" data-eliminar="${item.id}">Eliminar</button>
                    </div>
                </article>
            `).join("");

            listaReportes.querySelectorAll("[data-editar]").forEach((boton) => {
                boton.addEventListener("click", () => {
                    const item = items.find((reporte) => reporte.id === Number(boton.dataset.editar));
                    if (item) cargarEnFormulario(item);
                });
            });

            listaReportes.querySelectorAll("[data-eliminar]").forEach((boton) => {
                boton.addEventListener("click", () => {
                    eliminarReporte(Number(boton.dataset.eliminar));
                });
            });
        }

        async function cargarDatos() {
            const [respuestaReportes, respuestaNotificaciones] = await Promise.all([
                fetch("/api/reportes"),
                fetch("/api/notificaciones")
            ]);

            const reportes = await respuestaReportes.json();
            const notificaciones = await respuestaNotificaciones.json();

            renderReportes(reportes);
            renderNotificaciones(notificaciones);
        }

        form.addEventListener("submit", async (evento) => {
            evento.preventDefault();

            const payload = {
                vecino: campoVecino.value.trim(),
                tipo: campoTipo.value,
                descripcion: campoDescripcion.value.trim()
            };

            const id = campoId.value;
            const metodo = id ? "PUT" : "POST";
            const url = id ? `/api/reportes/${id}` : "/api/reportes";

            const respuesta = await fetch(url, {
                method: metodo,
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await respuesta.json();

            if (!respuesta.ok) {
                mostrarEstado(data.error || "No se pudo guardar el reporte.", true);
                return;
            }

            mostrarEstado(data.mensaje);
            limpiarFormulario();
            await cargarDatos();
        });

        botonCancelar.addEventListener("click", () => {
            limpiarFormulario();
        });

        cargarDatos().catch(() => {
            mostrarEstado("No se pudo cargar la informacion del sistema.", true);
        });
    </script>
</body>
</html>
"""


def normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    without_marks = "".join(char for char in normalized if not unicodedata.combining(char))
    return without_marks.strip().casefold()


def read_items(path: Path) -> list[dict]:
    if not path.exists():
        path.write_text("[]", encoding="utf-8")
        return []

    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        path.write_text("[]", encoding="utf-8")
        return []

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        path.write_text("[]", encoding="utf-8")
        return []

    return data if isinstance(data, list) else []


def write_items(path: Path, items: list[dict]) -> None:
    path.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")


def next_id(items: list[dict]) -> int:
    return max((int(item["id"]) for item in items), default=0) + 1


def is_notification_type(tipo: str) -> bool:
    return normalize_text(tipo) == "ruta de camion"


def validate_payload(payload: dict) -> tuple[dict | None, str | None]:
    vecino = str(payload.get("vecino", "")).strip()
    tipo = str(payload.get("tipo", "")).strip()
    descripcion = str(payload.get("descripcion", "")).strip()

    if not vecino or not tipo or not descripcion:
        return None, "Debes completar vecino, tipo y descripcion."

    if tipo not in TIPOS_VALIDOS:
        return None, "El tipo de reporte no es valido."

    data = {
        "vecino": vecino,
        "tipo": tipo,
        "descripcion": descripcion,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }
    return data, None


def sync_notification(reporte: dict, previous_notification_id: int | None = None) -> None:
    notificaciones = read_items(NOTIFICACIONES_FILE)

    notificaciones = [
        notificacion
        for notificacion in notificaciones
        if int(notificacion.get("reporte_id", -1)) != int(reporte["id"])
    ]

    if is_notification_type(reporte["tipo"]):
        notification_id = previous_notification_id or next_id(notificaciones)
        notificaciones.insert(0, {
            "id": notification_id,
            "reporte_id": reporte["id"],
            "fecha": reporte["fecha"],
            "vecino": reporte["vecino"],
            "mensaje": reporte["descripcion"],
        })

    write_items(NOTIFICACIONES_FILE, notificaciones)


def remove_notification_by_report(reporte_id: int) -> None:
    notificaciones = read_items(NOTIFICACIONES_FILE)
    filtered = [
        item for item in notificaciones if int(item.get("reporte_id", -1)) != reporte_id
    ]
    write_items(NOTIFICACIONES_FILE, filtered)


@app.get("/")
def panel() -> str:
    return render_template_string(PANEL_TEMPLATE, tipos_validos=TIPOS_VALIDOS)


@app.get("/api")
def api_info():
    return jsonify({
        "mensaje": "Bienvenido a la API de Servicios Comunitarios",
        "version": "1.0",
        "endpoints": [
            "/api/reportes",
            "/api/notificaciones",
        ],
    })


@app.get("/api/reportes")
def listar_reportes():
    return jsonify(read_items(REPORTES_FILE))


@app.post("/api/reportes")
def crear_reporte():
    payload = request.get_json(silent=True) or request.form.to_dict()
    reporte, error = validate_payload(payload)
    if error:
        return jsonify({"error": error}), 400

    reportes = read_items(REPORTES_FILE)
    reporte["id"] = next_id(reportes)
    reportes.insert(0, reporte)
    write_items(REPORTES_FILE, reportes)
    sync_notification(reporte)

    return jsonify({
        "mensaje": "Reporte guardado correctamente.",
        "data": reporte,
    }), 201


@app.put("/api/reportes/<int:reporte_id>")
def actualizar_reporte(reporte_id: int):
    payload = request.get_json(silent=True) or request.form.to_dict()
    nuevos_datos, error = validate_payload(payload)
    if error:
        return jsonify({"error": error}), 400

    reportes = read_items(REPORTES_FILE)
    notification_id = None

    for index, reporte in enumerate(reportes):
        if int(reporte["id"]) != reporte_id:
            continue

        for item in read_items(NOTIFICACIONES_FILE):
            if int(item.get("reporte_id", -1)) == reporte_id:
                notification_id = int(item["id"])
                break

        nuevos_datos["id"] = reporte_id
        reportes[index] = nuevos_datos
        write_items(REPORTES_FILE, reportes)
        sync_notification(nuevos_datos, notification_id)
        return jsonify({
            "mensaje": "Reporte actualizado correctamente.",
            "data": nuevos_datos,
        })

    return jsonify({"error": "No se encontro el reporte solicitado."}), 404


@app.delete("/api/reportes/<int:reporte_id>")
def eliminar_reporte(reporte_id: int):
    reportes = read_items(REPORTES_FILE)
    filtrados = [item for item in reportes if int(item["id"]) != reporte_id]

    if len(filtrados) == len(reportes):
        return jsonify({"error": "No se encontro el reporte solicitado."}), 404

    write_items(REPORTES_FILE, filtrados)
    remove_notification_by_report(reporte_id)
    return jsonify({"mensaje": "Reporte eliminado correctamente."})


@app.get("/api/notificaciones")
def listar_notificaciones():
    return jsonify(read_items(NOTIFICACIONES_FILE))


if __name__ == "__main__":
    read_items(REPORTES_FILE)
    read_items(NOTIFICACIONES_FILE)
    app.run(debug=True, host="0.0.0.0", port=5000)
