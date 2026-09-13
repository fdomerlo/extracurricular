# Getting Started

Este repositorio puede utilizarse de forma completamente autodidacta o como base para un recorrido acompañado por tutoría.

## Antes de empezar

No es un curso introductorio de programación. El programa parte de que ya podés leer y escribir código y querés convertir esa capacidad en una práctica de desarrollo más profesional.

Si todavía estás aprendiendo los fundamentos absolutos de programación, conviene consolidarlos antes de comenzar S1.

> **¿Dónde vive tu código?** Este repositorio contiene el currículo y las clases. Tu código personal y tu proyecto deben vivir en un repositorio propio bajo tu cuenta de GitHub. Seguí las instrucciones detalladas en [`student-workflow.md`](student-workflow.md).

## Elegí tu modalidad

### Autodidacta

Avanzá a tu propio ritmo utilizando todos los materiales abiertos, el Reference Project y las suites de tests:

> `Curriculum` → `Clases y Práctica` → `Proyecto` → `Evidencia` → `Autoevaluación` → `Milestone`

### Con tutoría

Seguí exactamente el mismo curriculum y agregá acompañamiento profesional: revisión periódica, code review, debugging y seguimiento de competencias.

Ver [`tutoring.md`](tutoring.md).

### Ritmo y dedicación

La duración de referencia está calculada en **tres años** (~22 semanas por semestre a razón de 10–12 hs semanales), pensada para ser compatible con empleo o estudios universitarios. Al estar guiado por **competencias y evidencias**, tu progreso no depende de plazos fijos: si disponés de mayor dedicación semanal o experiencia previa, podés completarlo en **1 a 2 años** acreditando los hitos (*milestones*). Consultá la tabla de dedicación en [`faq.md`](faq.md).

## Paso 1 — Entender el mapa

Empezá por [`../curriculum/study-plan.md`](../curriculum/study-plan.md).

Después revisá:

- [`../curriculum/competencies.md`](../curriculum/competencies.md) — qué capacidades desarrolla el programa;
- [`../curriculum/competency-matrix.md`](../curriculum/competency-matrix.md) — dónde aparece cada competencia;
- [`../curriculum/assessment.md`](../curriculum/assessment.md) — cómo se produce y evalúa la evidencia.

No es necesario leer los tres documentos completos antes de empezar. El objetivo es comprender la arquitectura general.

## Paso 2 — Comenzar S1

Entrá en [`../practice/s1/`](../practice/s1/).

El README del semestre explica el objetivo, la carga y la estructura. El contenido de las clases está en [`../practice/s1/classes/`](../practice/s1/classes/).

S1 es la primera implementación completa del curriculum y sirve como referencia de cómo deben estructurarse los semestres posteriores.

## Paso 3 — Elegir el proyecto

Tenés dos caminos principales.

### Reference Project

Si no tenés un problema propio, utilizá el proyecto de referencia incluido en S1.

Esto permite recorrer el curriculum sin necesitar un cliente real.

### Proyecto propio

Si ya tenés un problema que querés resolver, empezá por [`../project/project-brief.md`](../project/project-brief.md).

El proyecto puede ser:

- personal;
- académico;
- profesional;
- para un cliente real;
- una aplicación que quieras convertir en portfolio.

No intentes diseñar toda la arquitectura desde el principio. El proyecto debe crecer a medida que las competencias lo requieren.

## Paso 4 — Trabajar cada clase

El flujo recomendado es:

> `Concepto` → `Clase` → `Laboratorio / Ejercicio` → `Challenge` → `Aplicación al proyecto` → `Evidencia`

No midas el progreso por cantidad de páginas leídas. Medilo por lo que podés construir, explicar, probar y defender.

## Paso 5 — Registrar decisiones

Cuando una decisión técnica sea relevante, documentala.

Usá ADRs u otro mecanismo equivalente dentro del proyecto. Registrá especialmente decisiones sobre:

- arquitectura;
- modelo de datos;
- dependencias;
- seguridad;
- concurrencia;
- deployment;
- observabilidad.

El objetivo no es producir documentación burocrática. Es hacer visible el razonamiento.

## Paso 6 — Producir evidencia

Cada competencia necesita evidencia observable.

Puede tratarse de:

- laboratorio;
- ejercicio;
- challenge;
- proyecto;
- code review;
- Pull Request;
- defensa oral;
- documento técnico.

Consultá [`../curriculum/assessment.md`](../curriculum/assessment.md) para el marco completo.

## Paso 7 — Completar el milestone

Al finalizar el semestre no avances automáticamente al siguiente.

Primero comprobá:

- qué competencias alcanzaste;
- qué evidencia las demuestra;
- qué problemas todavía no podés resolver con autonomía;
- qué decisiones podés defender;
- qué aspectos del proyecto necesitan refactorización.

El milestone es una instancia de integración, no solamente una lista de tareas terminadas.

## Paso 8 — Continuar

La progresión general es:

| Semestre | Tema | Pregunta central |
|---|---|---|
| S1 | Construir | ¿Puedo construir software pequeño correctamente? |
| S2 | Persistir y servir | ¿Puedo construir una aplicación persistente y segura? |
| S3 | Entregar software | ¿Puedo llevar una aplicación hasta un entorno desplegable? |
| S4 | Diseñar sistemas | ¿Puedo diseñar sistemas más complejos y justificar sus trade-offs? |
| S5 | Producción | ¿Puedo operar y recuperar un servicio real? |
| S6 | Diseñar y liderar | ¿Puedo tomar decisiones de arquitectura y defender un sistema completo? |

## Stack de referencia

El curriculum está centrado en competencias, no en frameworks. Sin embargo, el material práctico necesita una implementación concreta.

La implementación de referencia utiliza principalmente Python y tecnologías de infraestructura y datos apropiadas para cada etapa. El stack puede evolucionar sin cambiar las competencias que el estudiante debe demostrar.

## Regla de trabajo

> No avances porque terminaste una lectura. Avanzá cuando puedas demostrar una capacidad.

## Si usás IA

La IA puede ayudarte a explicar conceptos, generar hipótesis, revisar código o investigar alternativas, pero no reemplaza la evidencia.

Antes de incorporar una salida generada por IA, preguntate:

1. ¿Entiendo qué hace?
2. ¿Puedo verificar que funciona?
3. ¿Puedo modificarla?
4. ¿Puedo explicar sus decisiones y limitaciones?

Si la respuesta es no, todavía no forma parte de tu solución.

## Si querés acompañamiento o tutoría

Si deseás acompañamiento personalizado, code review formativo o defensa de hitos:

1. Completá la [`evaluación diagnóstica inicial`](../assessment/diagnostic/initial-evaluation.md) (o la plantilla de [`desbloqueo técnico`](../tutoring/templates/technical-blocker.md) si ya estás cursando).
2. Enviá tu postulación por correo electrónico a **`fdomerlo@gmail.com`** con el asunto `[Extracurricular] Solicitud de Tutoría - <Tu Nombre>` adjuntando el formulario completado y el enlace a tu repositorio.
3. El tutor revisará tus evidencias para confirmar disponibilidad de vacantes y coordinar la agenda de trabajo.

Más detalles sobre la modalidad y plantillas operativas en [`tutoring/`](../tutoring/README.md).
