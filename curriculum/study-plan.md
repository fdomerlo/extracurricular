---
type: Directory Index
title: Plan de formación — Marco general
description: Plan de estudios agnóstico de tecnología, base común para cualquier instancia del programa.
---

# Plan de formación en desarrollo de software

- **Duración:** 6 semestres (~36 meses)
- **Estructura por semestre:** 22 semanas lectivas + receso
- **Dedicación de referencia:** 10 h/semana en semanas lectivas (~220 h por semestre, ~1.300 h en total)
- **Proyecto eje:** uno, longitudinal, durante los 6 semestres — propio o Reference Project

Este documento es el marco común. No prescribe lenguaje, framework, motor de base de datos ni arquitectura: eso lo define cada instancia (tu propio proyecto, o el Reference Project del repositorio) siguiendo el criterio de incorporación tecnológica de `project/project-model.md` §7.

Si tenés un proyecto propio y/o cliente real, este plan se completa con un documento derivado (`custom-plan.md` o equivalente) que sí nombra tecnologías, restricciones legales y decisiones concretas. Este documento nunca las nombra.

Este plan asume tres cosas. Si alguna deja de ser cierta, hay que reajustarlo.

1. **Algo programás.** No arranca de cero: arranca de "sé reconocer código cuando lo veo".
2. **Tenés (o elegís) un proyecto real.** Un cliente real, un usuario real, o en su defecto el Reference Project — pero siempre alguien que pueda quejarse del resultado. Eso enseña diseño de software mejor que cualquier libro.
3. **Tenés evidencia auditable.** Autoguiado (contra las rúbricas de `curriculum/assessment.md`) o con mentor — pero en ambos casos el criterio de "listo" es verificable, no una opinión.

---

## 1. Principios del plan

Estos seis puntos importan más que el temario. Si el temario se desvía y los principios se sostienen, el plan funciona igual.

**1.1. Un solo proyecto durante los 6 semestres.** No se empieza un proyecto nuevo por cada tema. El mismo sistema crece y convivís con tus propias malas decisiones. Eso es lo que pasa en un trabajo real: hoy te equivocás y dentro de un mes te vas a pasar dos semanas corrigiendo tus propias cagadas. Eso no lo enseña ningún curso.

**1.2. El código va a producción, o al menos a manos de un usuario real.** Un sistema que usan personas de verdad —aunque sean pocas— enseña validación, concurrencia, backups y manejo de errores mejor que cualquier ejercicio. El objetivo no es "terminar la app": es que alguien la use.

**1.3. Profundidad antes que amplitud.** Es preferible entender bien un motor de persistencia solamente, antes que conocer un poco de tres. Las tecnologías se aprenden en semanas; los fundamentos, en años.

**1.4. Primero a mano, después la herramienta.** SQL antes que el ORM. HTTP antes que el framework. La herramienta que te ahorra el trabajo solo te sirve si entendés el trabajo que te está ahorrando.

**1.5. Nada se da por terminado sin criterio de "listo".** Cada semestre tiene condiciones verificables (ver `curriculum/assessment.md` y las rúbricas por semestre). "Lo terminé" es una opinión, no un hecho.

**1.6. El inglés es parte del plan.** La bibliografía de calidad y gratuita en tu idioma cubre bien el arranque y después se vuelve escasa. No es opcional: es una habilidad técnica más.

---

## 2. El proyecto

### Dos modalidades

1. **Proyecto propio.** Vos proponés el problema. Puede haber cliente real, organización, o una necesidad que identificaste. Cuanto más real el usuario, mejor.
2. **Reference Project.** Si no tenés proyecto propio, usás el que provee el repositorio (`practice/*/reference-project/`). Recorre las mismas competencias y milestones que un proyecto propio.

### Si tu proyecto maneja datos reales de personas

Antes de que entre el primer dato real:

- **Durante el desarrollo, datos falsos.** Nada de datos reales en el entorno de desarrollo.
- **Backups automáticos y verificados** antes del primer dato real. Un backup que nunca se restauró no es un backup.
- **Investigá el marco legal aplicable** a los datos que vas a manejar (protección de datos personales, datos sensibles como salud o menores, derechos del usuario sobre su información) en tu jurisdicción. Esto se documenta en el `project-brief.md`, sección de restricciones legales.
- Si el sistema reemplaza algo que ya funciona, **corré en paralelo** hasta ganar la confianza de uso, no lo reemplaces de entrada.
- Acá el error no es un test en rojo. Es un problema real para alguien.

### Criterio de incorporación tecnológica

Antes de introducir cualquier tecnología nueva al proyecto, tenés que poder responder (ver `project/project-model.md` §7):

