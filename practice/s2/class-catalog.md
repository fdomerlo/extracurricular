# S2 — Class Catalog

Las 11 clases de S2, en orden cronológico y pedagógico. El frontmatter de cada archivo en `practice/s2/classes/` es la fuente de verdad; esta tabla lo resume.

| ID | Clase | Competencias | Nivel | Duración | Prerrequisitos |
|---|---|---|:---:|---|---|
| **S2-01** | Modelo relacional aplicado — Esquema DDL y restricciones | C18, C19, C21 | L2 | 1 sesión (~2 h) | S1-04, S1-05 |
| **S2-02** | SQL a mano — Consultas del dominio, joins y agregaciones | C19, C03 | L2 | 1 sesión (~2 h) | S2-01 |
| **S2-03** | Índices y planes de ejecución — EXPLAIN ANALYZE | C20, C57 | L2 | 1 sesión (~1.5 h) | S2-02 |
| **S2-04** | Transacciones, ACID y concurrencia reproducible | C22, C23 | L3 | 1.5 sesiones (~2 h) | S2-01, S1-05 |
| **S2-05** | ORM consciente y migraciones desde el dominio | C24, C25, C04 | L2 | 1 sesión (~2 h) | S2-01 a S2-04 |
| **S2-06** | Optimización de consultas con ORM — El problema N+1 | C20, C24 | L3 | 1 sesión (~1.5 h) | S2-05 |
| **S2-07** | Interfaz de acceso operativo — Django Admin como backoffice | C29, C40 | L2 | 1 sesión (~1.5 h) | S2-05 |
| **S2-08** | Autenticación y permisos por rol (RBAC) en backoffice | C34, C35, C33 | L2 | 1 sesión (~1.5 h) | S2-07 |
| **S2-09** | Testing de integración contra PostgreSQL real | C14, C13 | L3 | 1 sesión (~2 h) | S2-05, S1-06 |
| **S2-10** | Backup, restore y consistencia de datos | C26, C45 | L2 | 1 sesión (~1.5 h) | S2-01 a S2-05 |
| **S2-11** | IA como copiloto técnico con verificación estricta | C66, C67, C71 | L3 | 1 sesión (~1.5 h) | S1-11, S2-01 a S2-10 |

## Cobertura de competencias

Competencias desarrolladas en S2: **C03, C04, C13, C14, C18, C19, C20, C21, C22, C23, C24, C25, C26, C29, C33, C34, C35, C40, C45, C57, C66, C67, C71**.

### Competency Gates del Semestre (Evaluados formalmente en `M-S2`):
- **C14 — Tests de integración (L3):** Comprobado en `S2-09` mediante suite de pruebas contra PostgreSQL real.
- **C18 — Modelado relacional (L4):** Comprobado en `S2-01` y en la arquitectura relacional final.
- **C19 — SQL (L4):** Comprobado en `S2-01` y `S2-02` mediante DDL y consultas analíticas a mano.
- **C21 — PostgreSQL (L3):** Comprobado a lo largo de todo el semestre como motor de referencia.
- **C22 — Transacciones y ACID (L4):** Comprobado en `S2-04` mediante aislamiento y resolución de condiciones de carrera.
- **C24 — ORM consciente (L3):** Comprobado en `S2-05` y `S2-06` mediante mapeo disciplinado y control del problema N+1.
- **C25 — Migraciones (L3):** Comprobado en `S2-05` mediante transformaciones versionadas y reproducibles.
- **C66 — IA como tutor (L3):** Comprobado en `S2-11` mediante el uso guiado y la bitácora de verificación humana.
