# Extracurricular — Documento Fundacional

> **Documento de contexto permanente para humanos, LLMs y agentes de desarrollo.**

**Proyecto:** Extracurricular
**Repositorio:** `fdomerlo/extracurricular`
**Estado:** en construcción incremental
**Propósito:** construir un curriculum abierto de desarrollo moderno de software, centrado en competencias profesionales, evidencia observable y práctica sostenida.

---

# 1. Qué es este proyecto

Extracurricular es un programa educativo de aproximadamente tres años, organizado en seis semestres, cuyo objetivo es desarrollar capacidades profesionales de ingeniería de software.

No pretende enseñar una colección de lenguajes, frameworks o herramientas.

Su objetivo es formar personas capaces de:

```text
entender problemas
      ↓
modelar
      ↓
diseñar
      ↓
implementar
      ↓
probar
      ↓
entregar
      ↓
operar
      ↓
diagnosticar
      ↓
evolucionar
      ↓
defender decisiones
```

La tecnología es el medio.

La competencia profesional es el objetivo.

---

# 2. Por qué existe

La formación académica tradicional puede proporcionar fundamentos importantes, pero existe una brecha entre:

* conocer conceptos;
* aprobar materias;
* construir software;
* trabajar con sistemas reales;
* operar software;
* tomar decisiones técnicas;
* convivir con deuda técnica;
* diagnosticar fallos;
* comunicar decisiones;
* trabajar con herramientas modernas;
* utilizar IA sin delegar el razonamiento.

Extracurricular intenta cubrir esa brecha mediante práctica longitudinal.

No busca reemplazar una carrera universitaria.

Busca complementarla.

También puede utilizarse independientemente por autodidactas o desarrolladores que necesiten estructurar su formación.

---

# 3. Objetivo principal

El objetivo final del programa es que una persona pueda pasar de:

> "sé programar"

a:

> "puedo hacerme responsable de un sistema de software".

Esto implica desarrollar progresivamente la capacidad de:

* comprender un problema;
* modelar un dominio;
* elegir soluciones;
* implementar software;
* escribir y mantener tests;
* trabajar con Git;
* utilizar bases de datos;
* diseñar APIs;
* aplicar seguridad;
* desplegar software;
* automatizar delivery;
* diseñar sistemas;
* operar servicios;
* observar sistemas;
* diagnosticar problemas;
* recuperarse de fallos;
* gestionar deuda técnica;
* investigar tecnologías;
* trabajar con IA;
* comunicar decisiones;
* defender técnicamente una solución.

---

# 4. Principios fundacionales

## 4.1 Competencias antes que tecnologías

El curriculum no debe quedar atado a una tecnología concreta.

Por ejemplo:

```text
HTTP
```

es una capacidad/conocimiento fundamental.

Un framework web concreto es una implementación posible.

Por lo tanto:

```text
competencia
    ↓
fundamento
    ↓
tecnología de referencia
    ↓
práctica
```

y no:

```text
framework
    ↓
todo lo demás
```

Las tecnologías pueden cambiar.

Las competencias deben permanecer estables.

---

## 4.2 Fundamento antes que abstracción

El estudiante debe comprender qué problema resuelve una abstracción antes de depender de ella.

Ejemplos:

```text
SQL → ORM
HTTP → framework web
procesos → workers
redes → plataformas
contenedores → orquestación
Git → plataformas Git
observabilidad → herramientas específicas
```

No significa evitar abstracciones.

Significa comprender qué están abstrayendo.

---

## 4.3 Un proyecto longitudinal

El programa utiliza un proyecto como vehículo principal de aprendizaje.

El proyecto evoluciona durante los seis semestres.

Conceptualmente:

```text
S1
dominio + fundamentos
       ↓
S2
persistencia + servicios
       ↓
S3
aplicación + delivery
       ↓
S4
arquitectura + sistemas
       ↓
S5
producción + operación
       ↓
S6
observabilidad + evolución + liderazgo
```

Esto introduce una característica deliberada:

**las decisiones anteriores permanecen.**

El estudiante debe convivir con:

* deuda técnica;
* decisiones imperfectas;
* cambios de requisitos;
* refactors;
* migraciones;
* fallos;
* cambios de arquitectura;
* necesidades nuevas.

Esto es parte del aprendizaje.

---

# 5. Dos proyectos conceptuales

Existen dos posibilidades:

## Reference Project

Proyecto mantenido por el curriculum.

Sirve para:

* demostrar las actividades;
* proporcionar un contexto común;
* permitir estudiar sin disponer de proyecto propio;
* facilitar ejemplos;
* validar las prácticas.

## Student Project

Proyecto propio del estudiante.

Puede ser:

