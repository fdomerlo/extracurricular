# Reference Project — S3

## Propósito

Proyecto de referencia para autodidactas que no tienen un proyecto propio. Continúa el sistema persistente construido en `practice/s2/reference-project/`.

## Dominio

Sistema de gestión de turnos para un **consultorio odontológico ficticio**. Ningún dato de este proyecto corresponde a un consultorio, profesional o paciente real: toda la información de prueba es inventada.

En S3 el sistema pasa de tener solo una interfaz de administración a tener **vistas web propias**, usables por alguien fuera de tu máquina.

## Entidades

- Patient
- Professional
- Appointment

Sin cambios respecto a S1/S2.

## Novedades de este semestre

- Vistas web propias: reservar, confirmar y cancelar un turno sin pasar por la administración.
- Interactividad server-rendered (sin necesidad de una API separada ni de un frontend desacoplado) para acciones como confirmar o cancelar un turno sin recargar la página completa.
- Autenticación y permisos por rol en las vistas propias: **profesional**, **secretaria** y **paciente** (ficticio).
- Seguridad básica de aplicaciones web: inyección, XSS, CSRF, control de acceso roto.
- Despliegue: un servidor, proxy inverso, HTTPS, logs y backups automatizados.

## Datos de prueba

Todo el desarrollo y la demo usan datos ficticios (pacientes, profesionales y turnos inventados). Ningún usuario real del Reference Project debe existir en este sistema — ver la nota sobre datos sensibles en `requirements.md`.

## Evolución

```text
S1 → dominio
S2 → PostgreSQL
S3 → web                  ← estás acá
S4 → arquitectura y asincronía
S5 → producción
S6 → observabilidad
```
