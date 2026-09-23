# M-S2 — Aplicación persistente y acceso controlado

## Objetivo

Demostrar que el estudiante puede transformar el sistema de dominio en memoria de S1 en una aplicación persistente, transaccional, optimizada y administrable, garantizando la integridad de los datos ante concurrencia y fallos de infraestructura.

---

## Entregables Obligatorios

### 1. Esquema Relacional y Migraciones
- `schema.sql` con DDL nativo en PostgreSQL (claves primarias `UUID`, claves foráneas con `ON DELETE RESTRICT` y restricciones `CHECK`).
- Modelos de Django ORM con migraciones generadas y auditables mediante `python manage.py sqlmigrate`.
- Las migraciones se aplican exitosamente sobre una base de datos limpia desde cero.

### 2. Consultas y Optimización con Índices
- Archivo `db/queries/queries.sql` con consultas representativas (agenda, cancelaciones, reportes con agregación).
- Reporte `docs/performance_notes.md` con mediciones de `EXPLAIN ANALYZE` antes y después de indexar sobre un volumen de datos sintéticos representativo.

### 3. Evidencia Especial de Concurrencia Reproducible
- Documento `docs/concurrency_report.md` con:
  1. Escenario documentado de dos sesiones simultáneas que provocan solapamiento de turnos.
  2. Mecanismo de mitigación implementado (bloqueo transaccional, nivel de aislamiento o restricción de exclusión física).
  3. Verificación de que la condición de carrera ya no puede producirse.

### 4. Backoffice Operativo y RBAC
- Django Admin plenamente utilizable para la operación diaria (`TurnoAdmin`, `PacienteAdmin`, `ProfesionalAdmin`) con `list_display`, filtros, búsqueda y optimización `list_select_related`.
- Comando `agenda/management/commands/setup_roles.py` que crea de forma automatizada e idempotente los grupos `Recepcion`, `Profesional` y `Administracion`, bloqueando el borrado de datos a usuarios no autorizados.

### 5. Suite de Tests de Integración
- Suite con `pytest` y `pytest-django` ejecutándose exclusivamente contra PostgreSQL real.
- Pruebas que validan: persistencia fiel, rechazo de duplicados de DNI, bloqueo de borrado de pacientes con turnos, y límite estricto en la cantidad de consultas SQL (erradicación de N+1 con `django_assert_num_queries`).

### 6. Backup, Restore y Simulacro de Recuperación
- Scripts reproducibles `scripts/backup.sh` y `scripts/restore.sh`.
- Reporte `docs/backup_verification.md` que certifica la ejecución de un simulacro de recuperación ante desastres sobre una base limpia con verificación de conteo e integridad de tablas.

### 7. Bitácora de Verificación Humana de IA
- Documento `docs/ai_log_s2.md` registrando al menos un caso de asistencia técnica de IA donde el estudiante auditó críticamente el código generado, identificó una omisión o error, y aplicó la corrección correspondiente.

---

## Competency Gates Evaluados en M-S2

Para acreditar este milestone, el estudiante debe alcanzar el nivel requerido en cada uno de los 8 gates semestrales:

| Competencia | Descripción | Nivel requerido |
|---|---|:---:|
| **C14** | Tests de integración contra base real | **L3** |
| **C18** | Modelado relacional aplicado | **L4** |
| **C19** | SQL DDL y DML avanzado | **L4** |
| **C21** | Operación y configuración de PostgreSQL | **L3** |
| **C22** | Transacciones, ACID y aislamiento | **L4** |
| **C24** | ORM consciente y erradicación de N+1 | **L3** |
| **C25** | Migraciones reproducibles | **L3** |
| **C66** | IA como copiloto técnico con verificación humana | **L3** |

---

## Defensa Técnica Oral (30 minutos)

El estudiante debe defender su solución respondiendo preguntas de razonamiento y diseño:

1. ¿Por qué se utilizó `UUID` como clave primaria en lugar de enteros autoincrementales y qué impacto tiene en el desacoplamiento del dominio?
2. ¿Por qué aplanaste el objeto de valor `Horario` en la tabla `turno` en lugar de crear una tabla independiente?
3. ¿Cómo demostraste la condición de carrera de turnos superpuestos y cómo la previene tu solución a nivel de base de datos?
4. ¿Cuál es la diferencia matemática y de red entre `select_related` y `prefetch_related` en Django ORM?
5. ¿Qué información te brinda `EXPLAIN ANALYZE` que no aparece en un `EXPLAIN` simple?
6. ¿Por qué consideramos un antipatrón correr tests contra SQLite en memoria si el sistema opera con PostgreSQL?
7. ¿Cómo garantizaste que el proceso de backup y restore es íntegro y no pierde datos?
8. Mostrame un fragmento de código asistido por IA en este semestre: ¿qué error o supuesto incorrecto detectaste antes de commitearlo?

---

## Criterio de Evaluación

No se juzga la cantidad de líneas de código ni la velocidad de entrega.  
Se evalúa la **solidez de la persistencia, la reproducibilidad del entorno, la ausencia de consultas patológicas y la capacidad de defender técnicamente cada decisión tomada**.