1. ¿Qué problema resuelve?
2. ¿Por qué aparece ahora?
3. ¿Qué alternativas existen?
4. ¿Qué costo introduce?
5. ¿Cómo vas a saber que funcionó?

Si no hay necesidad concreta, no se incorpora. La complejidad crece por necesidad, no por acumulación.

---

## 3. Política de IA

Hay una fase, típicamente entre el segundo y el cuarto semestre, donde la IA produce código que funciona y el estudiante no aprende nada. Se nota tarde: cuando algo se rompe y las herramientas mentales ya están atrofiadas por falta de uso. La política escala con el semestre, no es la misma todo el tiempo.

### S1–S2 — Restrictivo

- **Nada se commitea que no puedas explicar línea por línea.**
- La primera versión de todo la escribís vos.
- La IA se usa para **preguntar**: "¿por qué esto falla?", "¿qué hace este operador?", "explicame este error" — no para producir código.
- Permitido: que te explique código ajeno, que te revise algo que ya escribiste, que te sugiera qué leer.
- Prohibido: pedirle una función, copiarla y pegarla.

### S3–S4 — Delegación con auditoría

- Podés delegar ejecución mecánica: refactorizaciones repetitivas, boilerplate, tests de casos que ya identificaste.
- **Auditás el diff completo antes de aceptar.** Todo. Línea por línea.
- No delegás nada cuyo resultado no puedas verificar.

### S5–S6 — Flujo profesional

- Diseño y arquitectura tuyos; ejecución delegada; revisión tuya.
- La habilidad valiosa acá no es escribir código: es **leer un diff con criterio**. Se entrena revisando.

### Regla transversal

Una vez por mes, una sesión de dos horas sin ninguna asistencia: sin IA, sin autocompletado. Solo la documentación oficial. Es un diagnóstico, no un castigo. Si no podés con esa sesión, no se puede avanzar.

Esta política es compatible con la tabla de `curriculum/assessment.md`, pero es más granular: define el *mecanismo* de escalado, no solo el permiso por semestre.

---

## 4. Progresión por semestre

Cada semestre desarrolla capacidades, no tecnologías. La tabla completa de competencias (IDs `C01`–`C77`) vive en `curriculum/competencies.md`; acá va el resumen orientado al proyecto.

| Semestre | Tema | El proyecto pasa a ser |
|---|---|---|
| S1 | Construir | un dominio ejecutable, sin infraestructura |
| S2 | Persistir y servir | persistente, con acceso controlado a sus datos |
| S3 | Entregar software | usable por alguien fuera de tu máquina |
| S4 | Diseñar sistemas | capaz de sostener carga y fallar con criterio |
| S5 | Producción | operable fuera del entorno de desarrollo |
| S6 | Evolucionar | observable, documentado y defendible |

### S1 — Construir (~170 h)

**Objetivo:** separar la lógica del negocio de todo lo demás. Que el sistema funcione sin base de datos, sin red y sin interfaz gráfica.

**Capacidades:** modelado de dominio (entidades, valores, reglas, estados e invariantes), lenguaje y estructuras de datos idiomáticas, entorno de trabajo reproducible, control de versiones desde el primer commit, testing de comportamiento, debugging sistemático.

**Entregable:** un paquete ejecutable desde línea de comandos que gestiona el dominio en memoria, con suite de tests.

**Criterios de "listo"**
- [ ] Ningún archivo del dominio importa nada de base de datos, red o interfaz.
- [ ] Cada regla de negocio que podés enunciar en una frase tiene al menos un test.
- [ ] Los tests corren en segundos, no en minutos.
- [ ] El historial de versiones tiene commits atómicos con mensajes que explican el *por qué*.
- [ ] Alguien ajeno al código confirmó que las reglas modeladas son las reglas reales.
- [ ] Podés explicar cualquier línea del proyecto sin mirar notas.

### S2 — Persistir y servir (~215 h)

**Objetivo:** entender la persistencia de datos de verdad, no a través de una capa de abstracción. Empezar a exponer el sistema mediante una interfaz de acceso controlada.

**Capacidades:** modelo relacional, normalización, consultas y agregaciones a mano, lectura de planes de ejecución, transacciones y niveles de aislamiento, concurrencia (dos operaciones simultáneas sobre el mismo recurso), capa de repositorios recién después de dominar lo anterior, migraciones versionadas, diseño básico de una interfaz de acceso a los datos (API o equivalente), autenticación mínima.

**Entregable:** el mismo sistema, ahora persistente, con migraciones, tests de integración contra una base real, y una interfaz de acceso con al menos un mecanismo de autenticación.

