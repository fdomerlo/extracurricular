# S2 — Trazabilidad curricular

Este documento establece la trazabilidad de S2 desde la competencia hasta la evidencia observable.

La unidad mínima de trazabilidad es:

```text
competencia
    ↓
clase
    ↓
actividad (laboratorio / ejercicio / challenge)
    ↓
project task
    ↓
evidencia
    ↓
evidence milestone (M-S2)
    ↓
competency gate (según matriz curricular)
```

---

## 1. Criterio de lectura

Una competencia declarada en el frontmatter de una clase significa que la clase **trabaja explícitamente** esa competencia en el nivel indicado. No significa necesariamente que el estudiante alcance allí el nivel final de graduación definido en `curriculum/competencies.md`.

Estados de desarrollo:
- **I** — introducción;
- **P** — práctica;
- **C** — consolidación;
- **D** — demostración evaluable en gate.

### Separación conceptual: Milestone de evidencia vs. Competency Gate
- **Milestone de evidencia (`evidence.milestone`)**: Hito en el que el estudiante entrega el artefacto verificable de la clase (para S2, todas las clases aportan evidencias al milestone de fin de semestre `M-S2`).
- **Competency Gate**: Hito curricular formal donde la competencia es auditada para certificación de dominio según `curriculum/competency-matrix.md`. Las competencias cuyos gates vencen formalmente en `M-S2` son: **C14, C18, C19, C21, C22, C24, C25, C66**.

---

## 2. S2 de un vistazo

| Clase | Tema | Competencias | Nivel de clase | Evidencia principal | Milestone de evidencia | Competency Gate(s) |
|---|---|---|:---:|---|:---:|---|
| **S2-01** | Modelo relacional aplicado | C18, C19, C21 | L2 | `schema.sql` con DDL y restricciones CHECK | M-S2 | C18 (M-S2), C19 (M-S2), C21 (M-S2) |
| **S2-02** | SQL a mano y consultas | C19, C03 | L2 | `queries.sql` con joins y agregaciones | M-S2 | C19 (M-S2), C03 (M-S6) |
| **S2-03** | Índices y EXPLAIN | C20, C57 | L2 | `performance_notes.md` con EXPLAIN ANALYZE | M-S2 | C20 (M-S5), C57 (M-S5) |
| **S2-04** | Transacciones y concurrencia | C22, C23 | L3 | `concurrency_report.md` con escenario reproducible | M-S2 | C22 (M-S2), C23 (M-S4) |
| **S2-05** | ORM y migraciones | C24, C25, C04 | L2 | Modelos Django y migraciones auditadas | M-S2 | C24 (M-S2), C25 (M-S2), C04 (M-S4) |
| **S2-06** | Optimización ORM (N+1) | C20, C24 | L3 | Tests con aserción de conteo de queries | M-S2 | C24 (M-S2), C20 (M-S5) |
| **S2-07** | Django Admin como backoffice | C29, C40 | L2 | `ModelAdmin` configurado y usable | M-S2 | C29 (M-S3), C40 (M-S4) |
| **S2-08** | Autenticación y RBAC | C34, C35, C33 | L2 | `setup_roles.py` y restricción de borrado | M-S2 | C34 (M-S3), C35 (M-S3), C33 (M-S3) |
| **S2-09** | Tests con PostgreSQL real | C14, C13 | L3 | Suite `pytest-django` contra base real | M-S2 | C14 (M-S2), C13 (M-S6) |
| **S2-10** | Backup y consistencia | C26, C45 | L2 | Scripts `backup/restore` y simulacro de DR | M-S2 | C26 (M-S5), C45 (M-S4) |
| **S2-11** | IA copiloto y verificación | C66, C67, C71 | L3 | `ai_log_s2.md` con auditoría humana | M-S2 | C66 (M-S2), C67 (M-S6), C71 (M-S5) |

---

## 3. Detalle de Trazabilidad por Clase

### S2-01 — Modelo relacional aplicado
- **Competencias:** C18 (Modelado relacional), C19 (SQL), C21 (PostgreSQL).
- **Evidencia E-S2-01:** `schema.sql` con claves primarias `UUID`, relaciones `FOREIGN KEY` y restricciones `CHECK` reflejando las reglas de negocio de S1.
- **Gates asociados:** C18 (M-S2), C19 (M-S2), C21 (M-S2).

### S2-02 — SQL a mano: Consultas, joins y agregaciones
- **Competencias:** C19 (SQL), C03 (Modelado de dominio).
- **Evidencia E-S2-02:** `db/queries/queries.sql` con agenda diaria (`INNER JOIN`), reporte de profesionales (`LEFT JOIN` con `COUNT`) y pacientes frecuentes (`GROUP BY` + `HAVING`).
- **Gates asociados:** C19 (M-S2), C03 (M-S6).

### S2-03 — Índices y planes de ejecución
- **Competencias:** C20 (Optimización de consultas), C57 (Performance).
- **Evidencia E-S2-03:** `docs/performance_notes.md` con trazas de `EXPLAIN ANALYZE` sobre 20.000 turnos sintéticos antes y después de indexar.
- **Gates asociados:** C20 (M-S5), C57 (M-S5).

