---
type: Directory Index
title: Plan de formación — Instancia (Consultorio odontológico)
description: Instancia concreta de curriculum/study-plan.md. Nombra tecnología, cliente real y restricciones legales.
version: 2 — actualiza la v1 para referenciar clases reales por ID en vez de listar contenido, y fija la ubicación de HTTP en S3.
---

# Plan de formación en desarrollo de software — Consultorio odontológico

Este documento **hereda de `curriculum/study-plan.md`**. No repite los principios, la política de IA por semestre ni la mecánica de ritmo y revisión: esos valen sin cambios. Acá se completa lo que `curriculum/study-plan.md` deja abierto a propósito: stack, cliente real, restricciones legales y bibliografía específica.

**Stack:** Python · Django · HTMX · PostgreSQL
**Modalidad:** con mentor (supervisor con experiencia que revisa código cada dos semanas)
**Proyecto eje:** sistema de gestión de turnos para consultorio odontológico
**Usuario real:** el consultorio — odontólogo, secretaria y pacientes

### Por qué este stack

Siguiendo el criterio de incorporación tecnológica de `curriculum/study-plan.md` §2: Django + HTMX se elige porque es **server-rendered** y permite que en S3 haya algo desplegado y usable por personas reales sin la complejidad adicional de mantener una API separada y un frontend independiente. Para un sistema de tres roles de usuario y un solo cliente, esa complejidad no está justificada todavía — si en algún momento aparece una necesidad concreta (una app móvil nativa, un tercero que consuma los datos), ahí se evalúa agregar una API real, no antes.

> Si estás siguiendo el plan de forma autodidacta o con otro proyecto, no tenés que replicar este stack. `curriculum/study-plan.md` es agnóstico a propósito; este documento es un ejemplo de cómo se completa, no una prescripción.

### Nota sobre esta versión (v2)

La v1 de este documento listaba contenidos por semestre en bullets. Eso duplicó, en al menos tres puntos (HTTP, seguridad web, despliegue/Nginx/HTTPS), contenido que ya existía como clases propias en el catálogo real del repositorio — escrito sin visibilidad completa de ese catálogo. Esta versión corrige eso: **de acá en más, este documento no describe contenido de clase, solo referencia clases por ID.** El contenido vive en `practice/sX/classes/`, una sola vez, sin copia.

---

## Advertencia legal — datos de pacientes reales

Son **datos de pacientes reales**. En Argentina eso cae bajo la Ley 25.326 de Protección de Datos Personales (los datos de salud son "datos sensibles", con requisitos más estrictos) y la Ley 26.529 sobre derechos del paciente e historia clínica.

En términos prácticos, desde el día uno:

- **Durante el desarrollo, datos falsos.** Nada de pacientes reales en la base de datos de desarrollo.
- **Backups automáticos y verificados** antes de que entre el primer dato real. Un backup que nunca se restauró no es un backup.
- **El sistema corre en paralelo con lo que usen hoy**, no lo reemplaza, hasta que se haya ganado la confianza en el uso.
- Acá el error no es un test en rojo. Es un problema serio para el consultorio.

Esto completa la sección de restricciones legales del `project-brief.md` del proyecto.

---

## Progresión — mapeo a los 6 semestres de `curriculum/study-plan.md`

| Semestre | Tema (`curriculum/study-plan.md`) | El sistema de turnos |
|---|---|---|
| S1 | Construir | motor de dominio por CLI: Paciente, Profesional, Turno, Práctica |
| S2 | Persistir y servir | PostgreSQL + Django ORM + admin + autenticación por rol |
| S3 | Entregar software | HTTP, Django + HTMX desplegado, con odontólogo/secretaria/pacientes usándolo |
| S4 | Diseñar sistemas | recordatorios en segundo plano, logging estructurado, refactor grande |
| S5 | Producción | servidor real operado con procedimientos de despliegue y rollback |
| S6 | Evolucionar | observabilidad, código ajeno, segundo lenguaje, salida profesional |

---

## S1 — Motor de dominio

**Objetivo:** separar la lógica del negocio de todo lo demás. Que el sistema de turnos funcione sin base de datos, sin web y sin interfaz gráfica.

**Clases** (`practice/s1/classes/`) — ya autoradas, 11 en total:

