# S1 — Trazabilidad curricular

Este documento establece la trazabilidad de S1 desde la competencia hasta la evidencia observable.

La unidad mínima es:

```text
competencia
    ↓
clase
    ↓
actividad
    ↓
project task
    ↓
evidencia
    ↓
evidence milestone
    ↓
competency gate (según matriz)
```

## 1. Criterio de lectura

Una competencia declarada en el frontmatter de una clase significa que la clase **trabaja explícitamente** esa competencia. No significa que el estudiante alcance allí el nivel final definido en `curriculum/competencies.md`.

Estados:

- **I** — introducción;
- **P** — práctica;
- **C** — consolidación;
- **D** — demostración evaluable.

Una misma competencia puede aparecer en varias clases. La primera aparición no tiene por qué ser su gate de evaluación.

### Separación conceptual: Milestone de evidencia vs. Competency Gate

- **Milestone de evidencia (`evidence.milestone`)**: Hito en el que el estudiante produce el artefacto verificable de la clase (para S1, todas las clases aportan evidencias al milestone de fin de semestre `M-S1`).
- **Competency Gate**: Hito curricular formal donde la competencia es auditada para certificación de dominio o promoción según `curriculum/competency-matrix.md`. Una clase de S1 produce evidencia evaluable para `M-S1` para competencias cuyo gate formal se ubica en semestres posteriores (ej. C45 en M-S4, C09 en M-S6, etc.).

## 2. S1 de un vistazo

| Clase | Tema | Competencias | Nivel de clase | Evidencia principal | Milestone de evidencia | Competency Gate(s) |
|---|---|---|---|---|---|---|
| S1-01 | Entorno de desarrollo | C45, C09 | L2 | entorno reproducible + historial Git | M-S1 | C45 (M-S4), C09 (M-S6) |
| S1-02 | Python idiomático | C02 | L2 | código tipado, dataclasses, convenciones | M-S1 | C02 (M-S1) |
| S1-03 | Excepciones de dominio | C05, C02 | L2 | jerarquía de errores + datos estructurados | M-S1 | C05 (M-S5), C02 (M-S1) |
| S1-04 | Entidades y valores | C03, C04 | L2 | modelo de dominio aislado | M-S1 | C03 (M-S6), C04 (M-S4) |
| S1-05 | Reglas de negocio | C03, C04, C05 | L3 | cinco reglas implementadas y verificadas | M-S1 | C03 (M-S6), C04 (M-S4), C05 (M-S5) |
| S1-06 | Testing con pytest | C13 | L2 | suite automatizada | M-S1 | C13 (M-S6) |
| S1-07 | Git, ramas y merge | C09, C10 | L3 | rama + conflicto + integración | M-S1 | C09 (M-S6), C10 (M-S3) |
| S1-08 | Debugging sistemático | C06, C58 | L2 | bug diagnosticado + proceso documentado | M-S1 | C06 (M-S5), C58 (M-S5) |
| S1-09 | Reproducir un bug | C06, C16 | L3 | test rojo → fix → verde + merge | M-S1 | C06 (M-S5), C16 (M-S4) |
| S1-10 | PR y code review | C10, C11 | L2 | PR revisable + issues + comentario de diseño | M-S1 | C10 (M-S3), C11 (M-S6) |
| S1-11 | IA como tutor/verificador | C66, C68, C71 | L3 | registro de uso/verificación + retrospectiva | M-S1 | C66 (M-S2), C68 (M-S5), C71 (M-S5) |

Las asignaciones anteriores se basan en el contenido real de las once clases y no solamente en los nombres de sus temas.

---

## 3. S1-01 — Entorno de desarrollo

**Competencias:** C45, C09
**Estado:** I/P
**Evidencia:** E-S1-01
**Milestone de evidencia:** M-S1
**Competency Gates:** C45 (M-S4), C09 (M-S6)

### Desarrollo

```text
C45 Entornos reproducibles
 ├── Demostración: uv + pyproject + uv.lock + src/
 ├── Laboratorio: reconstrucción del entorno
 ├── Ejercicio: borrar .venv + uv sync
 └── Project Task: proyecto real reproducible

C09 Git profesional
 ├── Demostración: git init
 ├── Laboratorio: commits atómicos
 ├── Ejercicio: segundo proyecto + dos commits
 └── Project Task: historial inicial del proyecto
```

La clase exige que otra persona pueda clonar y ejecutar el proyecto, que `uv.lock` esté versionado y que existan commits atómicos.

### Evidencia E-S1-01

- `pyproject.toml` correcto;
- `uv.lock` versionado;
- entorno reconstruible mediante `uv sync`;
- `.venv/` fuera del control de versiones;
- historial con al menos tres commits atómicos;
- reproducción por otra persona.

### Observación

