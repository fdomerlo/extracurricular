# S2 — Schedule

11 clases distribuidas en las 22 semanas lectivas del semestre (`curriculum/study-plan.md` §6). El contenido ocupa las semanas 1–15 con semanas de consolidación estratégica.

| Semana | Actividad | Proyecto |
|---:|---|---|
| 1 | S2-01 — Modelo relacional aplicado: DDL y restricciones | Project Task |
| 2 | S2-02 — SQL a mano: Consultas, joins y agregaciones | Project Task |
| 3 | S2-03 — Índices y planes de ejecución: EXPLAIN ANALYZE | Project Task |
| 4 | S2-04 — Transacciones, ACID y concurrencia reproducible | Project Task |
| 5 | S2-05 — ORM consciente y migraciones desde el dominio | Project Task |
| 6 | S2-06 — Optimización de consultas: El problema N+1 | Project Task |
| 7 | **Consolidación** — Migrar modelos restantes y erradicar N+1 de la agenda | Proyecto |
| 8 | S2-07 — Interfaz de acceso operativo: Django Admin | Project Task |
| 9 | **Consolidación** — Backoffice usable para todas las entidades del dominio | Proyecto |
| 10 | S2-08 — Autenticación y permisos por rol (RBAC) | Project Task |
| 11 | S2-09 — Testing de integración contra PostgreSQL real | Project Task |
| 12 | S2-10 — Backup, restore y consistencia de datos | Project Task |
| 13 | **Consolidación** — Simulacro de recuperación ante desastres y suite verde | Proyecto |
| 14 | S2-11 — IA como copiloto técnico con verificación estricta | Project Task |
| 15 | Consolidación final de código y documentación de S2 | Proyecto |
| 16 | Recuperación / cierre de pendientes | Correcciones |
| 17 | Integración del sistema persistente completo | Proyecto |
| 18 | Integración y preparación de la defensa | Proyecto |
| 19 | **Milestone M-S2** | Entrega |
| 20 | **Defensa técnica / revisión** | Evaluación |
| 21 | Buffer / recuperación de gates pendientes | Correcciones |
| 22 | Cierre / retrospectiva y preparación para S3 | Roadmap siguiente |

## Por qué hay semanas de consolidación

Las semanas 7, 9 y 13 no son relleno; son pausas deliberadas para absorber saltos de complejidad técnica:

- **Semana 7:** `S2-05` y `S2-06` introducen el ORM y la erradicación del problema N+1. Llevar todos los modelos del consultorio al ORM y blindar la suite de query count requiere trabajo concentrado en el proyecto.
- **Semana 9:** Configurar un Django Admin que sea realmente usable para usuarios no técnicos requiere personalizar vistas de lista, filtros, búsquedas y acciones para múltiples entidades.
- **Semana 13:** Ejecutar un simulacro serio de Disaster Recovery (`pg_dump` → borrar base → `pg_restore` → verificar integridad) exige tiempo para armar scripts reproducibles sin la presión de una clase nueva.

## Tutorías

Aproximadamente cada dos semanas. No son clases magistrales: revisan el trabajo producido, las decisiones de persistencia tomadas en Pull Requests, bloqueos técnicos y el avance hacia el milestone `M-S2`.
