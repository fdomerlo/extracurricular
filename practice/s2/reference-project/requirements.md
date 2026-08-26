# Reference Project — Requirements S2

## Functional requirements

### Persistencia

- Persistir Patient, Professional y Appointment en una base de datos relacional.
- Migraciones versionadas: corren desde una base vacía y dejan el esquema correcto.
- El dominio de S1 sigue sin importar nada de persistencia (la capa de acceso a datos es adicional, no un reemplazo del dominio).

### Administración y roles

- Interfaz de administración con alta, edición y consulta de Appointment.
- Autenticación de usuarios.
- Dos roles: **profesional** y **secretaria**, con permisos distintos sobre qué agendas puede ver y modificar cada uno.

### Backup

- Procedimiento de backup documentado y ejecutado, restaurado y verificado al menos una vez.

## Invariants

Heredados de S1 (`practice/s1/reference-project/requirements.md`):

- un turno no puede tener dos estados;
- no puede confirmarse un turno cancelado;
- no puede cancelarse un turno atendido;
- fecha/hora debe ser válida.

Nuevos en S2:

- dos reservas simultáneas sobre el mismo turno no pueden coexistir (se verifica con un test de concurrencia real, no simulado).

## Datos sensibles — nota educativa

Este Reference Project usa exclusivamente datos ficticios y no maneja información de personas reales, por lo que no requiere investigación legal alguna. Pero si tu proyecto real llegara a manejar datos de salud u otro tipo de datos sensibles, investigar el marco legal aplicable en tu jurisdicción (protección de datos personales, datos sensibles, derechos del titular de la información) es parte de la competencia que se espera que desarrolles — practicá esa investigación con tu propio proyecto, no con este.

## Non-goals

En S2 no se requiere:

- vistas web propias fuera de la interfaz de administración (llega en S3);
- HTMX ni interactividad de frontend (S3);
- Docker ni CI (S3);
- despliegue en un servidor real (S5);
- observabilidad (S6).
