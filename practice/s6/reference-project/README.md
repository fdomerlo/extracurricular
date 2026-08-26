# Reference Project — S6

## Propósito

Proyecto de referencia para autodidactas que no tienen un proyecto propio. Continúa el sistema en producción de `practice/s5/reference-project/`.

## Dominio

Sistema de gestión de turnos para un **consultorio odontológico ficticio**. Ningún dato de este proyecto corresponde a un consultorio, profesional o paciente real: toda la información de prueba es inventada.

En S6 el proyecto pasa a **segundo plano**: se mantiene, no crece. El foco pasa a la observabilidad del sistema, la lectura y contribución a código ajeno, la documentación como portfolio y la defensa técnica del proyecto completo.

## Entidades

- Patient
- Professional
- Appointment

Sin cambios respecto a S1–S5.

## Novedades de este semestre

- Observabilidad mínima consolidada: logs estructurados, métricas y, si aparece la necesidad, algo de tracing sobre lo ya instrumentado en S4/S5.
- Lectura de código ajeno: elegir una dependencia de código abierto que ya usa el proyecto (el framework web, el ORM, o cualquier librería del stack) y entenderla en profundidad.
- Al menos una contribución externa real (documentación o un bug chico) a un proyecto de código abierto — no necesariamente relacionado con el consultorio ficticio.
- Documentación técnica del proyecto completo como portfolio: problema → decisiones → errores → refactors → tests → despliegues → incidentes.
- Defensa técnica del proyecto completo, explicable en cinco minutos a alguien técnico y en dos a alguien que no lo es.

Este Reference Project no incluye la parte de `custom-plan.md` sobre haber cobrado por escribir código: eso depende de la salida profesional de cada persona, no es parte del proyecto de referencia en sí.

## Datos de prueba

Sin cambios: el sistema sigue operando exclusivamente con datos ficticios.

## Evolución

```text
S1 → dominio
S2 → PostgreSQL
S3 → web
S4 → resiliencia y refactor
S5 → producción
S6 → observabilidad         ← estás acá
```
