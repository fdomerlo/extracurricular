# Reference Project — Requirements S3

## Functional requirements

### Vistas propias

- Reservar, confirmar y cancelar un turno desde una vista propia (no la interfaz de administración).
- Interactividad de las acciones más frecuentes (confirmar, cancelar) sin recargar la página completa.

### Autenticación y permisos

- Tres roles con permisos distintos: profesional, secretaria, paciente.
- Un usuario sin sesión válida no accede a ningún dato de turnos o pacientes.

### Seguridad

- Mitigar inyección, XSS, CSRF y control de acceso roto en las vistas propias.
- Documentar qué protege el framework por defecto y qué queda bajo responsabilidad del proyecto.

### Despliegue

- Servidor con proxy inverso y HTTPS.
- Logs de aplicación y backups automatizados.
- El sistema completo vuelve a funcionar solo si el servidor se reinicia.

## Invariants

Heredados de S1 y S2 (`practice/s1/reference-project/requirements.md`, `practice/s2/reference-project/requirements.md`), sin cambios en S3.

## Datos sensibles — nota educativa

Este Reference Project usa exclusivamente datos ficticios y no maneja información de personas reales, por lo que no requiere investigación legal alguna. Pero si tu proyecto real llegara a manejar datos de salud u otro tipo de datos sensibles, investigar el marco legal aplicable en tu jurisdicción (protección de datos personales, datos sensibles, derechos del titular de la información) es parte de la competencia que se espera que desarrolles — practicá esa investigación con tu propio proyecto, no con este.

## Non-goals

En S3 no se requiere:

- containerización ni CI antes de `S3-09` (llegan dentro de este mismo semestre);
- procesos en segundo plano (S4);
- procedimientos formales de despliegue/rollback en producción (S5);
- observabilidad más allá de logs básicos (S6).
