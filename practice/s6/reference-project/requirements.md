# Reference Project — Requirements S6

## Functional requirements

### Observabilidad

- Responder, con evidencia del propio sistema: ¿está caído? ¿está lento? ¿desde cuándo? ¿por qué?

### Código ajeno

- Documentar el entendimiento profundo de al menos una dependencia externa del proyecto.
- Al menos una contribución aceptada en un proyecto de código abierto ajeno.

### Documentación y defensa

- El repositorio permite reconstruir la evolución completa del consultorio ficticio: problema → decisiones → errores → refactors → tests → despliegues → incidentes.
- Defensa técnica del proyecto completo, explicable en cinco minutos a alguien técnico y en dos a alguien que no lo es.

## Invariants

Heredados de S1–S5, sin cambios en S6.

## Non-goals

En S6 no se requiere:

- crecimiento funcional del dominio (Patient / Professional / Appointment se mantienen, no se agregan features nuevas);
- evidencia de haber cobrado por escribir código — no aplica a un Reference Project genérico, es parte específica de `custom-plan.md`.
