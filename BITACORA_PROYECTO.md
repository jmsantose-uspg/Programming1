# Bitacora del Proyecto

## 2026-04-25

- Se detecto que el proyecto anterior estaba orientado a otra idea.
- Se definio migrar el enfoque hacia un sistema de servicios comunitarios para vecinos.
- Se reviso el documento de diseno para alinear entidades, endpoints y tecnologias.

## 2026-04-26

- Se creo una nueva version de `Servicios_Comunitarios.py` desde cero.
- Se agrego panel web dentro del mismo archivo usando `render_template_string`.
- Se implemento almacenamiento en `reportes.json` y `notificaciones.json`.
- Se construyeron endpoints para listar, crear, actualizar y eliminar reportes.
- Se agrego la logica para convertir reportes de `Ruta de camion` en notificaciones activas.
- Se genero un documento Word con explicacion del proyecto y del codigo.

## 2026-04-27

- Se ajusto Flask para escuchar en `0.0.0.0` y permitir acceso desde otros dispositivos en la misma red.
- Se confirmo acceso remoto usando la IP local de la laptop.
- Se identifico la necesidad de dejar memoria e historial del proyecto dentro de archivos Markdown.

## Acuerdos tecnicos importantes

- El backend se mantiene en un solo archivo para simplificar la entrega.
- El almacenamiento se hace en JSON porque asi lo pidio el curso.
- El panel web es basico pero funcional para pruebas reales.
- No se implemento autenticacion en esta version.

