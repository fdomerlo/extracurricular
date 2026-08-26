# Reference Project — Requirements S5

## Functional requirements

### Despliegue y rollback

- Procedimiento de despliegue documentado, ejecutado al menos una vez.
- Procedimiento de rollback documentado, ejecutado al menos una vez, incluyendo el caso de revertir una migración de base de datos.

### Métricas e incidentes

- Tablero o registro mínimo de estado del sistema, accesible sin entrar al servidor.
- Al menos un incidente (real o simulado deliberadamente) diagnosticado con logs y métricas, documentado con causa raíz.

### Performance

- Al menos una consulta lenta identificada con datos de prueba a escala y resuelta (índice, reescritura, o justificación de por qué no hace falta).

## Invariants

Heredados de S1–S4, sin cambios en S5.

## Non-goals

En S5 no se requiere:

- observabilidad completa con tracing y SLIs/SLOs formales (llega en S6);
- contribuciones a proyectos externos (S6).