* personal;
* académico;
* profesional;
* open source;
* de un cliente real;
* definido junto con el tutor.

Ambos deben seguir el mismo modelo de competencias.

El contexto puede cambiar.

La exigencia formativa no.

---

# 6. El curriculum no es solamente contenido

El curriculum está compuesto por varias capas.

```text
COMPETENCIAS
     ↓
PLAN DE ESTUDIOS
     ↓
MATRIZ DE COMPETENCIAS
     ↓
CLASES
     ↓
ACTIVIDADES
     ↓
CHALLENGES
     ↓
PROJECT TASKS
     ↓
EVIDENCIAS
     ↓
COMPETENCY GATES
     ↓
MILESTONES
     ↓
DEFENSA
```

Cada capa responde una pregunta diferente.

### Competencias

¿Qué debe ser capaz de hacer el estudiante?

### Plan

¿En qué momento se trabaja cada capacidad?

### Matriz

¿Cómo progresa cada competencia a través del programa?

### Clase

¿Qué se enseña/practica concretamente?

### Actividad

¿Qué hace el estudiante?

### Challenge

¿Puede resolver un problema con menor asistencia?

### Project Task

¿Cómo aplica la competencia al proyecto?

### Evidencia

¿Qué artefacto observable demuestra trabajo?

### Competency Gate

¿En qué momento se considera que la competencia alcanzó el nivel requerido?

### Milestone

¿Qué conjunto de resultados debe estar terminado al finalizar una etapa?

### Defensa

¿Puede el estudiante explicar y justificar lo que construyó?

---

# 7. Evidencia antes que acumulación

Completar contenido no equivale a aprender.

Leer un libro no demuestra dominio.

Completar una clase tampoco.

Escribir mucho código tampoco.

La unidad fundamental de evaluación es la evidencia observable.

Ejemplos:

* código funcional;
* tests;
* commits;
* Pull Requests;
* documentación;
* diagramas;
* decisiones arquitectónicas;
* benchmarks;
* debugging;
* deployment;
* logs;
* métricas;
* incidentes;
* backups/restores;
* postmortems;
* contribuciones externas;
* defensa técnica.

La pregunta fundamental es:

> ¿Qué podría observar un tercero para determinar si el estudiante realmente puede hacer esto?

---

# 8. Milestone y competency gate

Estos conceptos deben mantenerse separados.

Una evidencia puede contribuir a un milestone temprano aunque la competencia asociada no alcance su nivel final hasta mucho después.

Por ejemplo:

```text
S1
    ↓
introducción/práctica de C66
    ↓
evidencia E-S1-X
    ↓
contribuye a M-S1

pero

C66
    ↓
competency gate
    ↓
M-S2
```

Por lo tanto:

**evidence milestone != competency gate**

salvo cuando explícitamente coincidan.

Esta distinción es estructural y debe conservarse en los documentos, frontmatter, herramientas y validaciones.

---

# 9. Niveles de dominio

El programa utiliza cuatro niveles:

| Nivel | Significado                |
| ----- | -------------------------- |
| L1    | comprende y puede explicar |
| L2    | aplica siguiendo una guía  |
| L3    | aplica con autonomía       |
| L4    | diseña, decide y defiende  |

El `nivel` de una clase representa el nivel esperado **en esa clase**.

No significa necesariamente que la competencia haya alcanzado su nivel final.

---

# 10. Roles de competencia dentro de una clase

Una clase puede:

* introducir una competencia;
* practicarla;
* consolidarla;
* demostrarla.

Por ello los roles son:

```text
introducción
práctica
consolidación
demostración
```

El rol evita interpretar cualquier mención de una competencia como evidencia de dominio.

Una clase pertenece a una competencia cuando existe una actividad intencional que permite trabajarla.

---

# 11. Progresión curricular

El programa está organizado en seis semestres.

| Semestre | Propósito             |
| -------- | --------------------- |
| S1       | Construir             |
| S2       | Persistir y servir    |
| S3       | Entregar software     |
| S4       | Diseñar sistemas      |
| S5       | Operar en producción  |
| S6       | Evolucionar y liderar |

La progresión conceptual es:

```text
S1 → software correcto
S2 → software persistente
S3 → software entregable
S4 → sistema diseñado
S5 → servicio operable
S6 → sistema evolucionable
```

La complejidad aumenta por necesidad.

No por acumulación arbitraria de tecnologías.

---

# 12. S1 es el patrón de referencia

El primer semestre es actualmente la implementación curricular más avanzada.

Por ello S1 debe considerarse el patrón para desarrollar los siguientes semestres.

Antes de producir grandes cantidades de contenido para S2–S6 se debe validar:

