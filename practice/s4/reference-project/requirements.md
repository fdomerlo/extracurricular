# Reference Project — Requirements S4

## Functional requirements

### Proceso en segundo plano

- Recordatorio de turno enviado de forma asíncrona, sin bloquear la reserva.
- Un fallo en el envío del recordatorio no debe romper ni cancelar el turno.

### Cache (condicional)

- Solo se introduce si hay una necesidad concreta y medible (ej. la consulta de disponibilidad de turnos es lenta con datos de prueba a escala). Si no hay necesidad, no se agrega cache este semestre.

### Refactorización

- Al menos una refactorización que toque una porción significativa del proyecto, respaldada por la suite de tests existente.
- Deuda técnica identificada y documentada en el backlog, aunque no toda se pague en este semestre.

## Invariants

Heredados de S1, S2 y S3, sin cambios en S4.

## Non-goals

En S4 no se requiere (ya construido en S3, ver `practice/s3/reference-project/`):

- containerización del entorno;
- pipeline de integración continua.

Tampoco se requiere en S4:

- procedimientos formales de despliegue/rollback en producción (llega en S5);
- métricas de salud del sistema más allá de logs (S5);
- observabilidad completa (tracing, SLIs/SLOs) (S6).
