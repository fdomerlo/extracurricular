# Desarrollo Moderno de Software

[![Release](https://img.shields.io/badge/release-v1.0_(S1_Released)-0969da?style=flat-square)](docs/roadmap.md)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC_BY--NC--SA_4.0-lightgrey?style=flat-square)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es)
[![Curriculum](https://img.shields.io/badge/curriculum-validated-2da44e?style=flat-square)](.github/workflows/curriculum-lint.yml)

**Un curriculum open source de tres años para desarrollar capacidades profesionales de ingeniería de software.**

> No está organizado alrededor de frameworks de moda. Está organizado alrededor de la capacidad de entender problemas, modelar dominios, construir, probar, desplegar, operar y evolucionar software.

> `Problema` → `Modelado` → `Implementación` → `Testing` → `Delivery` → `Operación` → `Diagnóstico` → `Evolución` → `Defensa técnica`

*Las tecnologías cambian; las capacidades profesionales de ingeniería permanecen.*

> **Estado del programa (v1.0 — S1 Released):**  
> El **Semestre 1 ("Construir")** se encuentra completamente publicado, testeado y listo para ser cursado de forma autónoma o con acompañamiento. Los semestres S2 a S6 se desarrollan de forma abierta conforme a nuestro [`Roadmap`](docs/roadmap.md).

---

## ¿Para quién es?

Este programa está pensado para personas con una base previa de programación que buscan adquirir criterio, solidez y hábitos de ingeniería mediante práctica sostenida:

- **Estudiantes de informática:** para complementar los fundamentos académicos con las prácticas reales de la industria.
- **Autodidactas:** para recorrer un camino estructurado y con estándares profesionales sin perderse en tutoriales aislados.
- **Desarrolladores junior:** para consolidar bases de arquitectura, testing, debugging y diseño antes de dar el salto de seniority.
- **Proyectos propios o reales:** para quienes desean construir un producto de software real como vehículo integral de aprendizaje.

*El programa no reemplaza una carrera de grado ni impone una metodología única: entrena capacidades observables y verificables.*

---

## Tres años, seis semestres

El currículo se divide en seis semestres (aproximadamente 22 semanas académicas por semestre), combinando estudio conceptual, ejercicios, proyecto integrador y un hito (*milestone*) con defensa técnica:

| Semestre | Eje de Aprendizaje | Capacidad Demostrable al Finalizar | Estado |
|:---:|---|---|:---:|
| **S1** | **Construir** | Software pequeño, modular, testeable en memoria y versionado con Git. | **Disponible** ([`practice/s1/`](practice/s1/)) |
| **S2** | **Persistir y servir** | Modelado relacional riguroso, capa de persistencia y servicios web/API. | *En Roadmap* |
| **S3** | **Entregar software** | Producto full-stack desplegado, contenedorización (Docker) y pipelines de CI/CD. | *En Roadmap* |
| **S4** | **Diseñar sistemas** | Arquitecturas distribuidas, asincronismo, colas y resiliencia de datos. | *En Roadmap* |
| **S5** | **Producción** | Operabilidad real, métricas, observabilidad, debugging distribuido y post-mortems. | *En Roadmap* |
| **S6** | **Diseñar y liderar** | Decisiones mayores de arquitectura, evolución de sistemas legados y defensa técnica integral. | *En Roadmap* |

El mapa normativo completo de las 79 competencias evaluadas está detallado en [`curriculum/competencies.md`](curriculum/competencies.md) y el cronograma en [`curriculum/study-plan.md`](curriculum/study-plan.md).

> **Ritmo y dedicación:** La estimación de 3 años responde a una dedicación *part-time* estándar (~10–12 h/semana). Al ser un currículo guiado por competencias observables y no por tiempo de cursada fija, personas con mayor dedicación semanal o experiencia previa pueden avanzar a su propio ritmo y completarlo en **1 a 2 años** a medida que acrediten y defiendan los hitos (*milestones*). Más detalles en [`docs/faq.md`](docs/faq.md).

---

## El proyecto es el vehículo de aprendizaje

No aprendés cada tema en un ejercicio descartable. Un único proyecto de dominio real evoluciona incrementalmente en complejidad arquitectónica durante los seis semestres:

- **S1 · Dominio:** Modelado de negocio, lógica pura y testing unitario exhaustivo en memoria.
- **S2 · Persistencia y API:** Modelado relacional riguroso, transacciones ACID y exposición HTTP.
- **S3 · Web y Delivery:** Frontend funcional, contenedorización (Docker) y pipelines de CI/CD.
- **S4 · Arquitectura distribuida:** Servicios asíncronos, procesamiento por eventos y capas de caché.
- **S5 · Producción:** Métricas, observabilidad, trazabilidad distribuida y análisis de fallos.
- **S6 · Evolución:** Refactorización a gran escala, gestión de sistemas legados y defensa técnica integral.

Podés construir el **Reference Project** incluido en el repositorio (un sistema de gestión de turnos para consultorios con reglas estrictas de agenda) o aplicar exactamente el mismo estándar sobre un proyecto propio o con cliente real.

---

## Dos modalidades de recorrido

| Modalidad Autodidacta | Modalidad Acompañada |
|---|---|
| **100% Libre y Gratuita** | **Tutoría Personalizada y Code Review** |
| • Acceso irrestricto a todas las clases y ejercicios.<br>• Implementación de referencia abierta.<br>• Suites de tests y linters locales para autocorregir.<br>• Paso a paso documentado para avanzar a tu propio ritmo. | • Sesiones periódicas sincrónicas (1 a 1).<br>• Code review formativo exigente estilo Tech Lead.<br>• Asistencia metodológica en diseño y debugging.<br>• Simulacros de defensa técnica oral.<br>• **Cupos limitados por dedicación docente.** |
| 👉 **[Comenzar en docs/getting-started.md](docs/getting-started.md)** | 👉 **[Conocer la tutoría en tutoring/README.md](tutoring/README.md)** |

---

## Navegación del repositorio

- [`curriculum/`](curriculum/): Plan de estudio maestro, catálogo de competencias y criterios de evaluación.
- [`practice/`](practice/): Clases prácticas detalladas, laboratorios y desafíos (comenzando por [`practice/s1/`](practice/s1/)).
- [`project/`](project/): Especificaciones de requerimientos y modelo del proyecto longitudinal.
- [`tutoring/`](tutoring/): Protocolos de consulta asincrónica, rubber-ducking y plantillas de intake técnico.
- [`docs/`](docs/): Guías de inicio rápido ([`getting-started.md`](docs/getting-started.md)), preguntas frecuentes ([`faq.md`](docs/faq.md)) y estado del proyecto ([`roadmap.md`](docs/roadmap.md)).

---

## Contribuir

Extracurricular es un proyecto colaborativo y en constante evolución. Las contribuciones que mejoren la claridad pedagógica, incorporen ejercicios rigurosos o refinen la bibliografía son bienvenidas.

Consultá las pautas y el flujo de trabajo en [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Licencia

Este proyecto utiliza un esquema de licenciamiento dual:

- **Contenido educativo, textos y currículo:** Licenciado bajo [Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es). Podés usarlo, estudiarlo y adaptarlo libremente para fines personales y formativos no comerciales, citando la autoría original. Queda prohibida su comercialización sin autorización.
- **Código fuente, herramientas y scripts (`tools/`, `tests/`):** Licenciados bajo la [Licencia MIT](LICENSE).

---

## Apoyo al proyecto

El currículo publicado permanece completamente abierto y gratuito. Si este material te resulta valioso en tu camino profesional y querés apoyar su investigación pedagógica y mantenimiento continuo, podés colaborar a través de:

[![Cafecito](https://img.shields.io/badge/Colaborar-Cafecito-FFDD00?style=flat-square&logo=cafecito)](https://cafecito.app/fdomerlo)
[![PayPal](https://img.shields.io/badge/Donar-PayPal-00457C?style=flat-square&logo=paypal)](https://paypal.me/FernandoMerlo)
[![Mercado Pago](https://img.shields.io/badge/Colaborar-Mercado%20Pago-009EE3?style=flat-square&logo=mercadopago)](https://link.mercadopago.com.ar/fdomerlo)

- **PayPal:** Para aportes directos en moneda extranjera (USD/EUR).
- **Mercado Pago / Cafecito:** Para colaboraciones en moneda local.

*Las tutorías personalizadas y revisiones técnicas individuales son servicios profesionales independientes del currículo de acceso libre.*
