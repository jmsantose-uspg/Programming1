# App de Inspeccion para Ingreso a Facturacion

Aplicacion web para capturar inspecciones de camiones desde una tablet y almacenar los datos en la computadora de la oficina de facturacion.

## Como funciona

- La computadora de facturacion ejecuta el servidor Flask.
- La tablet abre la IP local de esa computadora en el navegador.
- Cada inspeccion se guarda en una base SQLite local.
- El personal de oficina puede revisar el historial y exportarlo a CSV.

## Tecnologias

- Python
- Flask
- SQLite
- HTML, CSS y JavaScript del navegador

## Estructura

- `app.py`: servidor principal
- `templates/index.html`: interfaz principal
- `static/style.css`: estilos
- `data/inspecciones.db`: base de datos local

## Instalacion

1. Crear y activar un entorno virtual.
2. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

3. Ejecutar la app:

```powershell
python app.py
```

## Uso en red local

Como el servidor arranca con `host="0.0.0.0"`, la app puede abrirse desde otro dispositivo en la misma red Wi-Fi usando:

```text
http://IP_LOCAL_DE_LA_PC:5000/
```

Ejemplo:

```text
http://192.168.1.20:5000/
```

## Supuestos actuales

Esta primera version incluye un checklist base de inspeccion. Si necesitas que los campos coincidan exactamente con tu proceso real, solo hay que ajustar la lista `CHECKLIST_FIELDS` y los campos del formulario.
