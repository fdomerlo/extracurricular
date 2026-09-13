# Tutoría

La tutoría es la modalidad acompañada del programa. El curriculum y los materiales educativos permanecen abiertos y gratuitos; la tutoría aporta acompañamiento humano, revisión de código y evaluación formativa sobre el trabajo real del estudiante.

## Propósito

La tutoría no consiste en repetir las clases ni en desarrollar el proyecto por el estudiante.

Su propósito es ayudar al estudiante a:

- convertir un problema en un plan de desarrollo;
- tomar decisiones técnicas y justificar sus trade-offs;
- detectar errores conceptuales y técnicos;
- desarrollar capacidad de debugging;
- recibir feedback sobre código, arquitectura y documentación;
- producir evidencia de sus competencias;
- sostener un proyecto durante varios semestres;
- aprender a defender técnicamente lo construido.

> El tutor ayuda a razonar. El estudiante construye y responde por sus decisiones.

> **Módulo operativo:** Toda la documentación operativa de tutorías, los protocolos de sesión y los formularios de consulta previa viven en la carpeta [`../tutoring/`](../tutoring/README.md).

## Qué recibe el estudiante

La modalidad de tutoría se apoya en el mismo curriculum que la modalidad autodidacta, pero agrega acompañamiento humano.

### Seguimiento periódico

Las tutorías se realizan aproximadamente cada dos semanas. La frecuencia concreta se acuerda según el plan de trabajo y la disponibilidad.

Una sesión puede utilizarse para:

- revisar el avance desde la sesión anterior;
- analizar bloqueos;
- revisar decisiones técnicas;
- hacer debugging;
- revisar una Pull Request;
- analizar arquitectura;
- definir una investigación técnica;
- preparar una evidencia o milestone;
- establecer el siguiente objetivo.

### Code review

El objetivo del code review no es corregir código por el estudiante, sino enseñarle a detectar y resolver problemas de:

- diseño;
- legibilidad;
- testing;
- errores y estados;
- seguridad;
- mantenibilidad;
- arquitectura;
- deuda técnica.

Los comentarios deben conducir a decisiones que el estudiante pueda comprender y aplicar posteriormente sin asistencia.

### Evaluación

El progreso se contrasta con las competencias y evidencias definidas en [`../curriculum/competencies.md`](../curriculum/competencies.md) y [`../curriculum/assessment.md`](../curriculum/assessment.md).

La tutoría no reemplaza la evidencia. La ayuda a producirla y a interpretarla.

## Qué no incluye

La tutoría no implica:

- escribir el código del estudiante;
- resolver por él los ejercicios;
- elegir automáticamente la arquitectura;
- convertir cada sesión en una clase particular;
- garantizar que una implementación sea correcta sin que el estudiante pueda explicarla;
- sustituir una carrera universitaria o una formación formal previa.

## Proyecto

El estudiante puede trabajar sobre:

1. un proyecto propio;
2. un proyecto con cliente real;
3. un proyecto propuesto dentro del proceso de tutoría;
4. el Reference Project del repositorio.

La exigencia curricular es la misma. Lo que cambia es el contexto.

El proyecto evoluciona incrementalmente durante los seis semestres:

> `S1 Dominio` → `S2 Persistencia & API` → `S3 Aplicación & CI/CD` → `S4 Arquitectura distribuida` → `S5 Producción & Observabilidad` → `S6 Evolución & Defensa final`

## Flujo de trabajo

> `Trabajo autónomo` → `Evidencia / PR` → `Sesión de tutoría` → `Feedback & Code review` → `Corrección` → `Siguiente objetivo`

Entre sesiones, el estudiante continúa trabajando de forma autónoma. La tutoría debe aumentar progresivamente su autonomía, no crear dependencia del tutor.

### Formularios de consulta previa

Para optimizar el tiempo de cada encuentro sincrónico, el estudiante completa y envía con antelación el formulario adecuado a su situación:

- **Traba técnica o duda conceptual:** [`../tutoring/templates/technical-blocker.md`](../tutoring/templates/technical-blocker.md)
- **Decisión de diseño o arquitectura:** [`../tutoring/templates/architecture-review.md`](../tutoring/templates/architecture-review.md)
- **Revisión y defensa de milestone:** [`../tutoring/templates/milestone-check.md`](../tutoring/templates/milestone-check.md)

Consultá la guía completa en [`../tutoring/README.md`](../tutoring/README.md).

## Milestones

Al cierre de cada semestre se realiza una revisión de integración. El objetivo es comprobar que el estudiante puede demostrar las competencias trabajadas y explicar las decisiones relevantes del proyecto.

La evidencia puede incluir:

- código;
- tests;
- Pull Requests;
- documentación;
- ADRs;
- despliegues;
- diagnósticos;
- defensas orales.

## IA durante la tutoría

La IA puede utilizarse como herramienta de aprendizaje e ingeniería de acuerdo con la política del curriculum. El criterio fundamental es que el estudiante pueda explicar, verificar, modificar y defender cualquier código que incorpore al proyecto.

La tutoría puede utilizarse para revisar cómo se utilizó IA, detectar errores de razonamiento y mejorar el proceso de verificación.

## Acceso y disponibilidad

La tutoría es un servicio profesional arancelado con **cupos limitados** por dedicación docente. El repositorio es abierto y no condiciona el acceso al conocimiento ni el avance autodidacta a la contratación de tutorías.

### Cómo solicitar admisión o una sesión

Para postularte a la modalidad acompañada o coordinar una revisión técnica:

1. Completá el formulario adecuado a tu situación:
   - Para solicitar admisión o evaluar tu punto de partida: la [`evaluación diagnóstica inicial`](../assessment/diagnostic/initial-evaluation.md).
   - Para destrabar un problema técnico en curso: la plantilla de [`desbloqueo técnico`](../tutoring/templates/technical-blocker.md).
   - Para evaluar decisiones de arquitectura: la plantilla de [`revisión de diseño`](../tutoring/templates/architecture-review.md).
2. Enviá tu solicitud o consulta por correo electrónico a **`fdomerlo@gmail.com`** con el asunto:
   ```text
   [Extracurricular] Solicitud de Tutoría - <Tu Nombre y Apellido>
   ```
3. Adjuntá el formulario completado y el enlace a tu repositorio o proyecto.
4. El tutor revisará las evidencias y coordinará una breve llamada de alineación técnica para confirmar vacantes, condiciones y calendario.

Consultá los protocolos de preparación en [`../tutoring/README.md`](../tutoring/README.md).

## Principio de independencia

El objetivo de la tutoría es que cada semestre el estudiante necesite menos ayuda para resolver problemas equivalentes.

> Una buena tutoría termina produciendo autonomía.
