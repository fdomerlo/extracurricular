---
type: Directory Index
title: Evaluación y evidencia
---

# Evaluación y evidencia

La evaluación determina si una competencia fue realmente adquirida. No mide principalmente cantidad de código, cantidad de features o velocidad.

El principio central es:

> **No se declara una competencia alcanzada sin evidencia observable y defendible.**

## 1. Qué se evalúa

El curriculum trabaja con 79 competencias (`C01–C79`). Cada una tiene un nivel final esperado en [`competencies.md`](competencies.md).

Los niveles son:

| Nivel | Significado |
|---|---|
| L1 | Comprende y puede explicar el concepto |
| L2 | Lo aplica siguiendo una guía |
| L3 | Lo utiliza con autonomía |
| L4 | Diseña soluciones y justifica decisiones |

El nivel final es el objetivo de egreso; el estudiante no necesariamente debe alcanzar ese nivel en el primer semestre en que aparece una competencia.

## 2. Dos capas de evaluación

La evaluación combina dos mecanismos distintos.

### 2.1. Competency Gates

Cada milestone contiene competencias que deben demostrarse explícitamente.

Una competencia gateada no puede considerarse alcanzada simplemente porque el proyecto obtuvo una buena puntuación global.

Ejemplo:

```text
M-S4
│
├── C04 Diseño modular        ✓
├── C07 Refactoring           ✓
├── C23 Concurrencia          ✗
├── C42 Trade-offs            ✓
└── C43 ADRs                  ✓

Resultado: milestone incompleto
Motivo: C23 requiere remediación
```

### 2.2. Calidad global del proyecto

Además de los gates, se evalúa la calidad de la entrega completa:

| Dimensión | Peso orientativo |
|---|---:|
| Correctitud | 25% |
| Diseño y mantenibilidad | 20% |
| Testing y calidad | 15% |
| Legibilidad | 10% |
| Diagnóstico y robustez | 15% |
| Comunicación y documentación | 15% |

Estos pesos son orientativos y pueden adaptarse al semestre. **La rúbrica global nunca compensa el incumplimiento de un competency gate obligatorio.**

## 3. Evidencia

Una evidencia es un artefacto o actuación que permite observar una competencia.

Ejemplos:

- código del proyecto;
- tests;
- laboratorio;
- challenge;
- Pull Request;
- code review;
- ADR;
- benchmark;
- documentación;
- deployment;
- diagnóstico de incidente;
- investigación técnica;
- defensa oral.

La evidencia debe ser suficientemente concreta para que otra persona pueda revisarla sin depender exclusivamente de la palabra del estudiante.

## 4. Trazabilidad

La relación entre curriculum y evaluación es:

```text
competencia
    ↓
semestre
    ↓
clase / lab / challenge
    ↓
project task
    ↓
evidencia
    ↓
competency gate
    ↓
milestone
```

La matriz completa está en [`competency-matrix.md`](competency-matrix.md).

Reglas:

1. Todo contenido práctico nuevo declara las competencias que desarrolla.
2. Toda evidencia de evaluación declara las competencias que demuestra.
3. Todo milestone declara los competency gates que contiene.
4. Una competencia no debe aparecer como evaluada si no existe una evidencia identificable.

## 5. Milestones

Cada semestre termina con una instancia de integración.

El milestone no es simplemente "entregar el proyecto". El estudiante debe demostrar que puede:

- explicar qué construyó;
- justificar decisiones;
- mostrar evidencia;
- diagnosticar problemas relevantes;
- reconocer limitaciones;
- responder preguntas sobre el sistema.

La defensa puede ser escrita, práctica, oral o una combinación según el semestre.

## 6. Estados de competencia

Para evitar confundir "aprobó una actividad" con "domina una competencia", cada competencia puede registrar uno de estos estados:

| Estado | Significado |
|---|---|
| `introduced` | fue presentada |
| `practiced` | fue ejercitada |
| `consolidated` | se utiliza con autonomía |
| `demonstrated` | cumplió la evidencia del gate |
| `remediation` | la evidencia fue insuficiente y requiere trabajo adicional |

El estado `demonstrated` requiere cumplir el nivel definido por el gate correspondiente.

## 7. Remediación

No aprobar un gate no implica repetir automáticamente todo el semestre.

La remediación debe identificar:

1. competencia pendiente;
2. evidencia insuficiente;
3. causa probable;
4. actividad correctiva;
5. nueva evidencia;
6. fecha de revisión.

```text
fallo de gate
    ↓
diagnóstico
    ↓
actividad de remediación
    ↓
nueva evidencia
    ↓
revisión
```

El objetivo es cerrar una brecha concreta, no penalizar el error.

## 8. Defensa técnica

Una defensa sirve para comprobar que el estudiante comprende lo que presenta.

Puede incluir preguntas como:

- ¿Por qué elegiste esta solución?
- ¿Qué alternativas consideraste?
- ¿Qué pasa si falla esta dependencia?
- ¿Cómo verificarías este comportamiento?
- ¿Dónde está el límite de esta arquitectura?
- ¿Qué cambiarías si la carga se multiplicara?
- ¿Qué parte fue asistida por IA?
- ¿Cómo verificaste el código generado?

La defensa no busca memoria literal. Busca razonamiento y capacidad de explicar decisiones.

## 9. IA y evaluación

La política de uso de IA se define exclusivamente en [`study-plan.md`](study-plan.md).

Este documento no establece permisos adicionales por semestre. Evalúa la capacidad de trabajar responsablemente con IA cuando su uso está permitido.

En particular, el estudiante debe poder:

- identificar qué partes fueron asistidas;
- revisar el resultado;
- verificar comportamiento;
- detectar errores o supuestos incorrectos;
- modificar la solución;
- defender la decisión de incorporarla.

La competencia **C71 — Verificación humana** y las competencias relacionadas con IA requieren evidencia explícita de este proceso.

## 10. Criterio de aprobación de un milestone

Un milestone se considera **demostrado** cuando:

1. todos los competency gates obligatorios alcanzaron el nivel requerido;
2. la entrega supera el umbral mínimo de calidad definido para el semestre;
3. la evidencia es revisable;
4. el estudiante puede explicar y defender las decisiones relevantes.

La puntuación global es información diagnóstica. Los gates son condiciones de dominio.

## 11. Egreso

El objetivo de S6 no es obtener una puntuación final aislada.

El estudiante debe poder demostrar, mediante el conjunto de evidencias acumuladas, que puede:

- resolver problemas de software;
- diseñar sistemas;
- trabajar con código propio y ajeno;
- probar y diagnosticar;
- desplegar y operar;
- evaluar trade-offs;
- investigar alternativas;
- utilizar IA con verificación;
- comunicar decisiones técnicas;
- evolucionar un sistema existente;
- trabajar con autonomía.

La evidencia final se reúne en el portfolio y en la defensa técnica del proyecto.

## 12. Fuentes de verdad

- [`competencies.md`](competencies.md) — nombres, IDs y niveles finales.
- [`study-plan.md`](study-plan.md) — progresión temporal y política de IA.
- [`competency-matrix.md`](competency-matrix.md) — trazabilidad por competencia.
- [`project/project-milestones.md`](../project/project-milestones.md) — integración del proyecto.

Si estos documentos entran en contradicción, la inconsistencia debe resolverse antes de considerar estable el material afectado.
