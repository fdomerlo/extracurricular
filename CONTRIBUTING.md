# Contribuir a Extracurricular

¡Gracias por tu interés en contribuir a **Extracurricular**! Este proyecto es un currículo abierto centrado en el desarrollo de competencias de ingeniería de software.

---

## 1. Principios de Contribución

1. **Autonomía del estudiante:** Cualquier mejora en las clases o ejercicios debe preservar la capacidad del estudiante autodidacta de resolver las actividades sin requerir intervención sincrónica obligatoria.
2. **Trazabilidad y esquema:** Toda clase (`practice/s*/classes/S*-*.md`) debe mantener un encabezado YAML frontmatter válido conforme a las competencias (`curriculum/competencies.md`).
3. **No romper la progresión:** Las 79 competencias profesionales (`C01` a `C79`) y los hitos semestrales (`M-S1` a `M-S6`) son normativos. No se eliminan ni alteran sus identificadores canónicos.

---

## 2. Flujo de Trabajo

1. **Fork y rama:** Creá una rama descriptiva a partir de `main` (`git switch -c fix/descripcion` o `feature/descripcion`).
2. **Validación local:** Antes de proponer cambios, verificá que los metadatos y enlaces sean consistentes:
   ```bash
   # Validar estructura y metadata curricular
   python3 tools/curriculum_lint.py --semester S1
   ```
3. **Commits semánticos:** Seguí la convención de [Conventional Commits](https://www.conventionalcommits.org/) (ej. `docs: corregir errata en S1-04`, `test: agregar caso límite`).
4. **Pull Request:** Abrí un Pull Request describiendo qué problema pedagógico o técnico resuelve y cómo fue verificado.

---

## 3. Canales de Comunidad y Debate (GitHub Discussions)

Para mantener los *Issues* enfocados exclusivamente en bugs, erratas y desarrollo de contenido curricular, las consultas de aprendizaje se canalizan en **GitHub Discussions**:

- **`#dudas-s1`:** Preguntas conceptuales sobre las clases, laboratorios o ejercicios de S1.
- **`#show-your-project`:** Espacio para compartir tu repositorio personal o Reference Project y recibir feedback técnico entre pares.
- **`#ideas-y-arquitectura`:** Debates abiertos sobre decisiones de modelado, diseño de sistemas y propuestas para futuros semestres (S2–S6).

> Si estás cursando de forma autodidacta, Discussions es tu punto de encuentro para aprender junto a otros compañeros de estudio. Para acompañamiento individual sincrónico y code review estilo Tech Lead, consultá las pautas de admisión en [`tutoring/README.md`](tutoring/README.md).
