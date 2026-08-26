# Reference Project — S4

## Propósito

Proyecto de referencia para autodidactas que no tienen un proyecto propio. Continúa el sistema desplegado en `practice/s3/reference-project/`.

## Dominio

Sistema de gestión de turnos para un **consultorio odontológico ficticio**. Ningún dato de este proyecto corresponde a un consultorio, profesional o paciente real: toda la información de prueba es inventada.

En S4 el sistema pasa a poder **cambiarse sin miedo**: sostiene un proceso en segundo plano real, tolera fallos parciales y se somete a una refactorización grande hecha con red de tests.

> **Nota.** El entorno containerizado (Docker) y el pipeline de integración continua ya se construyeron en `practice/s3/reference-project/` (`S3-09`–`S3-12`), no en S4: es el orden real de este repositorio, distinto del de `custom-plan.md` (donde Docker/CI aparecen recién en su S4). S4 los da por construidos y se apoya en ellos.

## Entidades

- Patient
- Professional
- Appointment

Sin cambios respecto a S1/S2/S3.

## Novedades de este semestre

- Un proceso en segundo plano real: recordatorio de turno (email o notificación simulada) que no debe bloquear la reserva.
- Manejo de fallos parciales: un fallo en el envío de un recordatorio no debe romper ni cancelar el turno.
- Cache solo si aparece una necesidad concreta (ver criterio de incorporación tecnológica en `curriculum/study-plan.md` §2) — por ejemplo, si la consulta de disponibilidad de turnos se vuelve lenta con datos de prueba a escala.
- Logging estructurado sobre la aplicación y el proceso en segundo plano, sin datos de pacientes en los logs (aunque los datos sean ficticios, la práctica de no loguearlos es la que importa).
- Una refactorización grande, hecha con la red de tests como respaldo.

## Datos de prueba

Todo el desarrollo sigue usando datos ficticios. El proceso en segundo plano de recordatorios se prueba contra un servicio de email de desarrollo (nunca contra direcciones reales) o queda simulado con logs.

## Evolución

```text
S1 → dominio
S2 → PostgreSQL
S3 → web
S4 → resiliencia y refactor ← estás acá
S5 → producción
S6 → observabilidad
```
