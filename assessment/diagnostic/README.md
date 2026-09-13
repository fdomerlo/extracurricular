# Diagnóstico inicial

## Propósito

El diagnóstico inicial determina el **punto de partida curricular de un estudiante** antes de comenzar el proyecto longitudinal.

No es un examen de admisión ni una evaluación destinada a excluir estudiantes.

Su finalidad es responder:

> **¿Dónde está el estudiante actualmente y desde dónde debería continuar?**

El diagnóstico puede producir tres resultados principales:

1. **Nivelación** — el estudiante necesita desarrollar competencias previas antes de comenzar determinadas actividades del currículo.
2. **Ingreso curricular** — el estudiante posee las competencias necesarias para comenzar desde el punto recomendado.
3. **Aceleración** — el estudiante posee formación previa suficiente para evitar contenidos ya dominados y avanzar hacia competencias posteriores.

---

## Principios

### 1. Diagnosticar antes de enseñar

No asumir que todos los estudiantes comienzan desde el mismo punto.

### 2. Medir competencias, no solamente conocimientos

El diagnóstico debe observar tanto:

* conocimiento conceptual;
* capacidad procedimental;
* resolución de problemas;
* diagnóstico de errores;
* razonamiento;
* comunicación técnica;
* autonomía.

### 3. El conocimiento declarado no es suficiente

Que un estudiante indique que conoce una tecnología o concepto no constituye evidencia suficiente.

Siempre que sea posible, el diagnóstico debe solicitar una demostración observable.

### 4. No penalizar formación previa

Un estudiante avanzado no debe repetir contenidos simplemente porque el currículo tiene una secuencia fija.

El diagnóstico puede recomendar avanzar directamente hacia competencias que ya domina.

### 5. Las brechas son accionables

Una competencia insuficiente no debe producir solamente un resultado negativo.

Debe poder convertirse en:

```text
competencia
    ↓
brecha
    ↓
recurso / actividad de nivelación
    ↓
evidencia
    ↓
reevaluación
```

### 6. El diagnóstico no certifica definitivamente una competencia

El resultado indica el **nivel inicial estimado**.

La demostración curricular posterior sigue dependiendo de las evidencias y competency gates definidos por el programa.

---

## Modelo

El diagnóstico utiliza las competencias existentes en:

`curriculum/competencies.md`

y sus niveles:

```text
L1 — inicial
L2 — operativo
L3 — autónomo
L4 — avanzado
```

El resultado se expresa por competencia:

```text
CXX
nivel observado: L2
nivel requerido para inicio: L2
estado: READY
evidencia: práctica + explicación
```

---

## Resultados posibles

### READY

El estudiante posee las competencias mínimas necesarias para comenzar el tramo recomendado.

### CONDITIONAL

El estudiante puede comenzar, pero tiene brechas secundarias que deberán ser atendidas durante el recorrido.

### REMEDIATION

Existen brechas en competencias que bloquean determinadas actividades o el comienzo efectivo del proyecto.

### ACCELERATED

El estudiante demuestra competencias superiores a las requeridas para el inicio estándar.

Puede comenzar desde un punto curricular posterior, sujeto a validación mediante las primeras evidencias del recorrido.

---

## Flujo

```text
1. Cuestionario inicial
        ↓
2. Evaluación conceptual
        ↓
3. Evaluación práctica
        ↓
4. Evaluación de diagnóstico y explicación
        ↓
5. Perfil de competencias
        ↓
6. Identificación de brechas
        ↓
7. Determinación del punto de entrada
        ↓
8. Plan de nivelación o aceleración
        ↓
9. Readiness Gate
        ↓
10. Inicio curricular
```

---

## Principio de aceleración

La aceleración no consiste simplemente en "saltear clases".

El estudiante puede evitar actividades introductorias cuando exista evidencia suficiente de competencia.

Sin embargo, las competencias que poseen un competency gate posterior deben continuar siendo evaluadas cuando corresponda.

Por lo tanto:

```text
diagnóstico inicial
        ≠
competency gate curricular
```

---

## Principio de nivelación

La nivelación tampoco constituye un segundo currículo completo.

Debe ser la ruta mínima necesaria para cerrar las brechas que impiden avanzar.

La nivelación debe priorizar:

1. competencias bloqueantes;
2. prerequisitos;
3. fundamentos;
4. autonomía mínima;
5. capacidad de producir evidencia.

---

## Relación con el proyecto

El estudiante no debería comenzar el proyecto longitudinal simplemente porque completó el diagnóstico.

Debe alcanzar las condiciones mínimas operativas (nivel L2 en competencias bloqueantes como programación básica, terminal y razonamiento de errores) definidas en [`competency-map.md`](competency-map.md).

El proyecto comienza cuando existe evidencia suficiente de que el estudiante puede trabajar sobre él sin que las brechas fundamentales hagan imposible el aprendizaje curricular.

---

## Artefactos producidos

Un diagnóstico completo produce:

```text
diagnostic-result
    ├── competency profile
    ├── evidence summary
    ├── identified gaps
    ├── recommended entry point
    ├── remediation plan
    ├── acceleration recommendations
    └── readiness status
```

Estos artefactos permiten al estudiante conocer su punto de partida técnico o ser evaluados en caso de contar con tutoría.

---

## Regla de actualización

El sistema de diagnóstico evoluciona junto con el currículo.

Si se modifican:

* competencias;
* niveles;
* prerequisitos;
* estructura curricular;
* requisitos de entrada;

también el diagnóstico.

---

## Documentos del módulo

- [`initial-evaluation.md`](initial-evaluation.md): **Instrumento principal para el estudiante** que integra el cuestionario cualitativo y la prueba práctica.
- [`competency-map.md`](competency-map.md): Mapeo normativo a `curriculum/competencies.md`, competencias bloqueantes y criterios de suficiencia de entrada.
- [`practical-test.md`](practical-test.md): Especificación de las 5 tareas de la prueba práctica.
- [`questionarie.md`](questionarie.md): Especificación del cuestionario conceptual y de hábitos de trabajo.

*(Nota: Las rúbricas analíticas de corrección y criterios de decisión de Readiness Gate forman parte del marco de evaluación docente para el proceso de admisión).*
