# App de Inspeccion para Ingreso a Facturacion

Aplicacion web para capturar inspecciones de camiones desde una tablet y almacenar los datos en la computadora de la oficina de facturacion.

## Como funciona

- La computadora de facturacion ejecuta la app web con Python.
- La tablet abre la IP local de esa computadora en el navegador.
- Cada inspeccion se guarda en MariaDB.
- El personal de oficina puede revisar el historial y exportarlo a Excel.

## Tecnologias

- Python
- Flask
- MariaDB
- PyMySQL
- Waitress
- openpyxl
- HTML, CSS y JavaScript del navegador

## Estructura

- `app.py`: servidor principal
- `templates/index.html`: interfaz principal
- `static/style.css`: estilos
- `serve_app.py`: arranque con Waitress
- `iniciar_app.ps1`: script de inicio en Windows

## Instalacion

1. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

2. Configurar las variables de entorno para MariaDB:

```powershell
$env:IMPALA_DB_HOST = "localhost"
$env:IMPALA_DB_USER = "impala_app"
$env:IMPALA_DB_PASSWORD = "TU_PASSWORD"
$env:IMPALA_DB_NAME = "inspeccion_camiones"
$env:IMPALA_DB_PORT = "3306"
```

3. Ejecutar la app:

```powershell
python serve_app.py
```

Si `python` no funciona en Windows, usa el script incluido:

```powershell
powershell -ExecutionPolicy Bypass -File .\iniciar_app.ps1
```

## Uso en red local

Como el servidor arranca en la red local, la app puede abrirse desde otro dispositivo en la misma red Wi-Fi usando:

```text
http://IP_LOCAL_DE_LA_PC:5000/
```

Ejemplo:

```text
http://192.168.1.20:5000/
```

## Notas
- El repo no incluye la base de datos ni credenciales sensibles.
- Antes de usar la app en otra computadora, debes crear la base `inspeccion_camiones` y el usuario correspondiente en MariaDB.
- El checklist y los formularios pueden ajustarse desde `app.py` y `templates/index.html`.
