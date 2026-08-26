# Reference Project — S2

## Propósito

Proyecto de referencia para autodidactas que no tienen un proyecto propio. Continúa el motor de dominio construido en `practice/s1/reference-project/`.

## Dominio

Sistema de gestión de turnos para un **consultorio odontológico ficticio**. Ningún dato de este proyecto corresponde a un consultorio, profesional o paciente real: toda la información de prueba es inventada.

En S2 el dominio de S1 se vuelve **persistente** y queda accesible mediante una primera interfaz de administración con acceso controlado por rol.

## Entidades

- Patient
- Professional
- Appointment

Sin cambios respecto a S1: en S2 no se agregan entidades nuevas, se les da persistencia real.

## Novedades de este semestre

- Esquema relacional para Patient / Professional / Appointment, con SQL escrito a mano antes de introducir cualquier capa de abstracción.
- Persistencia real (PostgreSQL + ORM), con migraciones versionadas.
- Interfaz de administración con alta, edición y consulta de turnos.
- Autenticación básica y dos roles: **profesional** (ve y gestiona su propia agenda) y **secretaria** (gestiona la agenda de todos los profesionales).
- Un test de concurrencia: dos reservas simultáneas sobre el mismo turno no pueden coexistir.

## Datos de prueba

Todo el desarrollo usa datos ficticios (pacientes, profesionales y turnos inventados). Nunca se cargan datos reales de personas en este proyecto — ver la nota sobre datos sensibles en `requirements.md`.

## Evolución

```text
S1 → dominio
S2 → PostgreSQL           ← estás acá
S3 → web
S4 → arquitectura y asincronía
S5 → producción
S6 → observabilidad
```
