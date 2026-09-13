---
type: Directory Index
title: Plan de formación — Marco general
description: Plan de estudios centrado en competencias, con una implementación tecnológica de referencia.
---

# Plan de formación en desarrollo de software

- **Duración de referencia:** 6 semestres (~36 meses en ritmo part-time; acelerable a 12–24 meses según dedicación y experiencia previa)
- **Estructura:** aproximadamente 22 semanas académicas por semestre de referencia (el avance real está determinado por la acreditación de hitos)
- **Carga estimada:** ~1.495 horas totales de ingeniería
- **Dedicación de referencia:** ~10–12 h/semana durante las semanas activas, con variaciones según el semestre y el proyecto
- **Proyecto eje:** uno, longitudinal, durante los 6 semestres — propio o Reference Project

Este documento define **qué se aprende y en qué secuencia**. El curriculum está centrado en competencias. Las tecnologías concretas aparecen en el material práctico como implementaciones de referencia y pueden cambiar sin alterar el objetivo formativo.

## 1. Principios del plan

### 1.1. Competencias antes que tecnologías

El objetivo no es memorizar frameworks. El objetivo es desarrollar capacidad para entender problemas, modelar, construir, probar, desplegar, operar, diagnosticar y evolucionar software.

### 1.2. Un proyecto longitudinal

El mismo sistema crece durante los seis semestres siempre que sea pedagógicamente conveniente. Esto obliga a convivir con decisiones anteriores, deuda técnica y cambios de requisitos.

```text
S1 → dominio y fundamentos
S2 → persistencia y servicios
S3 → aplicación y delivery
S4 → arquitectura y sistemas
S5 → producción y operación
S6 → evolución y liderazgo técnico
```

### 1.3. Profundidad antes que amplitud

Es preferible comprender profundamente una tecnología y sus fundamentos antes que acumular herramientas superficialmente.

### 1.4. Primero el fundamento, después la abstracción

SQL antes que ORM. HTTP antes que framework. Procesos y redes antes que plataformas que los abstraen. La herramienta se aprende mejor cuando se entiende qué trabajo está automatizando.

### 1.5. Evidencia antes que acumulación

Terminar una lectura o una clase no demuestra dominio. Cada competencia debe producir evidencia observable y, cuando corresponda, una defensa técnica.

### 1.6. Inglés técnico

La lectura de documentación y bibliografía técnica en inglés forma parte de las capacidades profesionales del programa.

## 2. Proyecto

Hay dos modalidades.

1. **Proyecto propio:** el estudiante propone el problema y puede trabajar con usuarios o clientes reales.
2. **Reference Project:** proyecto proporcionado por el repositorio para quienes no dispongan de uno propio.

Ambos recorren las mismas competencias y milestones.

### Criterio de incorporación tecnológica

Antes de incorporar una tecnología nueva al proyecto, el estudiante debe poder responder:

1. ¿Qué problema resuelve?
2. ¿Por qué aparece ahora?
3. ¿Qué alternativas existen?
4. ¿Qué costo introduce?
5. ¿Cómo vamos a verificar que funcionó?

La complejidad debe crecer por necesidad, no por acumulación.

## 3. Política de IA

La IA se incorpora progresivamente. El objetivo es aprender a utilizarla sin delegar el razonamiento ni la responsabilidad técnica.

### S1–S2 — IA como tutor y asistente controlado

- La primera versión de las soluciones debe ser producida por el estudiante.
- La IA puede explicar conceptos, errores y código existente.
- Puede utilizarse para sugerir lecturas o preguntas de diagnóstico.
- No se debe copiar una implementación generada sin comprenderla.

### S3–S4 — Delegación con auditoría

Se permite delegar tareas mecánicas como boilerplate, refactors repetitivos o tests de casos ya identificados.

El estudiante debe revisar el diff completo, ejecutar la solución y verificar su comportamiento.

### S5–S6 — Flujo profesional

La IA puede participar ampliamente en diseño asistido, implementación, debugging, documentación, investigación y agentes de desarrollo.

La responsabilidad sobre la solución sigue siendo humana.

### Regla transversal

> **Todo código incorporado al proyecto debe poder ser explicado, modificado, verificado y defendido por el estudiante.**

La evaluación no penaliza el uso permitido de IA: evalúa la capacidad de comprender y verificar el resultado.

## 4. Progresión por semestre

| Semestre | Tema | El proyecto pasa a ser | Horas estimadas |
|---|---|---|---:|
| S1 | **Construir** | un dominio ejecutable y testeable | ~170 h |
| S2 | **Persistir y servir** | persistente y accesible mediante una interfaz | ~215 h |
| S3 | **Entregar software** | usable fuera de la máquina del desarrollador | ~260 h |
| S4 | **Diseñar sistemas** | más complejo, reproducible y resistente a fallos | ~300 h |
| S5 | **Producción** | operable, observable y recuperable | ~300 h |
| S6 | **Evolucionar** | documentado, defendible y preparado para evolución | ~250 h |
| **Total** | | | **~1.495 h** |

Las horas son una estimación de carga de trabajo y no constituyen un contrato de horas semanales exactas.

## 5. S1 — Construir

**Objetivo:** construir software pequeño, modular, testeable y versionado.

**Capacidades principales:** modelado de dominio, Python idiomático en la implementación de referencia, estructuras de datos, Git, testing unitario, debugging y documentación.