C45 tiene una demostración fuerte pero su nivel L4 final no se pretende demostrar aquí. C09 se introduce en S1-01 y se consolida en S1-07/S1-10.

---

## 4. S1-02 — Python idiomático

**Competencia:** C02
**Estado:** I/P
**Evidencia:** E-S1-02
**Milestone de evidencia:** M-S1
**Competency Gates:** C02 (M-S1)

### Desarrollo

```text
C02 Python idiomático
 ├── Demostración: dataclasses
 ├── Laboratorio: refactor de clase existente
 ├── Ejercicio: HorarioAtencion
 ├── Challenge: kw_only
 └── Project Task: ruff + CONVENTIONS.md
```

La clase trabaja type hints, dataclasses, valores inmutables, comprehensions y argumentos mutables por defecto. La evidencia exige además que el código futuro mantenga esas convenciones y que `ruff` pase.

### Evidencia E-S1-02

- funciones nuevas tipadas;
- ausencia de argumentos mutables por defecto;
- ejemplo propio de comprehension;
- dataclass correctamente elegida;
- `ruff` sin errores;
- revisión de una dataclass por tutor.

### Observación

El nivel de la clase es L2. No debe interpretarse como demostración del L3 final de C02.

---

## 5. S1-03 — Excepciones propias del dominio

**Competencias:** C05, C02
**Estado:** C05 I/P; C02 P
**Evidencia:** E-S1-03
**Milestone de evidencia:** M-S1
**Competency Gates:** C05 (M-S5), C02 (M-S1)

### Desarrollo

```text
C05 Gestionar estados y errores
 ├── Demostración: HorarioInvalidoError
 ├── Laboratorio: PacienteNoEncontradoError
 ├── Ejercicio: TurnoSuperpuestoError
 ├── Challenge: raise ... from ...
 └── Project Task: exceptions.py

C02 Python idiomático
 └── aplicación secundaria: diseño de excepciones y type hints
```

La clase define una jerarquía `ConsultorioError`, excepciones específicas y datos estructurados en las excepciones. También distingue excepción de un resultado esperado como `None`.

### Evidencia E-S1-03

- `ConsultorioError` como base;
- excepciones específicas con datos relevantes;
- ausencia de `ValueError`/`Exception` genéricos para reglas de dominio;
- justificación de excepción vs. valor de retorno.

### Corrección aplicada

La asignación principal de esta clase es C05. C02 queda como competencia secundaria de implementación; no se debe utilizar esta clase como evidencia principal de dominio de C02.

---

## 6. S1-04 — Modelado de dominio

**Competencias:** C03, C04
**Estado:** I/P
**Evidencia:** E-S1-04
**Milestone de evidencia:** M-S1
**Competency Gates:** C03 (M-S6), C04 (M-S4)

### Desarrollo

```text
C03 Modelar dominios complejos
 ├── entidad vs. valor
 ├── identidad
 ├── composición
 └── Paciente / Profesional / Practica / Turno

C04 Diseñar software modular
 ├── separación del dominio
 ├── referencias entre objetos
 └── dominio sin persistencia/web
```

La clase exige distinguir entidades y valores y mantener el dominio independiente de base de datos, red e interfaz.

### Evidencia E-S1-04

- entidades con identidad propia;
- valores con igualdad por contenido;
- modelo `Paciente`, `Profesional`, `Practica`, `Turno`;
- dominio aislado de infraestructura;
- justificación oral de cada decisión.

### Observación

C03 y C04 tienen aquí una introducción importante, pero su demostración de nivel final queda en semestres posteriores.

---

## 7. S1-05 — Reglas de negocio del consultorio

**Competencias:** C03, C04, C05
**Estado:** C
**Evidencia:** E-S1-05
**Milestone de evidencia:** M-S1
**Competency Gates:** C03 (M-S6), C04 (M-S4), C05 (M-S5)

### Desarrollo

```text
C03
 └── convertir conocimiento del consultorio en reglas ejecutables

C04
 └── separar reglas por responsabilidad y evitar un método monolítico

C05
 └── estados y errores derivados de reglas de negocio
```

Las cinco reglas son: solapamiento, duración según práctica, cancelación tardía, sobreturnos y feriados. La clase exige verificarlas manualmente antes de automatizarlas en S1-06.

### Evidencia E-S1-05

- cinco reglas implementadas independientemente;
- caso positivo y negativo por regla;
- validación del experto de dominio;
- configuración de umbral de cancelación y feriados;
- capacidad de explicar cada regla.

### Observación crítica

Esta clase es el centro pedagógico de S1. Es la primera instancia donde las competencias de modelado dejan de ser ejercicios aislados y se convierten en comportamiento del sistema.

---

## 8. S1-06 — Testing con pytest

**Competencia:** C13
**Estado:** I/P
**Evidencia:** E-S1-06
**Milestone de evidencia:** M-S1
**Competency Gates:** C13 (M-S6)