| ID | Título |
|---|---|
| S1-01 | Entorno de desarrollo |
| S1-02 | Python idiomático |
| S1-03 | Manejo de errores — excepciones propias del dominio |
| S1-04 | Modelado de dominio — entidades y valores |
| S1-05 | Reglas de negocio del consultorio |
| S1-06 | Testing con pytest aplicado al dominio |
| S1-07 | Git en profundidad — ramas y flujo de trabajo |
| S1-08 | Pensar como debugger |
| S1-09 | Reproducir un bug |
| S1-10 | Pull Requests y revisión de código |
| S1-11 | IA como tutor y verificador |

**Entregable:** un paquete Python con interfaz de línea de comandos que gestiona turnos en memoria, con suite de tests.

**Criterios de "listo"**
- [ ] Ningún archivo del paquete de dominio importa nada de base de datos, web o interfaz.
- [ ] Cada regla del consultorio que podés enunciar en una frase tiene al menos un test.
- [ ] Los tests corren en menos de 5 segundos.
- [ ] El historial de git tiene commits atómicos con mensajes legibles, no "cambios" ni "fix", y al menos una rama con un merge real (`S1-07`).
- [ ] Al menos un cambio entró por Pull Request con descripción y revisión, no por merge directo (`S1-10`).
- [ ] Tu papá miró la lista de reglas y confirmó que son las reglas reales del consultorio.
- [ ] Podés explicar cualquier línea del proyecto sin mirar notas.

---

## S2 — Persistencia

**Objetivo:** entender bases de datos relacionales de verdad, no a través de una capa de abstracción. Exponer el dominio mediante el admin de Django y autenticación básica.

**Clases** (`practice/s2/classes/`) — pendientes de autoría con el mismo criterio que S1. No se listan bullets de contenido acá para evitar que este documento se desalinee del catálogo real, como pasó en la v1. Cuando se autoren, referenciarlas por ID en esta tabla.

> **HTTP no vive en S2 — aplicado.** El stub `S2-05 — HTTP desde el lado del servidor` se mudó a `S3-01 — HTTP como protocolo`, y las clases de S2 se renumeraron para cerrar el hueco. S2 queda con 15 clases.

**Entregable:** el mismo sistema, ahora persistente en PostgreSQL, con migraciones, tests de integración contra una base real, y gestionable desde el admin de Django con roles diferenciados.

**Criterios de "listo"**
- [ ] Podés escribir a mano cualquier consulta que el ORM genera.
- [ ] Sabés leer un `EXPLAIN` y explicar por qué una consulta usa o no usa un índice.
- [ ] Existe un test que demuestra que dos reservas simultáneas del mismo turno no pueden coexistir.
- [ ] El dominio de S1 sigue sin importar nada de base de datos.
- [ ] Las migraciones corren desde cero sobre una base vacía y dejan el esquema correcto.
- [ ] Hay un script de backup y **lo ejecutaste, restauraste y verificaste** al menos una vez.
- [ ] El admin de Django distingue lo que puede hacer un odontólogo de lo que puede hacer una secretaria.

> **Regla dura del semestre:** SQL a mano un tiempo consistente antes de tocar el ORM. El que aprende el ORM primero no aprende SQL nunca.

---

## S3 — Web y puesta en producción

**Objetivo:** el salto real del plan. Al final de este semestre hay gente usando el sistema.

**Clases** (`practice/s3/classes/`) — pendientes de autoría, mismo criterio.

> **HTTP vive acá — aplicado.** `S3-01 — HTTP como protocolo` (métodos, códigos de estado, cookies, sesiones) es la primera clase del semestre, **antes** de tocar Django. Django, HTMX, auth en vistas propias, seguridad aplicada y despliegue (Nginx/HTTPS/backups) van después, en ese orden. S3 queda con 17 clases. No listar el detalle de cada una acá hasta autorarlas — evita el mismo problema de duplicación que tuvo la v1.

**Entregable:** aplicación web desplegada, con usuarios reales del consultorio usándola.

**Criterios de "listo"**
- [ ] Tres personas del consultorio la usaron durante dos semanas seguidas.
- [ ] Hay al menos cinco bugs reportados por usuarios reales y cerrados.
- [ ] Un usuario sin sesión no accede a ningún dato de pacientes (lo verificaste probando, no suponiendo).
- [ ] Los backups corren solos y probaste una restauración completa.
- [ ] Sabés qué pasa si el servidor se reinicia: ¿vuelve solo el sistema?
- [ ] Podés explicar qué hace Nginx y por qué está ahí.

