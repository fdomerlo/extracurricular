# Mapa de competencias diagnósticas

## Propósito

Este documento vincula el diagnóstico inicial con el catálogo oficial de competencias.

La fuente normativa de las competencias continúa siendo:

`curriculum/competencies.md`

Este archivo **no redefine competencias**.

Su función es determinar:

* cuáles son relevantes para el ingreso;
* cuáles son bloqueantes;
* qué nivel mínimo se espera;
* cómo pueden evaluarse;
* qué tipo de evidencia es apropiada.

---

## Categorías

Las competencias diagnósticas deben agruparse por capacidad, no por tecnología.

Categorías iniciales:

### Fundamentos de programación

Incluye competencias relacionadas con:

* variables;
* tipos;
* control de flujo;
* funciones;
* estructuras de datos;
* modularización;
* razonamiento algorítmico.

### Herramientas de desarrollo

Incluye:

* terminal;
* editor;
* sistema de archivos;
* Git;
* ejecución de programas;
* gestión básica del entorno.

### Resolución de problemas

Incluye:

* descomposición;
* identificación de errores;
* debugging;
* búsqueda de información;
* lectura de documentación.

### Ingeniería básica

Incluye:

* organización del código;
* separación de responsabilidades;
* pruebas;
* manejo de errores;
* documentación.

### Comunicación técnica

Incluye:

* explicar una solución;
* justificar decisiones;
* describir problemas;
* documentar procedimientos.

---

## Competencias bloqueantes

Una competencia es bloqueante cuando su ausencia impide razonablemente comenzar una actividad fundamental del primer tramo.

Una competencia no debe considerarse bloqueante solamente porque sea importante.

La clasificación debe justificarse por prerequisitos reales.

---

## Tabla de diagnóstico de entrada (S1)

Evaluación de prerrequisitos normativos contrastados contra `curriculum/competencies.md` para el ingreso al primer tramo curricular (S1):

| ID | Competencia | Nivel mínimo S1 | Bloqueante | Evidencia principal | Instrumento | Criterio de suficiencia de entrada |
|---|---|:---:|:---:|---|---|---|
| C01 | Resolver problemas mediante programación | L1 | **Sí** | Práctica (algorítmica / descomposición) | Practical Test (Task 2) | Descompone un problema simple en funciones y estructuras de datos funcionales. |
| C02 | Escribir Python idiomático | L1 | **No** | Práctica / Sintaxis | Practical Test (Task 2, 4) | Maneja sintaxis básica de Python (o lenguaje equivalente) para scripts simples. |
| C05 | Gestionar estados y errores | L1 | **No** | Conceptual / Diagnóstico | Questionnaire / Practical Test (Task 3) | Comprende el concepto de excepción y distingue flujo normal de situaciones de fallo. |
| C06 | Debugging sistemático | L1 | **Sí** | Diagnóstico y corrección | Practical Test (Task 3) | Interpreta un traceback de error, localiza la causa y formula hipótesis antes de editar. |
| C09 | Git profesional | L1 | **No** | Procedimental / Conceptual | Questionnaire / Practical Test (Task 1) | Conoce la noción de repositorio, commit y control de versiones local básico. |
| C12 | Documentación técnica | L1 | **No** | Lectura y comprensión | Questionnaire | Lee documentación técnica de una biblioteca o módulo sin depender de videotutoriales. |
| C13 | Tests unitarios | L1 | **No** | Conceptual / Verificación | Questionnaire / Practical Test (Task 4) | Comprende la noción de test automatizado y aserción de un resultado esperado. |
| C45 | Entornos reproducibles | L1 | **Sí** | Procedimental | Practical Test (Task 1) | Opera la terminal (navegación, rutas, ejecución de comandos y scripts de Python). |
| C66 | IA como tutor | L1 | **No** | Reflexión / Hábitos | Questionnaire | Emplea IA como herramienta de consulta o explicación sin adopción pasiva y ciega. |
| C71 | Verificación humana | L1 | **Sí** | Explicación y verificación | Practical Test (Task 5) / Questionnaire | Verifica y valida personalmente cualquier código propio o sugerido antes de aceptarlo. |
| C74 | Comunicación técnica | L1 | **Sí** | Explicación verbal / escrita | Practical Test (Task 5) / Questionnaire | Articula con claridad qué hace su código, por qué tomó una decisión y qué problemas encontró. |
| C76 | Aprendizaje autónomo | L1 | **Sí** | Resolución / Indagación | Questionnaire / Practical Test | Ante una traba técnica consulta documentación, investiga el error y no se detiene de inmediato. |
| C77 | Inglés técnico | L1 | **No** | Comprensión lectora | Questionnaire | Lee documentación técnica esencial y mensajes de error en inglés (incluso con asistencia). |

---

## Competencias indicadoras de Aceleración (Punto de entrada > S1)

Si el estudiante demuestra un nivel operativo alto o autónomo (L2/L3) en las siguientes competencias, se activa la evaluación de aceleración para saltear S1 y comenzar en semestres posteriores:

| ID | Competencia | Nivel observado para acelerar | Evidencia para salto curricular |
|---|---|:---:|---|
| C01 | Resolver problemas mediante programación | L2+ | Resuelve problemas complejos con arquitectura limpia, modular y eficiente. |
| C03 | Modelar dominios complejos | L2+ | Modela entidades, reglas de negocio y value objects sin acoplamiento a frameworks. |
| C04 | Diseñar software modular | L2+ | Separa responsabilidades en capas claras con abstracciones justificadas y cohesión alta. |
| C09 | Git profesional | L2+ | Manejo fluido de ramas, merge, rebasing y resolución de conflictos. |
| C10 | Branching / PRs / Issues | L2+ | Trabajo con flujos de Pull Requests, code review y descriptores claros. |
| C13 | Tests unitarios | L2+ | Diseña suites de tests con pytest usando fixtures y casos de borde sistemáticos. |
| C18 / C19 | Modelado relacional / SQL | L2+ | Diseña esquemas relacionales normalizados y escribe queries SQL puras sin ORM. |

---

## Regla de cobertura

No es necesario evaluar las 79 competencias para el ingreso.

El diagnóstico debe evaluar las competencias que funcionan como **prerequisitos del punto de entrada** y aquellas cuya ausencia pueda alterar significativamente la ruta recomendada.

Las restantes se evaluarán durante el currículo.

---

## Regla de progresión

Una competencia puede aparecer:

```text
diagnóstico
    ↓
S1
    ↓
S2
    ↓
S3
```

Esto no significa que el diagnóstico certifique su dominio final.

El diagnóstico solamente establece el estado inicial.