### Desarrollo

```text
C13 Tests unitarios
 ├── estructura de tests
 ├── pytest.raises
 ├── fixtures
 ├── parametrize
 └── suite de las cinco reglas
```

La clase transforma las verificaciones manuales de S1-05 en una suite automatizada y exige casos límite, fixtures, parametrización y prueba explícita de excepciones.

### Evidencia E-S1-06

- al menos un test por cada regla;
- fixture reutilizada;
- test parametrizado;
- `pytest.raises`;
- suite en menos de cinco segundos;
- demostración de un fallo intencional y su corrección.

### Observación

C13 tiene nivel final L4, pero S1 solo introduce y practica el testing unitario. La demostración avanzada se reserva para S6.

---

## 9. S1-07 — Git en profundidad

**Competencias:** C09, C10
**Estado:** C
**Evidencia:** E-S1-07
**Milestone de evidencia:** M-S1
**Competency Gates:** C09 (M-S6), C10 (M-S3)

### Desarrollo

```text
C09 Git profesional
 ├── branches
 ├── merge
 ├── conflictos
 └── historial gráfico

C10 Branching / PRs / Issues
 ├── workflow de ramas
 └── base para PR de S1-10
```

La clase exige una rama integrada, un conflicto real resuelto por el estudiante y la documentación del workflow.

### Evidencia E-S1-07

- rama creada y mergeada;
- conflicto real resuelto;
- `git log --graph` mostrando integración;
- workflow documentado en `CONVENTIONS.md`;
- explicación de fast-forward vs. merge commit.

### Observación

C10 todavía no se demuestra como PR completo aquí; S1-10 es su evidencia principal.

---

## 10. S1-08 — Pensar como debugger

**Competencias:** C06, C58
**Estado:** C06 P; C58 P
**Evidencia:** E-S1-08
**Milestone de evidencia:** M-S1
**Competency Gates:** C06 (M-S5), C58 (M-S5)

### Desarrollo

```text
C06 Debugging sistemático
 ├── reproducir
 ├── aislar
 ├── hipótesis
 ├── probar
 ├── arreglar
 ├── verificar
 └── prevenir regresión

C58 Diagnóstico
 └── lectura de traceback + inspección del estado
```

La clase exige observar el proceso de diagnóstico, no solamente comprobar que el bug fue arreglado. `breakpoint()` y la suite completa forman parte de la práctica.

### Evidencia E-S1-08

- bug encontrado sin asistencia;
- uso de `breakpoint()`;
- hipótesis explícita;
- suite completa verde después del arreglo;
- proceso documentado en `CONVENTIONS.md`.

### Observación

C58 es una competencia transversal que continuará creciendo en S2–S5. Aquí se introduce el método.

---

## 11. S1-09 — Reproducir un bug

**Competencias:** C06, C16
**Estado:** C
**Evidencia:** E-S1-09
**Milestone de evidencia:** M-S1
**Competency Gates:** C06 (M-S5), C16 (M-S4)

### Desarrollo

```text
C06
 └── reproducir → minimizar → test rojo → fix → verde

C16
 └── convertir una regresión en evidencia automatizada
```

El punto central es que el test que reproduce el defecto debe fallar antes del arreglo y quedar registrado en el historial.

### Evidencia E-S1-09

- test rojo antes del fix;
- caso minimizado;
- arreglo posterior;
- suite completa verde;
- rama `fix/...` y merge;
- explicación de por qué el test demuestra que el bug era reproducible.

### Observación

Esta es la primera evidencia fuerte de C16, aunque su nivel final L4 se consolida en S4/S6.

---

## 12. S1-10 — Pull Requests y revisión de código

**Competencias:** C10, C11
**Estado:** C10 P; C11 P
**Evidencia:** E-S1-10
**Milestone de evidencia:** M-S1
**Competency Gates:** C10 (M-S3), C11 (M-S6)

### Desarrollo

```text
C10
 ├── PR como unidad de integración
 ├── issues
 └── workflow de cambios no triviales

C11
 ├── revisión sobre diff
 ├── preguntas de diseño
 └── comentarios accionables
```

La clase exige un PR real, revisión del propio diff, issues etiquetados y al menos un comentario sobre diseño.

### Evidencia E-S1-10

- PR mergeado;
- descripción con problema, solución y verificación;
- modificación posterior a la apertura;
- tres issues etiquetados;
- comentario de revisión sobre diseño;
- límite de tamaño de PR documentado.

### Observación

C11 se introduce aquí y se demuestra con práctica supervisada. El nivel L4 final requiere revisión sostenida de código ajeno en semestres posteriores.

---

## 13. S1-11 — IA como tutor y verificador