* estructura de clases;
* frontmatter;
* trazabilidad;
* modelo de evidencia;
* relación con Project Tasks;
* relación con milestones;
* evaluación;
* experiencia del estudiante;
* linting;
* documentación;
* flujo de trabajo.

El objetivo no es tener seis semestres incompletos.

El objetivo es tener una primera unidad sólida que pueda replicarse.

---

# 13. Política de IA

La IA es una herramienta profesional y forma parte del curriculum.

El programa no intenta prohibirla indefinidamente.

La enseñanza busca desarrollar:

* formulación de problemas;
* evaluación de respuestas;
* verificación;
* debugging;
* comparación de alternativas;
* revisión de código;
* detección de errores;
* comprensión de limitaciones;
* responsabilidad técnica.

La autonomía aumenta progresivamente.

### S1–S2

IA principalmente como:

* tutor;
* explicador;
* asistente de diagnóstico;
* ayuda para documentación;
* apoyo controlado.

### S3–S4

Se puede delegar más trabajo mecánico:

* boilerplate;
* refactors repetitivos;
* tests derivados;
* documentación;
* tareas acotadas.

Siempre con revisión humana.

### S5–S6

Se permite un flujo profesional de IA/agentes:

* investigación;
* diseño asistido;
* implementación;
* debugging;
* documentación;
* automatización;
* agentes de desarrollo.

La responsabilidad sigue siendo del estudiante.

Regla transversal:

> Todo código incorporado al proyecto debe poder ser explicado, modificado, verificado y defendido por el estudiante.

---

# 14. Tutoría

La tutoría es un servicio complementario.

No debe existir contenido educativo secreto cuya única finalidad sea obligar a pagar.

El material curricular puede permanecer abierto.

La tutoría aporta:

* seguimiento;
* feedback;
* code review;
* discusión técnica;
* debugging;
* revisión arquitectónica;
* seguimiento de competencias;
* preparación de milestones;
* preparación de defensas;
* acompañamiento sobre el proyecto real.

El tutor no debe convertirse en implementador.

El estudiante conserva la responsabilidad sobre:

* decisiones;
* implementación;
* investigación;
* verificación;
* defensa.

El objetivo de la tutoría es aumentar la autonomía, no crear dependencia.

---

# 15. Evaluación

La evaluación se centra en evidencia.

No se evalúa principalmente:

* cantidad de código;
* cantidad de frameworks;
* velocidad;
* cantidad de features;
* cantidad de horas conectadas.

Se evalúa:

```text
comprensión
+
implementación
+
verificación
+
razonamiento
+
diagnóstico
+
comunicación
+
defensa
```

Una solución técnicamente correcta pero que el estudiante no puede explicar no constituye evidencia suficiente de autonomía.

---

# 16. Modelo de aprendizaje

El flujo pedagógico general es:

```text
concepto
   ↓
ejemplo
   ↓
práctica guiada
   ↓
ejercicio
   ↓
challenge
   ↓
aplicación al proyecto
   ↓
evidencia
   ↓
feedback
   ↓
corrección
   ↓
milestone
   ↓
defensa
```

La repetición deliberada y la evolución del proyecto son características deseadas.

---

# 17. Arquitectura documental

El repositorio contiene diferentes tipos de documentos.

## `curriculum/`

Define el contrato educativo.

Incluye:

* competencias;
* plan;
* matriz;
* evaluación;
* esquema de clases.

## `practice/`

Contiene la implementación práctica del curriculum.

## `project/`

Define el proyecto longitudinal y sus milestones.

## `theory/`

Contiene bibliografía y material teórico.

## `docs/`

Contiene documentación operacional y pedagógica:

* cómo empezar;
* tutoría;
* roadmap;
* FAQ;
* journey;
* diagnóstico;
* etc.

## `tools/`

Contiene automatizaciones que validan o transforman la estructura curricular.

---

# 18. El curriculum como sistema declarativo

Una dirección futura importante es tratar el curriculum como datos estructurados.

Conceptualmente:

```text
competencies
      ↓
classes
      ↓
activities
      ↓
evidence
      ↓
gates
      ↓
milestones
```

Esto permite eventualmente generar:

* mapas de competencias;
* progreso del estudiante;
* checklists de tutoría;
* informes;
* planes personalizados;
* dashboards;
* portfolios;
* validaciones;
* documentación.

Por eso el frontmatter no es decoración.

Es metadata curricular.

El objetivo futuro es que las herramientas puedan comportarse como un pequeño "compilador curricular".

---

# 19. Reglas para agentes y LLMs

Cualquier agente que trabaje en este repositorio debe asumir:

### Regla 1

No modificar la filosofía del curriculum sin justificarlo.

### Regla 2

No agregar tecnologías simplemente porque sean populares.

### Regla 3

No duplicar competencias.

### Regla 4

