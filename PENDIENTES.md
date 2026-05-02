# Pendientes y Mejoras Futuras

## Pendientes cercanos

- Verificar por que en algunos dispositivos el guardado puede fallar y revisar la consola del servidor cuando ocurra.
- Hacer pruebas completas en mas de un navegador y mas de un telefono.
- Confirmar que la escritura en `reportes.json` y `notificaciones.json` se mantiene estable en todas las pruebas.

## Mejoras futuras

- Agregar autenticacion de usuarios.
- Separar HTML, CSS y JavaScript en archivos independientes.
- Agregar busqueda o filtros por tipo de reporte.
- Agregar fechas mas detalladas o historial por vecino.
- Implementar notificaciones automaticas por correo o WhatsApp.
- Migrar de JSON a SQLite o MySQL si el proyecto crece.

## Riesgos conocidos

- JSON no maneja bien concurrencia alta.
- El modo `debug=True` no es recomendable en produccion.
- El acceso por red local depende del firewall y de la IP actual del equipo.