**Competencias:** C66, C68, C71
**Estado:** C66 C; C68 C; C71 C
**Evidencia:** E-S1-11
**Milestone de evidencia:** M-S1
**Competency Gates:** C66 (M-S2), C68 (M-S5), C71 (M-S5)

### Desarrollo

```text
C66 IA como tutor
 ├── preguntas
 ├── explicaciones
 └── investigación guiada

C68 Revisar código generado
 └── verificar una explicación/sugerencia contra código real

C71 Verificación humana
 ├── no confiar por plausibilidad
 ├── ejecutar
 ├── contrastar documentación
 └── comprobar comportamiento
```

La clase formaliza la política restrictiva de S1–S2 y exige un registro de cómo se utilizó y verificó IA.

### Evidencia E-S1-11

- caso propio de uso de IA;
- registro de pregunta y verificación;
- contraste con comportamiento real o documentación;
- media hora de trabajo sin asistencia;
- retrospectiva de semestre.

### Corrección importante

S1-11 **no desarrolla C67 — IA como herramienta**. La política de S1–S2 restringe la generación de soluciones y la clase está diseñada como tutor/verificador. C67 debe comenzar en S2, tal como establece la matriz curricular.

---

# 14. Evidencia acumulada de S1

Las evidencias de clase alimentan un único milestone:

```text
E-S1-01 ──┐
E-S1-02 ──┤
E-S1-03 ──┤
E-S1-04 ──┤
E-S1-05 ──┤
E-S1-06 ──┤
E-S1-07 ──┤──→ M-S1
E-S1-08 ──┤
E-S1-09 ──┤
E-S1-10 ──┤
E-S1-11 ──┘
```

El milestone S1 exige además Project Brief, código, tests, Git, reproducibilidad, bug report, una decisión técnica y defensa.

## 15. Cobertura de competencias en S1

### Trabajadas explícitamente por clases

| Competencia | Clases | Evidencia |
|---|---|---|
| C02 | S1-02, S1-03 | E-S1-02, E-S1-03 |
| C03 | S1-04, S1-05 | E-S1-04, E-S1-05 |
| C04 | S1-04, S1-05 | E-S1-04, E-S1-05 |
| C05 | S1-03, S1-05 | E-S1-03, E-S1-05 |
| C06 | S1-08, S1-09 | E-S1-08, E-S1-09 |
| C09 | S1-01, S1-07 | E-S1-01, E-S1-07 |
| C10 | S1-07, S1-10 | E-S1-07, E-S1-10 |
| C11 | S1-10 | E-S1-10 |
| C13 | S1-06 | E-S1-06 |
| C16 | S1-09 | E-S1-09 |
| C45 | S1-01 | E-S1-01 |
| C58 | S1-08 | E-S1-08 |
| C66 | S1-11 | E-S1-11 |
| C68 | S1-11 | E-S1-11 |
| C71 | S1-11 | E-S1-11 |

La lista coincide con el catálogo de S1 y se mantiene deliberadamente acotada.

### Competencias no trabajadas explícitamente en clases de S1

C01, C07, C08, C12, C14, C15, C17, C18–C44, C46–C57, C59–C65, C67, C69–C70, C72–C79.

Esto **no constituye un defecto por sí mismo**. Una competencia no tiene que aparecer en todos los semestres. Debe existir una ruta clara hacia su introducción y su gate posterior.

Sin embargo, estas competencias deben verificarse en la construcción de S2–S6 para garantizar que ninguna llegue a su gate sin haber tenido una práctica suficiente.

## 16. Auditoría S1

### Consistencias confirmadas

- Las 11 clases tienen competencias declaradas en frontmatter.
- El catálogo coincide con las 11 clases y sus competencias principales.
- C66/C68/C71 están correctamente asociadas a S1-11; C67 queda diferida a S2.
- C05 es la competencia principal de S1-03; C06 se concentra en S1-08/S1-09.
- La evidencia acumulada de S1 alimenta un único milestone M-S1.

### Pendientes estructurales

1. Incorporar `evidence` y `gate` al frontmatter de cada clase para que la trazabilidad sea legible por herramientas.
2. Definir IDs equivalentes para labs, challenges y project tasks cuando S2 empiece a construirse.
3. Convertir la tabla de cobertura en una validación automatizable.
4. Revisar que cada competencia que tenga gate en S2 tenga al menos una actividad de práctica previa.
5. Revisar especialmente C01, C12, C72, C74, C76 y C78: son competencias transversales que pueden quedar invisibles si se modelan solamente por clases técnicas.

## 17. Regla para S2–S6

No agregar una clase nueva solamente porque falta un tema.

Antes de crearla, completar:

```text
¿Qué competencia desarrolla?
        ↓
¿Qué nivel trabaja?
        ↓
¿Qué actividad permite practicarla?
        ↓
¿Qué Project Task la aplica?
        ↓
¿Qué evidencia produce?
        ↓
¿En qué milestone se demuestra?
```
