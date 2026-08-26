# Class Catalog

Las 11 clases de S1, en orden. El frontmatter de `practice/s1/classes/` es la fuente de
verdad; esta tabla lo resume.

| ID | Clase | Competencias | Nivel | Duración | Prerrequisitos |
|---|---|---|---|---|---|
| S1-01 | Entorno de desarrollo | C45, C09 | L2 | 1 sesión (~2 h) | — |
| S1-02 | Python idiomático | C02 | L2 | 1 sesión (~2 h) | S1-01 |
| S1-03 | Manejo de errores — excepciones propias del dominio | C05, C02 | L2 | 1 sesión (~1.5 h) | S1-02 |
| S1-04 | Modelado de dominio — entidades y valores | C03, C04 | L2 | 1 sesión (~2 h) | S1-02, S1-03 |
| S1-05 | Reglas de negocio del consultorio | C03, C04, C05 | L3 | **2 sesiones** (~2 h c/u) | S1-03, S1-04 |
| S1-06 | Testing con pytest aplicado al dominio | C13 | L2 | 1 sesión (~2 h) | S1-05 |
| S1-07 | Git en profundidad — ramas y flujo de trabajo | C09, C10 | L3 | 1 sesión (~1.5 h) | S1-01 |
| S1-08 | Pensar como debugger | C06, C58 | L2 | 1 sesión (~1.5 h) | S1-06, S1-07 |
| S1-09 | Reproducir un bug | C06, C16 | L3 | 1 sesión (~1.5 h) | S1-06, S1-07, S1-08 |
| S1-10 | Pull Requests y revisión de código | C10, C11 | L2 | 1 sesión (~1.5 h) | S1-07, S1-09 |
| S1-11 | IA como tutor y verificador | C66, C68, C71 | L3 | 1 sesión (~1.5 h) | S1-01…S1-10 |

## Cobertura de competencias

Competencias desarrolladas en S1: **C02, C03, C04, C05, C06, C09, C10, C11, C13, C16, C45,
C58, C66, C68, C71**.

Notas de asignación, para que se puedan discutir:

- **S1-01** desarrolla C45 (entornos reproducibles), no C02: la clase es `uv`, lockfile y
  layout `src/`, no Python idiomático. C09 entra por el primer commit.
- **S1-03** desarrolla C05 ("gestionar estados y errores"), no C03: diseña una jerarquía de
  excepciones, que es diseño de código, no modelado del dominio.
- **S1-08** y **S1-09** desarrollan C06 ("debugging sistemático"). C05 no es debugging.
- **S1-11** no declara C67 ("IA como herramienta", L4): contradice la política restrictiva
  de S1–S2 que la propia clase enseña (`curriculum/study-plan.md` §3).