**Entregable:** programa ejecutable desde línea de comandos que gestiona el dominio en memoria y posee una suite de tests.

**Criterios de listo:**

- [ ] El dominio no depende de base de datos, red o interfaz.
- [ ] Las reglas de negocio importantes tienen tests.
- [ ] Los tests son rápidos y reproducibles.
- [ ] El historial de Git permite entender la evolución del proyecto.
- [ ] Las reglas fueron contrastadas con un usuario, cliente o especificación.
- [ ] El estudiante puede explicar el código y sus decisiones.

## 6. S2 — Persistir y servir

**Objetivo:** comprender la persistencia y comenzar a exponer el sistema mediante una interfaz controlada.

**Capacidades principales:** modelo relacional, normalización, SQL, planes de ejecución, transacciones, aislamiento, concurrencia, migraciones, repositorios, APIs y autenticación.

**Entregable:** el mismo sistema persistente, con migraciones, tests de integración contra una base real y una interfaz de acceso autenticada.

**Criterios de listo:**

- [ ] Puede escribir y explicar las consultas relevantes sin depender del ORM.
- [ ] Puede interpretar un plan de ejecución básico.
- [ ] Existe evidencia de comportamiento correcto ante operaciones concurrentes relevantes.
- [ ] El dominio continúa aislado de la persistencia.
- [ ] Las migraciones funcionan desde una base vacía.
- [ ] El backup fue ejecutado, restaurado y verificado.

## 7. S3 — Entregar software

**Objetivo:** llevar la aplicación a usuarios fuera del entorno de desarrollo.

**Capacidades principales:** HTTP, interfaz de usuario, autenticación y autorización, seguridad de aplicaciones, empaquetado reproducible, deployment, HTTPS, logs y backups.

**Entregable:** aplicación desplegada y utilizada por personas reales o por un grupo de prueba equivalente.

**Criterios de listo:**

- [ ] Usuarios externos utilizaron el sistema de forma sostenida.
- [ ] Los bugs encontrados fueron registrados y resueltos.
- [ ] Los controles de acceso fueron verificados mediante pruebas.
- [ ] Los backups son automáticos y existe una restauración probada.
- [ ] El sistema se recupera correctamente después de reiniciar los servicios.
- [ ] El estudiante puede explicar la infraestructura de deployment.

## 8. S4 — Diseñar sistemas

**Objetivo:** diseñar y modificar sistemas con mayor complejidad sin perder control sobre sus fallos.

**Capacidades principales:** integración continua, procesos en segundo plano, asincronía, colas, caching cuando existe una necesidad real, fallos parciales, reintentos, refactoring, deuda técnica, patrones y trade-offs.

**Entregable:** sistema reproducible, con pipeline de integración continua, procesamiento en segundo plano y una refactorización significativa realizada con una red de tests.

**Criterios de listo:**

- [ ] El entorno se puede reconstruir desde cero de forma reproducible.
- [ ] Los cambios relevantes pasan validaciones automáticas.
- [ ] Se completó una refactorización significativa sin pérdida funcional.
- [ ] Existen mecanismos para detectar fallos relevantes.
- [ ] Las decisiones arquitectónicas importantes están documentadas y justificadas.

## 9. S5 — Producción

**Objetivo:** operar software como servicio y diagnosticar problemas con evidencia.

**Capacidades principales:** sistemas y redes aplicados, deployment, rollback, observabilidad, métricas, logs, incidentes, performance, backup/restore, recuperación y seguridad operacional.

**Entregable:** servicio operable con procedimientos de deployment y rollback probados y evidencia de al menos un diagnóstico de fallo real o simulado.

**Criterios de listo:**

- [ ] Deployment y rollback fueron ejecutados y documentados.
- [ ] Existen métricas mínimas de salud.
- [ ] Se diagnosticó un fallo utilizando métricas, logs u otra evidencia.
- [ ] El estudiante puede explicar la topología de deployment.
- [ ] La recuperación ante escenarios definidos fue probada.

## 10. S6 — Evolucionar

**Objetivo:** integrar las competencias y demostrar autonomía profesional.

**Capacidades principales:** observabilidad avanzada, lectura de código ajeno, Open Source, investigación técnica, documentación, comunicación, liderazgo técnico, IA y agentes, arquitectura y evolución.

**Entregable:** sistema con observabilidad, portfolio técnico, evidencia de contribución externa y defensa técnica del proyecto completo.

**Criterios de listo:**

- [ ] Puede diagnosticar el estado del sistema a partir de evidencia.
- [ ] Realizó al menos una contribución a un proyecto externo.
- [ ] Puede explicar el sistema a audiencias técnicas y no técnicas.
- [ ] Puede justificar las principales decisiones arquitectónicas.
- [ ] Puede defender el uso de IA y verificar los resultados incorporados.
- [ ] Puede presentar y defender el proyecto completo.

## 11. Competencias y trazabilidad

El curriculum contiene **79 competencias, C01–C79**.

El plan determina la progresión. La matriz determina dónde se introduce, practica, consolida y evalúa cada competencia.

La trazabilidad buscada es:

```text
competencia
    ↓
semestre
    ↓
clase
    ↓
práctica
    ↓
project task
    ↓
evidencia
    ↓
competency gate
    ↓
milestone
```

Ver [`competencies.md`](competencies.md), [`competency-matrix.md`](competency-matrix.md) y [`assessment.md`](assessment.md).