---

## S4 — Operación

**Objetivo:** que el sistema se pueda cambiar sin miedo.

**Clases** (`practice/s4/classes/`) — pendientes de autoría, mismo criterio.

> ⚠️ **Revisar contra el repo real antes de autorar.** La v1 de este documento ubicaba Docker, Compose y CI en S4 — pero según el catálogo real, esas clases viven en S3 (`S3-09` a `S3-12`), y Claude Code ya lo corrigió en el commit 5 de la sesión de reestructuración. No repitas ese contenido acá. Lo que sí es propio de S4, sin solapamiento conocido: procesos en segundo plano (recordatorios de turno), logging estructurado, refactor con red de tests, deuda técnica, y patrones de diseño aplicados a problemas reales ya identificados en el proyecto.

**Entregable:** el proyecto containerizado (heredando la base de S3), con recordatorios automáticos funcionando en segundo plano, y una refactorización grande hecha con confianza.

**Criterios de "listo"**
- [ ] `docker compose up` levanta todo el sistema en una máquina limpia.
- [ ] Ningún cambio llega a la rama principal sin pasar los tests.
- [ ] Hiciste una refactorización que tocó más de veinte archivos y no rompiste nada.
- [ ] Los recordatorios de turno se envían sin bloquear la reserva, y un fallo de envío no rompe el turno.
- [ ] Podés justificar cada patrón aplicado con el problema real que resolvió.

---

## S5 — Producción

**Objetivo:** operar el sistema fuera del entorno de desarrollo, con criterio de qué pasa cuando algo falla.

**Clases** (`practice/s5/classes/`) — pendientes de autoría, mismo criterio.

**Entregable:** sistema en producción con procedimientos de despliegue y rollback probados, métricas mínimas visibles, y un diagnóstico de incidente documentado.

**Criterios de "listo"**
- [ ] Ejecutaste un despliegue y un rollback siguiendo el procedimiento documentado, sin improvisar.
- [ ] Hay un tablero o registro mínimo de estado del sistema, accesible sin entrar al servidor.
- [ ] Te enterás de que el sistema se cayó antes de que te llamen.
- [ ] Diagnosticaste un incidente con evidencia (logs, métricas), no adivinando la causa.

---

## S6 — Profesionalización

**Objetivo:** dejar de ser alguien que hizo un proyecto y pasar a ser alguien que trabaja de esto.

Acá el proyecto pasa a segundo plano. Se mantiene, no crece.

**Clases** (`practice/s6/classes/`) — pendientes de autoría, mismo criterio.

**Entregable:** el sistema con observabilidad mínima, al menos una contribución externa aceptada, portfolio documentado y defensa técnica del proyecto completo.

**Criterios de "listo"**
- [ ] Al menos tres contribuciones aceptadas en proyectos ajenos.
- [ ] Cobraste por escribir código al menos una vez.
- [ ] Podés explicar tu proyecto en cinco minutos a alguien técnico y en dos a alguien que no lo es.
- [ ] El repositorio permite reconstruir la evolución completa del consultorio: problema → decisiones → errores → refactors → tests → despliegues → incidentes.

> **Sobre un segundo lenguaje:** el plan es 100% Python hasta acá. Es una decisión pedagógica y estratégica. Python es fácil, pero es cierto que hoy se buscan juniors en JavaScript, TypeScript, Java o .NET. El avance de la IA hace que el lenguaje empiece a estar en segundo plano: de acá a tres años el mercado va a pedir Ingenieros de IA (AI Engineer), para lo que con Python vas a tener una base muy sólida.
>
> **Sobre el timing:** si tenés un ritmo de estudio constante y las prácticas las realizás sin problemas, hacia la segunda mitad del plan vas a estar invirtiendo más tiempo en el desarrollo del sistema del consultorio que en el estudio formal, la IA ya es un asistente viable (con tu auditoría) y además ya sos empleable.

---

## Bibliografía específica de esta instancia

Todo este listado es **gratuito y en castellano**, salvo donde se indique. Complementa la bibliografía agnóstica de `curriculum/study-plan.md` §6.

### Núcleo — leer completo

