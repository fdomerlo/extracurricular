# Roadmap

Este repositorio es un curriculum vivo. El diseño general abarca seis semestres, pero el material práctico se desarrolla y valida progresivamente.

## Estado actual

| Área | Estado |
|---|---|
| Modelo curricular | Establecido |
| Competencias | Definidas |
| Matriz de competencias | Definida |
| Marco de evaluación | Definido |
| Modelo de proyecto | Definido |
| S1 — Construir | Material de referencia disponible |
| S2 — Persistir y servir | Material de referencia disponible |
| S3 — Entregar software | Estructura y planificación disponibles; contenido en desarrollo |
| S4 — Diseñar sistemas | Planificado |
| S5 — Producción | Planificado |
| S6 — Diseñar y liderar | Planificado |

## Principio de desarrollo

El objetivo no es publicar rápidamente seis semestres de texto. Cada etapa debe mantener trazabilidad pedagógica:

> `Competencia` → `Clase` → `Práctica` → `Proyecto` → `Evidencia` → `Milestone`

Un semestre se considera suficientemente maduro cuando esa cadena puede recorrerse sin depender de explicaciones externas no documentadas.

## Fase 1 — Fundación

- [x] Definir propósito del programa.
- [x] Definir progresión de seis semestres.
- [x] Definir competencias y niveles de dominio.
- [x] Definir matriz de competencias.
- [x] Definir marco de evaluación.
- [x] Definir modelo de proyecto longitudinal.
- [x] Definir Reference Project como alternativa para autodidactas.
- [x] Definir modelo general de tutoría.
- [x] Documentar cómo comenzar.
- [x] Documentar preguntas frecuentes.

## Fase 2 — S1: Construir

- [x] Definir objetivo y resultado esperado.
- [x] Definir calendario.
- [x] Definir catálogo de clases.
- [x] Publicar material de las clases.
- [x] Definir laboratorios y challenges.
- [x] Definir milestone.
- [x] Definir rúbrica.
- [x] Publicar Reference Project inicial.
- [x] Validar el recorrido completo con estudiantes.
- [x] Incorporar feedback de implementación.

## Fase 3 — S2: Persistir y servir

Objetivo: convertir el dominio construido en S1 en una aplicación persistente, testeada y servida mediante HTTP.

Prioridades:

- [x] Completar clases.
- [x] Completar laboratorios.
- [x] Completar challenges.
- [x] Completar project tasks.
- [x] Definir evidencia por competencia.
- [x] Completar milestone M-S2.
- [x] Completar Reference Project.
- [ ] Ejecutar una cohorte piloto.
- [ ] Revisar carga y dificultad.

## Fase 4 — S3: Entregar software

Objetivo: llevar la aplicación a un ciclo de entrega reproducible.

Áreas esperadas:

- frontend práctico;
- integración de aplicación;
- Docker y entornos reproducibles;
- CI/CD;
- configuración;
- deployment;
- seguridad aplicada;
- testing de sistema.

Pendiente de autoría y validación.

## Fase 5 — S4: Diseñar sistemas

Objetivo: introducir problemas de arquitectura, asincronía, concurrencia, escalabilidad y evolución.

Áreas esperadas:

- arquitectura modular;
- límites y dependencias;
- concurrencia;
- workers;
- colas y procesamiento asíncrono;
- caching;
- performance;
- observabilidad inicial;
- ADRs y trade-offs.

Pendiente de autoría y validación.

## Fase 6 — S5: Producción

Objetivo: aprender a operar software como servicio.

Áreas esperadas:

- Linux aplicado;
- deployment;
- observabilidad;
- métricas;
- incidentes;
- recuperación;
- backup y restore;
- tolerancia a fallos;
- seguridad operacional;
- SLI / SLO.

Pendiente de autoría y validación.

## Fase 7 — S6: Diseñar y liderar

Objetivo: integrar las competencias y demostrar autonomía profesional.

Áreas esperadas:

- arquitectura de sistemas;
- evolución del producto;
- investigación de alternativas;
- decisiones técnicas;
- comunicación técnica;
- liderazgo técnico;
- agentes y desarrollo por especificación;
- verificación humana de sistemas asistidos por IA;
- proyecto final;
- defensa técnica.

Pendiente de autoría y validación.

## Validación pedagógica

Cada semestre nuevo debe validarse antes de considerarse estable.

La validación debería incluir:

1. recorrido completo por una persona distinta del autor;
2. revisión de carga horaria;
3. detección de prerrequisitos faltantes;
4. revisión de alineación entre competencias y actividades;
5. evaluación de los milestones;
6. feedback de estudiantes;
7. revisión de material obsoleto;
8. registro de cambios relevantes.

## Evolución tecnológica

Las herramientas pueden cambiar sin modificar automáticamente las competencias.

Una tecnología nueva debería incorporarse solamente cuando:

1. resuelva un problema pedagógico o profesional relevante;
2. exista una competencia que justifique su presencia;
3. pueda integrarse sin introducir complejidad accidental;
4. aporte una evidencia que no pueda obtenerse mejor de otra forma.

## Versionado

Las versiones del curriculum deberían reflejar cambios significativos en el modelo pedagógico, no cada modificación menor de texto.

Una futura estrategia puede utilizar releases como:

```text
v0.x  desarrollo y validación
v1.0  curriculum base validado
v1.x  mejoras compatibles
v2.0  cambios estructurales del curriculum
```

## Próximo objetivo

El próximo hito operativo es completar y validar S2 sin romper la trazabilidad entre competencias, clases, práctica, proyecto y evaluación.

La prioridad es **calidad y coherencia antes que volumen de contenido**.