**Criterios de "listo"**
- [ ] Podés escribir a mano cualquier consulta que la capa de abstracción genera.
- [ ] Sabés leer un plan de ejecución y explicar por qué una consulta usa o no un índice.
- [ ] Existe un test que demuestra que dos operaciones simultáneas sobre el mismo recurso no generan un estado inconsistente.
- [ ] El dominio de S1 sigue sin importar nada de persistencia.
- [ ] Las migraciones corren desde cero sobre una base vacía y dejan el esquema correcto.
- [ ] Hay un procedimiento de backup y **lo ejecutaste, restauraste y verificaste** al menos una vez.

> **Regla dura:** un tramo consistente de trabajo con SQL a mano antes de tocar cualquier capa de abstracción. El que aprende la herramienta antes que el fundamento no aprende el fundamento nunca.

### S3 — Entregar software (~260 h)

**Objetivo:** el salto real del plan. Al final de este semestre hay alguien usando el sistema, fuera de tu máquina.

**Capacidades:** protocolo de comunicación cliente-servidor (antes del framework), construcción de una interfaz de usuario, autenticación y permisos por rol, seguridad básica de aplicaciones (inyección, control de acceso roto, gestión de sesión), empaquetado reproducible, despliegue con proxy inverso, HTTPS, logs y backups automatizados.

**Entregable:** aplicación desplegada, con usuarios reales usándola.

**Criterios de "listo"**
- [ ] Al menos dos o tres personas la usaron durante dos semanas seguidas.
- [ ] Hay bugs reportados por usuarios reales y cerrados.
- [ ] Un usuario sin sesión válida no accede a ningún dato que no debería (lo verificaste probando, no suponiendo).
- [ ] Los backups corren solos y probaste una restauración completa.
- [ ] Sabés qué pasa si el servidor se reinicia: ¿vuelve solo el sistema?
- [ ] Podés explicar cada pieza de la infraestructura de despliegue y por qué está ahí.

> Este semestre es donde el proyecto deja de ser un ejercicio. Todo lo anterior existe para llegar acá.

### S4 — Diseñar sistemas (~300 h)

**Objetivo:** que el sistema se pueda cambiar sin miedo, y que empiece a sostener condiciones reales de uso: más carga, fallos parciales, procesos que no pueden bloquear al usuario.

**Capacidades:** entornos reproducibles y empaquetados, integración continua (linter, formateo, tests en cada cambio), procesos en segundo plano para tareas que no deben bloquear al usuario, alguna forma de cache cuando hay una necesidad real, manejo de fallos parciales y reintentos, refactorización con red de tests, deuda técnica (identificarla, documentarla, pagarla), patrones y principios de diseño aplicados a problemas reales que ya tenés — no como catálogo abstracto.

**Entregable:** el proyecto empaquetado de forma reproducible, con pipeline de integración continua, al menos un proceso en segundo plano funcionando, y una refactorización grande hecha con confianza.

**Criterios de "listo"**
- [ ] El entorno completo se levanta desde cero en una máquina limpia con un solo comando.
- [ ] Ningún cambio llega a la rama principal sin pasar los tests.
- [ ] Hiciste una refactorización que tocó una porción significativa del proyecto y no rompiste nada.
- [ ] Te enterás de que el sistema falló antes de que te lo reporten.
- [ ] Podés justificar cada patrón o principio de diseño que aplicaste con el problema real que resolvió.

### S5 — Producción (~300 h)

**Objetivo:** operar el sistema fuera del entorno de desarrollo, con criterio de qué pasa cuando algo falla.

**Capacidades:** fundamentos de sistemas operativos y redes aplicadas al despliegue, procedimiento de despliegue y de rollback documentados, métricas mínimas de salud del sistema (¿está caído? ¿está lento? ¿desde cuándo?), diagnóstico de al menos un incidente real o simulado, performance básica.

**Entregable:** sistema desplegado con procedimientos de despliegue y rollback probados, y evidencia de al menos un diagnóstico de fallo.

**Criterios de "listo"**
- [ ] Existe un procedimiento de despliegue documentado y uno de rollback, y ambos fueron ejecutados al menos una vez.
- [ ] Hay métricas mínimas visibles del estado del sistema.
- [ ] Diagnosticaste un fallo real (o simulado deliberadamente) usando esas métricas o logs, no adivinando.
- [ ] Podés explicar la topología completa de despliegue: qué corre dónde y por qué.

### S6 — Evolucionar (~250 h)

**Objetivo:** dejar de ser alguien que hizo un proyecto y pasar a ser alguien que trabaja de esto.

**Capacidades:** observabilidad (logs estructurados, métricas, trazas), lectura de código ajeno — la habilidad más subestimada de la profesión —, contribución a proyectos de terceros, documentación técnica, comunicación del proyecto a audiencias técnicas y no técnicas, uso de IA de forma verificable en un flujo profesional.