| Tema | Recurso | Cuándo | Notas |
|---|---|---|---|
| Herramientas, shell, git, depuración | **Semestre faltante** (MIT) — `missing-semester-esp.github.io`, `missing.csail.mit.edu` | S1, primeras semanas (git y shell); depuración en `S1-08` | Traducción comunitaria del curso del MIT. Es exactamente lo que la facultad no enseña. |
| Git en profundidad | **Pro Git**, Chacon y Straub — `git-scm.com/book/es/v2` | Cap. 1–2 en `S1-01`; cap. 3 en `S1-07`; cap. 6 (contribución) en `S1-10`; caps. 5 y 7 en S3 | Traducción completa y oficial. Es *el* libro de git. |
| Python | **Documentación oficial de Python en español** — `docs.python.org/es/3/` | S1, permanente | El tutorial oficial más la referencia de biblioteca. Traducción oficial y completa. |
| Índices, rendimiento SQL | **Use The Index, Luke!**, Markus Winand — `use-the-index-luke.com/es` | S2 | Traducción completa al español, revisada por el autor. El mejor material que existe sobre índices, y agnóstico de motor. |
| Patrones, SOLID, refactorización | **Refactoring Guru** — `refactoring.guru/es` | S4 | La web es gratuita y muy buena. El libro es pago; no hace falta. Leelo cuando ya tengas código feo propio que arreglar, no antes. |
| Seguridad web | **OWASP Top 10** — `owasp.org/Top10/` | S3 | La edición 2021 tiene traducción oficial al español. Ediciones más recientes pueden estar solo en inglés todavía. |
| Testing | **Documentación oficial de pytest** — `docs.pytest.org` | S1 (`S1-06`) | En inglés, sin traducción oficial completa. Primera exposición corta a documentación técnica en inglés. |

### Referencia — para consultas, no es material de estudio

| Tema | Recurso | Notas |
|---|---|---|
| HTTP, HTML, CSS, JavaScript | **MDN Web Docs en español** — `developer.mozilla.org/es/` | La referencia web estándar de la industria. Buena parte traducida; lo no traducido cae a inglés automáticamente. |
| Django | Documentación oficial — `docs.djangoproject.com` | La traducción al español es parcial. El tutorial oficial en inglés es excelente; este es un buen primer contacto forzado con documentación técnica en inglés. |
| PostgreSQL | Documentación oficial — `postgresql.org/docs/` | Traducciones al español al día del proyecto comunitario, pero suelen ir por detrás de la versión actual. Para el tutorial alcanza; para lo avanzado, inglés. |

### Si necesita reforzar fundamentos

| Tema | Recurso | Notas |
|---|---|---|
| Programación desde cero | **Python para Todos**, Charles Severance — `es.py4e.com/book` | Traducción al español, gratuita, del libro y los materiales. Solo si hace falta apuntalar bases. |

### Meta-recursos

| Recurso | Para qué |
|---|---|
| `github.com/EbookFoundation/free-programming-books` (archivo `free-programming-books-es.md`) | Catálogo mantenido de libros libres en castellano por tema. |
| `gnu.org/doc/other-free-books.es.html` | Listado de libros libres de la FSF. |

---

## Correspondencia con la versión anterior de este documento

Este documento reemplazó la versión de bloques (`B1`–`B5`, 36 meses) por los 6 semestres de `curriculum/study-plan.md`. Tabla de equivalencia original:

| Bloque anterior | Semestres nuevos | Nota |
|---|---|---|
| B1 — Motor de dominio (meses 1–4) | S1 | Expandido de 6 a 11 clases al autorar contenido real (git, PRs, debugging, IA se sumaron). |
| B2 — Persistencia (meses 5–9) | S2 | Se le agregó admin de Django y auth por rol, que antes estaba en B3. |
| B3 — Web y producción (meses 10–15) | S3 | HTTP confirmado acá, no en S2: es `S3-01`. |
| B4 — Operación (meses 16–22) | S4 | Docker/CI corregido: viven en S3, no en S4 (v1 los tenía mal ubicados). |
| — (nuevo) | S5 | Antes no existía como bloque propio. |
| B5 — Profesionalización (meses 23–36, ~600h) | S6 | Acotado a un semestre; el contenido de producción se movió a S5. |

---

_Documento vivo, revisar al final de cada semestre. Hereda de `curriculum/study-plan.md`: si algo acá contradice un principio de ese documento, gana `curriculum/study-plan.md`. Para contenido de clase, gana siempre `practice/sX/classes/` sobre lo que diga este documento._
