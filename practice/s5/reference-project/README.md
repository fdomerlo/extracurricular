# Reference Project — S5

## Propósito

Proyecto de referencia para autodidactas que no tienen un proyecto propio. Continúa el sistema construido en `practice/s4/reference-project/`.

## Dominio

Sistema de gestión de turnos para un **consultorio odontológico ficticio**. Ningún dato de este proyecto corresponde a un consultorio, profesional o paciente real: toda la información de prueba es inventada.

En S5 el sistema pasa a **operarse fuera del entorno de desarrollo**, con criterio de qué pasa cuando algo falla.

## Entidades

- Patient
- Professional
- Appointment

Sin cambios respecto a S1/S2/S3/S4.

## Novedades de este semestre

- Procedimiento de despliegue documentado y ejecutado.
- Procedimiento de rollback documentado y ejecutado, incluyendo rollback de una migración de base de datos.
- Métricas mínimas de salud del sistema: ¿está caído? ¿está lento? ¿desde cuándo?
- Diagnóstico de al menos un incidente simulado deliberadamente (ej. la base de datos se queda sin conexiones disponibles, o el proceso en segundo plano de S4 deja de consumir la cola de recordatorios), usando logs y métricas, no adivinando.
- Identificación y resolución de al menos una consulta lenta con datos de prueba a escala.

## Datos de prueba

El servidor de producción de este Reference Project, si se despliega, debe poblarse solo con datos ficticios generados para la demo — nunca con datos de personas reales.

## Evolución

```text
S1 → dominio
S2 → PostgreSQL
S3 → web
S4 → resiliencia y refactor
S5 → producción            ← estás acá
S6 → observabilidad
```
