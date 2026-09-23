# M-S2 Rubric

Rúbrica pública de evaluación y autodiagnóstico para el Milestone `M-S2`.

| Dimensión | Excelente | Aceptable | Insuficiente |
|---|---|---|---|
| **Modelo Relacional** | Esquema DDL riguroso con UUIDs, tipos precisos, claves foráneas e integridad referencial exhaustiva. | Tablas funcionales con claves foráneas básicas. | Tipos inadecuados, falta de claves foráneas o campos desnormalizados sin justificación. |
| **SQL y Consultas** | Consultas complejas con joins, agregaciones y CTEs escritas a mano con legibilidad y exactitud matemática. | Consultas funcionales para los reportes principales. | Dificultad para formular consultas sin depender de la ayuda de un ORM. |
| **Optimización e Índices** | Interpreta `EXPLAIN ANALYZE` con rigor; diseña índices compuestos basados en selectividad y mide impacto. | Agrega índices que mejoran los tiempos de respuesta. | Agrega índices a ciegas sin medir o desconoce la diferencia entre Seq Scan e Index Scan. |
| **Concurrencia y ACID** | Reproduce la condición de carrera con precisión y la resuelve mediante transacciones, bloqueos o exclusión. | Conoce el concepto y previene el solapamiento en escenarios estándar. | No puede reproducir la condición de carrera o confía en validaciones en memoria. |
| **ORM y Migraciones** | Modelos reflejan fielmente el esquema; migraciones limpias y auditadas con `sqlmigrate`; dominio desacoplado. | Modelos y migraciones funcionales. | Migraciones corruptas, cambios manuales en base sin migración o acoplamiento excesivo. |
| **Control de N+1** | Erradica N+1 con `select_related` y `prefetch_related`; tests con aserciones de conteo de consultas. | Resuelve N+1 en las vistas principales. | Presenta consultas N+1 en bucles que degradan la base de datos. |
| **Backoffice y RBAC** | Django Admin personalizado con filtros, búsquedas y permisos segregados por roles operativos (RBAC). | Admin operativo con roles básicos. | Acceso sin restricciones con superusuario para todas las tareas. |
| **Testing de Integración** | Suite con `pytest-django` contra PostgreSQL real, transaccional, rápida (<5s) y cubriendo casos límite. | Tests contra PostgreSQL que verifican el camino feliz. | Tests contra SQLite o ausencia de pruebas de base de datos. |
| **Operación y Respaldo** | Scripts automatizados de backup/restore y evidencia documentada de simulacro de recuperación íntegro. | Backup y restore ejecutados manualmente. | No se probó la restauración o se perdieron datos en el proceso. |
| **Verificación de IA** | Bitácora con análisis crítico de código asistido; detecta alucinaciones y supuestos erróneos antes del commit. | Explica el código asistido por IA. | Acepta código de IA sin auditar o no puede explicar el SQL generado. |
| **Defensa Técnica** | Justifica con solvencia técnica cada decisión de persistencia, diseño y concurrencia. | Explica las decisiones principales. | No puede fundamentar las decisiones o titubea en conceptos nucleares. |
