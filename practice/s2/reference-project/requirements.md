# Reference Project — Requirements S2 (Persistir y servir)

## Functional Requirements

### 1. Persistencia y Consultorio Relacional
- Almacenar pacientes, profesionales, catálogo de prácticas y turnos en PostgreSQL 16+.
- Registrar cancelaciones de turnos con fecha, motivo y bandera de cancelación tardía.
- Consultar la agenda diaria ordenada cronológicamente y generar reportes de turnos por profesional.

### 2. Operación y Gestión Administrativa
- Administrar pacientes y turnos mediante el backoffice de Django Admin.
- Control de acceso basado en roles (RBAC): recepción (sin permisos de eliminación), profesionales (solo lectura de agenda) y administradores.

### 3. Operaciones de Datos
- Respaldar la base de datos de forma automatizada mediante script con `pg_dump`.
- Restaurar el sistema sobre una base vacía mediante script con `pg_restore` sin pérdida de información.

---

## Technical Invariants

1. **Identidad Desacoplada:** Todas las tablas principales emplean `UUID` como clave primaria, permitiendo que el dominio genere identidades antes de persistir.
2. **Integridad Referencial:** Ningún turno puede quedar huérfano; la eliminación de un paciente o profesional con turnos asociados está bloqueada por base de datos (`ON DELETE RESTRICT`).
3. **Invariante Temporal:** Todo turno debe satisfacer `hora_inicio < hora_fin` validado por restricción física `CHECK`.
4. **Protección de Concurrencia:** Dos transacciones simultáneas no pueden agendar el mismo profesional en horarios superpuestos (inconsistencia prevenida por bloqueos pesimistas, serialización o restricciones de exclusión).
5. **Eficiencia de Acceso:** La consulta de agenda no incurre en el problema N+1 (verificado mediante pruebas automáticas con `django_assert_num_queries`).

---

## Non-goals para S2

En este semestre explícitamente **no se requiere**:
- Vistas web públicas personalizadas ni maquetado frontend (HTML, CSS, JS, HTMX) — contenido central de **S3**.
- Despliegue en infraestructura cloud ni contenedores de producción — contenido de **S4 y S5**.
- Procesamiento en segundo plano con colas asincrónicas (Celery / Redis) — contenido de **S4**.
