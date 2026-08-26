# Reference Project — S1

## Propósito

Proyecto de referencia para autodidactas que no tienen un proyecto propio.

## Dominio

Sistema de gestión de turnos.

En S1 se construye únicamente un **motor de dominio ejecutable desde CLI**.

## Entidades

- Patient
- Professional
- Appointment

## Reglas

- un turno pertenece a un profesional;
- un turno pertenece a un paciente;
- un turno tiene fecha/hora;
- un turno posee un estado;
- no se puede confirmar un turno cancelado;
- no se puede cancelar un turno ya atendido.

La persistencia aparece en S2.

## Evolución

```text
S1 → dominio
S2 → PostgreSQL
S3 → web
S4 → arquitectura y asincronía
S5 → producción
S6 → observabilidad
```