No agregar una competencia a una clase solamente porque se menciona.

### Regla 5

Toda competencia declarada debe tener una actividad intencional.

### Regla 6

Toda evidencia debe ser observable.

### Regla 7

No confundir evidencia, milestone y competency gate.

### Regla 8

No tratar el frontmatter como texto informal.

### Regla 9

Las herramientas de validación deben validar el contrato documental real.

### Regla 10

No modificar grandes cantidades de contenido educativo cuando el problema puede resolverse modificando el esquema o la herramienta.

### Regla 11

Preferir cambios pequeños, verificables y reversibles.

### Regla 12

No inventar contenido futuro para aparentar que el curriculum está terminado.

### Regla 13

S1 es el patrón de referencia actual.

### Regla 14

Antes de extender el sistema, verificar que el modelo existente sea consistente.

---

# 20. Estado actual

El proyecto se encuentra en una etapa de construcción y estabilización.

Actualmente existen:

* marco curricular;
* 79 competencias;
* plan de seis semestres;
* matriz de competencias;
* modelo de evaluación;
* modelo de proyecto;
* modelo de tutoría;
* estructura práctica;
* implementación significativa de S1;
* trazabilidad de S1;
* esquema de metadata de clases;
* herramientas de lint/migración;
* workflows de validación.

S1 es la referencia más completa.

S2 está en desarrollo.

S3–S6 están definidos conceptualmente y deben desarrollarse progresivamente.

---

# 21. Prioridades actuales

El orden correcto de trabajo es:

## P0 — Consistencia

Resolver:

1. contrato de frontmatter;
2. parser YAML;
3. evidencia vs milestone vs competency gate;
4. linter;
5. migración;
6. CI;
7. trazabilidad S1.

## P1 — Experiencia

Agregar:

* diagnóstico;
* student journey;
* onboarding;
* portfolio/outcomes;
* documentación de contribución.

## P2 — Validación

Probar S1 con estudiantes reales.

Medir:

* tiempo real;
* dificultades;
* abandono;
* comprensión;
* calidad de evidencias;
* carga de trabajo;
* utilidad de tutoría.

## P3 — Escalamiento

Después de validar S1:

```text
S1 validado
    ↓
S2
    ↓
S3
    ↓
S4
    ↓
S5
    ↓
S6
```

No construir todo simultáneamente.

---

# 22. Qué significa "terminado"

Una parte del curriculum no está terminada porque exista un archivo Markdown.

Una unidad curricular está terminada cuando:

* el objetivo está definido;
* las competencias están identificadas;
* las actividades son coherentes;
* la práctica existe;
* el challenge existe cuando corresponde;
* el Project Task existe;
* existe evidencia observable;
* la trazabilidad es verificable;
* la evaluación es coherente;
* el material fue revisado;
* los enlaces funcionan;
* el lint pasa;
* y, cuando sea posible, fue probado con estudiantes.

La validación real es pedagógica y técnica.

---

# 23. Filosofía de desarrollo del propio repositorio

El repositorio de Extracurricular también debe ser tratado como un proyecto de software.

Por lo tanto debe aplicar:

* control de versiones;
* cambios pequeños;
* documentación;
* automatización;
* validación;
* CI;
* revisión;
* trazabilidad;
* decisiones explícitas.

El curriculum enseña ingeniería de software y, al mismo tiempo, su propio repositorio debe demostrar buenas prácticas de ingeniería.

---

# 24. Principio de estabilidad

Cuando exista tensión entre:

* agregar contenido;
* agregar tecnología;
* mejorar la estructura;
* mejorar la trazabilidad;
* mejorar la validación;
* probar con estudiantes;

se debe priorizar la capacidad de demostrar que el curriculum funciona.

La prioridad no es volumen.

La prioridad es calidad, coherencia y reproducibilidad.

---

# 25. Visión a largo plazo

Extracurricular puede evolucionar desde un repositorio educativo hacia un sistema curricular declarativo.

La visión es:

```text
curriculum declarativo
        ↓
contenido
        ↓
práctica
        ↓
evidencia
        ↓
evaluación
        ↓
progreso
        ↓
portfolio
        ↓
tutoría
```

El mismo modelo puede servir para:

* autodidactas;
* estudiantes;
* tutores;
* docentes;
* proyectos personales;
* formación profesional.

La tecnología puede cambiar.

El modelo pedagógico debe permanecer reconocible.

---

# 26. Principio final

El propósito de Extracurricular no es producir personas que sepan utilizar muchas herramientas.

Es producir personas capaces de hacerse responsables de software.

> **No formar usuarios de herramientas. Formar personas capaces de construir, probar, entregar, operar, diagnosticar y evolucionar software, y de defender técnicamente sus decisiones.**
