# Desarrollo Moderno de Software

Un recorrido práctico de tres años para aprender desarrollo de software moderno mediante **competencias + proyecto + evidencia + mentoría**. No reemplaza una carrera universitaria: es para quien ya sabe programar algo y quiere convertir eso en capacidad profesional, con o sin mentor.

No está organizado alrededor de frameworks. Está organizado alrededor de la capacidad de:

```text
entender un problema
→ modelarlo
→ construirlo
→ probarlo
→ desplegarlo
→ operarlo
→ medirlo
→ evolucionarlo
→ defender las decisiones
```

Las tecnologías cambian. Las capacidades permanecen.

## ¿Es esto para vos?

**Autodidacta sin proyecto propio.** Arrancás en [`practice/s1/reference-project/`](practice/s1/reference-project/), seguís [`curriculum/study-plan.md`](curriculum/study-plan.md) semestre por semestre, y te evaluás contra [`curriculum/assessment.md`](curriculum/assessment.md).

**Estudiante con proyecto propio (con o sin mentor).** Empezás completando [`project/project-brief.md`](project/project-brief.md). [`curriculum/study-plan.md`](curriculum/study-plan.md) es tu plan base — un ejemplo real de cómo se completa esa plantilla para una instancia concreta está en [`project/students/consultorio-odontologico/`](project/students/consultorio-odontologico/).

**Mentor evaluando usar esto con alguien.** El contrato pedagógico completo está en [`curriculum/competencies.md`](curriculum/competencies.md) (qué sabe hacer un egresado) y [`curriculum/assessment.md`](curriculum/assessment.md) (cómo se audita). El modelo de mentoría está en [`project/project-model.md`](project/project-model.md).

## Modalidades de uso y mentoría

El currículum, los lineamientos del proyecto y la estructura de evaluación de este repositorio son **100% open source y gratuitos**. El objetivo es que cualquier persona con disciplina pueda formarse con estándares reales de la industria.

Puedes usar este material de tres formas:

### 1. Modalidad autodidacta (gratuita)

Clonas el repositorio, sigues el plan de estudios por tu cuenta usando el `Reference Project` (o tu propio proyecto) y te autoevalúas utilizando las rúbricas provistas en `curriculum/assessment.md`.

### 2. Mentoría personalizada y code reviews (arancelado)

El material es libre, pero el tiempo de revisión técnica no lo es. Si quieres que el proyecto que construyas tenga el rigor de un entorno laboral real, ofrezco cupos limitados para mentoría 1 a 1. Esto incluye:

- Code reviews detallados de tus pull requests cada dos semanas.
- Sesiones de depuración (debugging) en vivo cuando te bloquees.
- Auditoría de arquitectura y seguridad de tu proyecto.
- Simulacro de entrevista y defensa técnica al finalizar cada semestre.

*(Para consultar disponibilidad y valores, contáctame a [fdomerlo@gmail.com](mailto:fdomerlo@gmail.com)).*

### 3. Clases específicas / consultoría

Si eres un equipo, una institución, o un grupo de estudiantes que necesita una clase profunda sobre un tema específico del plan (ej. *diseño de APIs, concurrencia en bases de datos, Docker/CI*), ofrezco capacitaciones a medida.

## Arquitectura educativa

```text
CURRICULUM
   │
   ├── teoría
   │    └── bibliografía y recursos
   │
   └── práctica
        ├── clases
        ├── labs
        ├── challenges
        └── project tasks
                  │
                  ▼
             PROYECTO
                  │
                  ▼
             MENTORÍA
          aproximadamente
           cada 2 semanas
                  │
                  ▼
              EVIDENCIA
                  │
                  ▼
              MILESTONE
```

## Duración

3 años / 6 semestres.

Cada semestre se modela sobre aproximadamente **22 semanas académicas**, dejando margen para recesos, exámenes, enfermedad, retrasos y recuperación.

Cada semestre contiene:

- **entre 11 y 17 clases principales**, según el semestre
- trabajo autónomo entre clases
- mentorías aproximadamente cada 2 semanas
- integración de proyecto
- milestone y defensa
- buffer

Las clases son unidades pedagógicas, no necesariamente sesiones de una hora: una puede ocupar más de una semana.

## Progresión

| Semestre | Tema | Resultado |
|---|---|---|
| S1 | Construir | software pequeño, modular, testeable y versionado |
| S2 | Persistir y servir | aplicación persistente + API |
| S3 | Entregar software | producto full-stack desplegado + CI/CD |
| S4 | Diseñar sistemas | sistema escalable, asíncrono y observable |
| S5 | Producción | servicio productivo operable y recuperable |
| S6 | Diseñar y liderar | arquitectura, producto y proyecto final |

