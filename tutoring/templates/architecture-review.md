# Consulta de Tutoría — Revisión de Diseño y Arquitectura

Completá este formulario cuando hayas tomado una decisión de diseño, estructura o modelado sobre tu proyecto y quieras revisar sus *trade-offs*, alternativas y consecuencias técnicas junto al tutor.

---

## 1. Datos Generales

- **Estudiante:** 
- **Fecha:** 
- **Semestre / Proyecto:** (ej. S1 Consultorio, S2 Proyecto propio)
- **Repositorio / Rama / PR:** (ej. `rama-dominio-turnos` o enlace al commit)

---

## 2. Contexto de la Decisión

1. **¿Qué problema de negocio, requerimiento funcional o necesidad técnica motivó este cambio?**
   > [Describí brevemente el motivo del cambio]

2. **Área arquitectónica impactada:** (marcar las que aplican con `[X]`)
   - [ ] Modelado de dominio y entidades
   - [ ] Manejo de estado, mutabilidad y transiciones
   - [ ] Separación de capas (dominio vs persistencia vs interfaz)
   - [ ] Diseño de errores y excepciones
   - [ ] Estrategia de testing o test doubles
   - [ ] Organización de módulos y paquetes

---

## 3. Alternativas Consideradas

*Todo buen diseño surge de comparar alternativas. Explicá al menos dos opciones que evaluaste:*

### Alternativa A (la que implementaste o preferís)
- **Descripción:** [Cómo funciona o cómo está estructurada]
- **Motivo de elección:** [Por qué te parece la mejor opción para esta etapa]

### Alternativa B (la descartada o en duda)
- **Descripción:** [Qué otra alternativa contemplaste]
- **Motivo de descarte o duda:** [Por qué no te convenció o qué riesgo le viste]

---

## 4. Trade-offs y Consecuencias Asumidas

*Marcá con `[X]` los compromisos que identificás en tu diseño actual:*
- [ ] Privilegié simplicidad inicial sobre flexibilidad futura (evité abstracción prematura).
- [ ] Privilegié extensibilidad / desacoplamiento aunque sume más clases o interfaces.
- [ ] Privilegié inmutabilidad / seguridad aunque implique copiar estructuras en memoria.
- [ ] Privilegié legibilidad directa sobre optimizaciones de rendimiento.
- [ ] Acepté un acoplamiento temporal que deberé refactorizar en un semestre posterior.

---

## 5. Código o Diff a Revisar

- **Archivos clave involucrados (máximo 1 o 2 archivos relevantes):**
  > [Rutas o nombres de archivo, ej. `src/domain/appointments.py`]
- **Pregunta central para debatir en la sesión sincrónica:**
  > [Ejemplo: "¿Tiene sentido abstraer esta validación en una regla de negocio separada o alcanza con un método de la entidad?"]