### S2-04 — Transacciones, ACID y concurrencia reproducible
- **Competencias:** C22 (Transacciones y ACID), C23 (Concurrencia).
- **Evidencia E-S2-04:** `docs/concurrency_report.md` con la simulación interactiva de dos sesiones concurrentes que intentan reservar el mismo turno, demostrando la colisión y la solución mediante bloqueos transaccionales o exclusión física.
- **Gates asociados:** C22 (M-S2), C23 (M-S4).

### S2-05 — ORM consciente y migraciones desde el dominio
- **Competencias:** C24 (ORM consciente), C25 (Migraciones), C04 (Software modular).
- **Evidencia E-S2-05:** Modelos de Django que replican el esquema de `S2-01`, migraciones versionadas y auditoría de paridad con `python manage.py sqlmigrate`.
- **Gates asociados:** C24 (M-S2), C25 (M-S2), C04 (M-S4).

### S2-06 — Optimización de consultas con ORM: El problema N+1
- **Competencias:** C20 (Optimización de consultas), C24 (ORM consciente).
- **Evidencia E-S2-06:** Erradicación del defecto N+1 con `.select_related()` y `.prefetch_related()`, respaldada por tests automatizados con `django_assert_num_queries`.
- **Gates asociados:** C24 (M-S2), C20 (M-S5).

### S2-07 — Interfaz de acceso operativo: Django Admin
- **Competencias:** C29 (Aplicaciones Web), C40 (Arquitectura modular).
- **Evidencia E-S2-07:** Panel de administración `TurnoAdmin` configurado con columnas informativas, filtros por fecha/profesional, búsqueda por DNI y optimización `list_select_related`.
- **Gates asociados:** C29 (M-S3), C40 (M-S4).

### S2-08 — Autenticación y permisos por rol (RBAC) en backoffice
- **Competencias:** C34 (Autenticación), C35 (RBAC), C33 (Identidad y sesiones).
- **Evidencia E-S2-08:** Comando `setup_roles.py` que crea grupos `Recepcion`, `Profesional` y `Administracion`, bloqueando borrados a operadores no administradores (con test de rechazo HTTP 403).
- **Gates asociados:** C34 (M-S3), C35 (M-S3), C33 (M-S3).

### S2-09 — Testing de integración contra PostgreSQL real
- **Competencias:** C14 (Tests de integración), C13 (Tests unitarios).
- **Evidencia E-S2-09:** Suite `tests/test_integration_consultorio.py` corriendo con `pytest-django` contra base PostgreSQL real, validando persistencia, restricciones de unicidad e integridad referencial.
- **Gates asociados:** C14 (M-S2), C13 (M-S6).

### S2-10 — Backup, restore y consistencia de datos
- **Competencias:** C26 (Backup y Restore), C45 (Entornos reproducibles).
- **Evidencia E-S2-10:** Scripts `scripts/backup.sh` y `scripts/restore.sh`, junto a `docs/backup_verification.md` certificando el simulacro de recuperación ante desastres sin pérdida de datos.
- **Gates asociados:** C26 (M-S5), C45 (M-S4).

### S2-11 — IA como copiloto técnico con verificación estricta
- **Competencias:** C66 (IA como tutor), C67 (IA como herramienta), C71 (Verificación humana).
- **Evidencia E-S2-11:** Bitácora `docs/ai_log_s2.md` documentando la detección y corrección de alucinaciones o errores sutiles en código SQL/ORM generado por IA.
- **Gates asociados:** C66 (M-S2), C67 (M-S6), C71 (M-S5).

---

## 4. Evidencia Acumulada hacia Milestone M-S2

```text
E-S2-01 (DDL & Constraints) ────────┐
E-S2-02 (SQL Queries) ──────────────┤
E-S2-03 (EXPLAIN ANALYZE) ──────────┤
E-S2-04 (Concurrencia reproducible) ┤
E-S2-05 (ORM & Migraciones) ────────┼───► Milestone M-S2
E-S2-06 (Erradicación N+1) ─────────┤     (8 Competency Gates)
E-S2-07 (Backoffice Admin) ─────────┤
E-S2-08 (RBAC & Seguridad) ─────────┤
E-S2-09 (Tests de integración) ─────┤
E-S2-10 (Backup / Restore) ─────────┤
E-S2-11 (Verificación humana IA) ───┘
```

---

## 5. Auditoría de Cobertura en S2

- **Competencias con Gate principal en M-S2:** C14, C18, C19, C21, C22, C24, C25, C66. Todas cuentan con clases prácticas dedicadas y evidencias de entrega específicas.
- **Competencias en práctica o consolidación con Gate futuro:**
  - C03, C04, C13, C40, C45 (Gates en M-S4 o M-S6)
  - C20, C26, C57, C71 (Gates en M-S5)
  - C29, C33, C34, C35 (Gates en M-S3)
  - C23 (Gate en M-S4)
  - C67 (Gate en M-S6)
- **Consistencia de esquemas:** 100% verificado contra `curriculum/competencies.md` y `curriculum/competency-matrix.md`.
