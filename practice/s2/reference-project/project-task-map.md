# Reference Project — Project Task Map S2

Mapeo entre las clases de S2 y las tareas prácticas sobre el proyecto del consultorio médico.

| Clase | Project Task | Artefacto Generado en el Repo |
|---|---|---|
| **S2-01** | Definir esquema DDL nativo del consultorio con UUIDs, claves foráneas y restricciones CHECK | `schema.sql` |
| **S2-02** | Crear dataset de prueba y redactar consultas analíticas de agenda y reportes a mano | `seed.sql`, `db/queries/queries.sql` |
| **S2-03** | Generar volumen sintético y medir planes de ejecución con `EXPLAIN ANALYZE` antes y después de indexar | `db/indexes.sql`, `docs/performance_notes.md` |
| **S2-04** | Reproducir condición de carrera de turnos solapados en dos terminales y documentar solución transaccional | `docs/concurrency_report.md` |
| **S2-05** | Integrar Django 5.x, declarar modelos del consultorio y generar migraciones auditadas con `sqlmigrate` | `agenda/models.py`, `agenda/migrations/` |
| **S2-06** | Erradicar consultas N+1 en la agenda con `select_related` y agregar tests con límite de query count | `agenda/services.py`, `tests/test_queries_performance.py` |
| **S2-07** | Configurar Django Admin profesional (`TurnoAdmin`, `PacienteAdmin`) con filtros, búsquedas y acciones | `agenda/admin.py` |
| **S2-08** | Implementar comando de roles RBAC (`setup_roles.py`) y restringir permisos de borrado en el admin | `agenda/management/commands/setup_roles.py`, `tests/test_rbac.py` |
| **S2-09** | Armar suite de tests de integración con `pytest-django` contra base PostgreSQL real | `pytest.ini`, `tests/test_integration_consultorio.py` |
| **S2-10** | Escribir scripts automatizados de respaldo/restauración y documentar simulacro de Disaster Recovery | `scripts/backup.sh`, `scripts/restore.sh`, `docs/backup_verification.md` |
| **S2-11** | Auditar críticamente sugerencias de código SQL/ORM generadas por IA y documentar bitácora de verificación | `docs/ai_log_s2.md` |