## Proyecto longitudinal

Cada estudiante puede:

1. aportar su propio proyecto;
2. trabajar con un cliente real;
3. trabajar con un proyecto propuesto por un mentor;
4. utilizar el Reference Project si es autodidacta.

El proyecto puede cambiar. Las competencias y milestones permanecen.

La filosofía es:

> El estudiante propone qué quiere construir. El mentor ayuda a convertirlo en un plan de desarrollo técnicamente exigente.

## Referencia vs proyecto real

El Reference Project permite que una persona sin cliente pueda completar el recorrido.

El proyecto real permite que el estudiante aprenda además:

- requisitos ambiguos;
- feedback;
- negociación de alcance;
- cambios;
- prioridades;
- trade-offs;
- responsabilidad sobre decisiones.

## Estructura del repositorio

```text
modern-software-development/
│
├── curriculum/
│   ├── competencies.md
│   ├── competency-matrix.md
│   ├── study-plan.md
│   └── assessment.md
│
├── theory/
│   └── README.md            # redirige a study-plan.md §6 hasta que tenga contenido propio
│
├── practice/
│   ├── s1/                  # 11 clases con contenido autorado (único semestre escrito)
│   │   ├── classes/
│   │   └── reference-project/
│   ├── s2/ … s6/            # estructura de plantilla, contenido pendiente de autoría
│   │   ├── classes/
│   │   └── reference-project/
│
└── project/
    ├── project-brief.md
    ├── project-milestones.md
    ├── project-model.md
    └── students/
        └── consultorio-odontologico/
            └── custom-plan.md
```

## Modelo de mentoría

La mentoría no consiste en impartir nuevamente las clases.

El mentor:

- revisa evidencia;
- cuestiona decisiones;
- detecta riesgos;
- ayuda a priorizar;
- propone investigación;
- exige justificación;
- define el siguiente objetivo.

El estudiante sigue siendo responsable de construir.

## Autodidacta vs mentoría

### Autodidacta

Puede seguir:

```text
clase
→ laboratorio
→ challenge
→ project task
→ evidencia
→ milestone
```

### Con mentor

Se añade:

```text
trabajo
→ mentoría
→ feedback
→ corrección
→ siguiente objetivo
```

La misma estructura sirve para ambos casos.

## ¿Te sirvió este material? (Colaboraciones)

Si estás siguiendo el plan de forma autodidacta y te ha aportado valor en tu carrera, el repositorio está abierto a colaboraciones. Puedes invitarme un café o apoyar el mantenimiento de este plan a través de:

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub-ea4aaa?style=flat-square&logo=github)](https://github.com/sponsors/fdomerlo)
[![Cafecito](https://img.shields.io/badge/Colaborar-Cafecito-FFDD00?style=flat-square&logo=cafecito)](https://cafecito.app/fdomerlo)
[![PayPal](https://img.shields.io/badge/Donar-PayPal-00457C?style=flat-square&logo=paypal)](https://paypal.me/fdomerlo)
[![Mercado Pago](https://img.shields.io/badge/Colaborar-Mercado%20Pago-009EE3?style=flat-square&logo=mercadopago)](https://link.mercadopago.com.ar/fdomerlo)

- **GitHub Sponsors:** Ideal para suscripciones mensuales o pagos únicos internacionales.
- **PayPal:** Para aportes directos en moneda extranjera (USD/EUR).
- **Mercado Pago / Cafecito:** Para colaboraciones y pagos directos en moneda local.

## Evaluación

No se evalúa principalmente:

- cantidad de código;
- cantidad de frameworks;
- velocidad;
- cantidad de features.

Se evalúa:

- comprensión;
- calidad;
- evidencia;
- decisiones;
- capacidad de debugging;
- reproducibilidad;
- comunicación;
- capacidad de evolución.

## IA

La IA se incorpora como herramienta de ingeniería, no como sustituto del aprendizaje.

El estudiante debe poder:

- formular problemas;
- evaluar respuestas;
- verificar código;
- detectar errores;
- justificar decisiones;
- reconocer cuándo no debe confiar en una salida.

La política de IA evoluciona con el nivel del estudiante. La política completa, escalada por semestre, está en [`curriculum/study-plan.md`](curriculum/study-plan.md) §3.

## Evolución del curriculum

Este repositorio debe tratarse como un sistema vivo.
Las modificaciones se realizan sobre evidencia.

## Objetivo final

> No enseñar a usar herramientas. Formar personas capaces de construir, operar y evolucionar sistemas de software.
