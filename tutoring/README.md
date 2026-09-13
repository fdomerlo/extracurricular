# Comunicación Técnica y Plantillas de Consulta

Este módulo proporciona los protocolos y plantillas de estructuración técnica de **Extracurricular**.

> **Principio:** Describir un problema con precisión técnica, aislar su contexto y formular una hipótesis antes de consultar es una competencia profesional fundamental de ingeniería.

---

## 1. Propósito de las Plantillas

Tanto si estás aprendiendo de forma autónoma como si contás con el acompañamiento de un tutor o par de estudio, estas plantillas te ayudan a estructurar tu razonamiento y no perder tiempo:

- **Autodidactas:** Funcionan como un ejercicio estructurado de *rubber ducking* (depuración del patito de goma) y documentación técnica de decisiones para tu portfolio.
- **Estudiantes con tutoría:** Constituyen el *Asynchronous Intake*: el formulario obligatorio que se completa y comparte antes de una sesión sincrónica o revisión de código.

---

## 2. Plantillas Disponibles

Las plantillas se encuentran en [`templates/`](templates/):

| Situación | Plantilla | Cuándo utilizarla |
|---|---|---|
| **Traba técnica o duda conceptual** | [`templates/technical-blocker.md`](templates/technical-blocker.md) | Ante un fallo o bug bloqueante. Exige registrar el traceback, aislar el caso mínimo, completar el checklist de verificación previa y formular una hipótesis de causa raíz. |
| **Decisión de diseño o arquitectura** | [`templates/architecture-review.md`](templates/architecture-review.md) | Antes de realizar una refactorización grande o adoptar una librería/patrón nuevo. Exige exponer al menos 2 alternativas evaluadas y sus trade-offs. |
| **Defensa de hito o entrega** | [`templates/milestone-check.md`](templates/milestone-check.md) | Previo al cierre de un milestone semestral. Permite auto-auditar las precondiciones (tests en verde, estilo, docs) y verificar el dominio de competencias. |

---

## 3. Dinámica Recomendada ante un Bloqueo Técnico

Antes de pedir ayuda externa o consultar a un asistente de IA:

> `1. Reproducir fallo` → `2. Aislar caso mínimo` → `3. Completar plantilla` → `4. Formular hipótesis` → `5. Consultar con evidencia`

Muchos bloqueos se resuelven espontáneamente durante el proceso de responder las preguntas de la plantilla. Si el bloqueo persiste, la persona que te ayude dispondrá de toda la evidencia técnica necesaria para orientarte sin perder tiempo en explicaciones ambiguas.

---

## 4. Admisión a la Modalidad Acompañada y Contacto

La tutoría personalizada es un servicio profesional arancelado con **cupos estrictamente limitados** para garantizar profundidad en el seguimiento, code reviews formativos exhaustivos y sesiones individuales de defensa técnica.

### Proceso de Admisión y Solicitud

1. **Autodiagnóstico inicial:** Completá la [`Evaluación Diagnóstica Inicial`](../assessment/diagnostic/initial-evaluation.md) para mapear tu punto de partida, contexto y disponibilidad.
2. **Envío formal de solicitud:** Enviá un correo electrónico a **[fdomerlo@gmail.com](mailto:fdomerlo@gmail.com)** con el asunto: `Extracurricular, Solicitud de Tutoría - <Tu Nombre y Apellido>`
3. **Información a incluir en el mensaje:**
   - Breve presentación de tu trayectoria y tus objetivos profesionales.
   - Enlace a tu repositorio o proyecto sobre el que trabajarás (Reference Project o desarrollo propio).
   - La evaluación diagnóstica completada (o la plantilla de consulta correspondiente).
   - Disponibilidad horaria tentativa para sesiones sincrónicas (habitualmente quincenales).
4. **Alineación y coordinación:** Si existen cupos disponibles en el período lectivo actual, coordinaremos una llamada breve de diagnóstico y alineación técnica para formalizar el plan de trabajo y el calendario.
