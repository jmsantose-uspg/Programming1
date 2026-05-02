# Servicios Comunitarios

Proyecto desarrollado en Python con Flask para registrar reportes vecinales y mostrar notificaciones importantes dentro de una comunidad.

## Objetivo

El sistema permite:

- Crear reportes comunitarios.
- Consultar reportes existentes.
- Editar reportes.
- Eliminar reportes.
- Mostrar notificaciones activas cuando el tipo de reporte es `Ruta de camion`.

## Tecnologias

- Python
- Flask
- HTML, CSS y JavaScript embebidos
- Archivos JSON como almacenamiento

## Archivos principales

- `Servicios_Comunitarios.py`: archivo principal del sistema.
- `reportes.json`: guarda los reportes registrados.
- `notificaciones.json`: guarda las notificaciones activas.

## Como ejecutar el proyecto

1. Activar el entorno virtual si se desea.
2. Ejecutar:

```powershell
c:/Escritorio/Mis_Programas/.venv/Scripts/python.exe c:/Escritorio/Mis_Programas/Servicios_Comunitarios.py
```

3. Abrir en navegador local:

```text
http://127.0.0.1:5000/
```

4. Abrir desde otro dispositivo en la misma red:

```text
http://IP_LOCAL_DE_LA_LAPTOP:5000/
```

## Endpoints principales

- `GET /` Panel web principal
- `GET /api` Informacion general de la API
- `GET /api/reportes` Listar reportes
- `POST /api/reportes` Crear reporte
- `PUT /api/reportes/<id>` Actualizar reporte
- `DELETE /api/reportes/<id>` Eliminar reporte
- `GET /api/notificaciones` Listar notificaciones activas

## Reglas importantes del sistema

- Los tipos validos son: `Seguridad`, `Mantenimiento`, `Mascotas`, `Quejas` y `Ruta de camion`.
- Si el tipo es `Ruta de camion`, el sistema tambien crea o actualiza una notificacion.
- Los campos obligatorios son `vecino`, `tipo` y `descripcion`.

## Estado actual

El proyecto ya cuenta con:

- Panel web funcional
- CRUD de reportes
- Notificaciones activas
- Almacenamiento en JSON
- Acceso local desde otros dispositivos en la misma red

