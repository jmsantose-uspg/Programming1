# Decisiones Tecnicas del Proyecto

## 1. Uso de Flask

Se eligio Flask porque:

- Es mas facil de aprender para el nivel del proyecto.
- Permite construir rutas REST rapidamente.
- Se integra bien con formularios y respuestas JSON.

## 2. Uso de archivos JSON

Se eligio JSON porque:

- Fue un requerimiento del catedratico.
- Simplifica el entorno de desarrollo.
- Evita instalar una base de datos formal.

Limitacion:

- No es ideal para muchos usuarios escribiendo al mismo tiempo.

## 3. Panel web dentro del mismo archivo Python

Se decidio mantener HTML, CSS y JavaScript dentro de `Servicios_Comunitarios.py` porque:

- Reduce la complejidad inicial.
- Facilita mover y ejecutar el proyecto.
- Es suficiente para una entrega academica.

Limitacion:

- En proyectos grandes conviene separar plantillas y archivos estaticos.

## 4. Logica especial para notificaciones

Se decidio que un reporte de `Ruta de camion` genere una notificacion porque:

- Es la categoria que requiere mayor visibilidad.
- Permite diferenciar avisos urgentes de reportes normales.

## 5. Acceso desde la red local

Se habilito `host="0.0.0.0"` para:

- Permitir pruebas reales desde celulares u otras computadoras.
- Mostrar que el sistema puede usarse en una comunidad dentro de la misma red.

## 6. Sin autenticacion

Se dejo fuera la autenticacion porque:

- No era parte del alcance principal.
- Habria agregado tiempo y complejidad innecesaria para esta version.