**Entregable:** el sistema con observabilidad mínima, al menos una contribución externa aceptada, portfolio documentado, y una defensa técnica del proyecto completo.

**Criterios de "listo"**
- [ ] Podés responder, con evidencia del propio sistema: ¿está caído? ¿está lento? ¿desde cuándo? ¿por qué?
- [ ] Al menos una contribución aceptada en un proyecto ajeno.
- [ ] Podés explicar el proyecto completo en cinco minutos a alguien técnico y en dos a alguien que no lo es.
- [ ] El repositorio permite reconstruir la evolución completa: problema → decisiones → errores → refactors → tests → despliegues → incidentes.

---

## 5. Ritmo y mecánica

### Semana tipo (10 h de referencia)

| Actividad | Horas | Observación |
|---|---|---|
| Escribir código en el proyecto | 6 | El grueso. No negociable. |
| Lectura dirigida | 2 | Bibliografía del semestre en curso. |
| Repaso y notas | 1 | Escribir qué aprendiste. Escribir es entender. |
| Buffer | 1 | Para la semana en que algo se complica. Siempre hay complicaciones. |

Ajustable según dedicación real, manteniendo la proporción.

### Estructura de las 22 semanas lectivas

| Semanas | Contenido |
|---|---|
| 1–16 | Clases del semestre, con Project Task en cada una. El número de clases varía por semestre (ver `practice/sX/schedule.md`); las semanas sobrantes son de consolidación, no de relleno |
| 17–18 | Integración del proyecto |
| 19 | Milestone: entrega |
| 20 | Defensa / revisión |
| 21 | Buffer / recuperación |
| 22 | Cierre / retrospectiva |

Después de las 22 semanas lectivas hay receso antes del semestre siguiente.

### Cadencia de revisión

- **Cada dos semanas (con mentor):** revisión de código, media hora, sobre un cambio real, no sobre "mostrame lo que hiciste". El valor está en las preguntas: *¿qué pasa si la persistencia se desconecta acá?* *¿por qué esta validación está en la interfaz y no en el dominio?*
- **Cada fin de semestre:** revisión contra los criterios de "listo". Los que no se cumplen se convierten en issues del backlog.
- **Primeras semanas de cada semestre nuevo:** cerrar los pendientes del semestre anterior antes de arrancar contenido nuevo, sin excepciones. La deuda técnica que no se paga en la primera oportunidad no se paga nunca.

Autodidacta sin mentor: la revisión de código la reemplaza la rúbrica de `curriculum/assessment.md` y una sesión propia de auto-revisión con la misma cadencia.

### Backlog

Un tablero de issues abierto y visible. Todo lo que quedó a medias, todo lo que sabés que está mal pero funciona, todo lo que un usuario reportó. Etiquetas mínimas: `bug`, `deuda-tecnica`, `mejora`.

---

## 6. Bibliografía

Independiente del stack elegido, estos recursos son agnósticos de tecnología y aplican siempre:

| Tema | Tipo de recurso a buscar | Cuándo |
|---|---|---|
| Herramientas, shell, control de versiones, depuración | Un curso o guía de fundamentos de herramientas de desarrollo (ej. el "Missing Semester" del MIT y sus traducciones) | S1, primeras semanas |
| Control de versiones en profundidad | El libro oficial de tu sistema de control de versiones (ej. Pro Git) | Caps. iniciales en S1; ramas y flujo en S3 |
| Índices y rendimiento de consultas | Un recurso agnóstico de motor sobre índices (ej. "Use The Index, Luke!") | S2 |
| Patrones, principios de diseño, refactorización | Un catálogo de patrones y refactors (ej. Refactoring Guru) | S4, cuando ya tengas código propio que arreglar, no antes |
| Seguridad web | OWASP Top 10 | S3 |
| Protocolo HTTP, HTML, CSS, JavaScript | La referencia web estándar de la industria (MDN o equivalente) | S3 en adelante, consulta permanente |

Para el lenguaje, framework y motor de persistencia que elijas (propios o del Reference Project), aplicá el mismo criterio: documentación oficial como núcleo, cursos de terceros solo para reforzar fundamentos. Esa bibliografía específica se documenta en el plan derivado de tu instancia (`custom-plan.md` o equivalente), no acá.

### Idioma de la bibliografía

Herramientas, control de versiones, fundamentos, índices, seguridad web, patrones suelen tener buena cobertura en castellano. Lo publicado en los últimos años sobre arquitectura, observabilidad, sistemas distribuidos y prácticas de operación tiende a estar mayormente en inglés.

El inglés técnico entra al plan alrededor de la mitad del primer año, no como algo aparte sino como la forma normal de leer documentación. Leer documentación técnica es mucho más fácil que hablarla.
