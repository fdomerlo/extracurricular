# Flujo de Trabajo del Estudiante (Student Workflow)

Esta guía establece cómo organizar tu espacio de trabajo local y tu repositorio personal para cursar **Extracurricular** de forma profesional y reproducible.

---

## 1. La Regla Fundamental: Dónde vive tu código

> **Extracurricular es tu currículo, especificación técnica y libro de texto. No debés commitear tu código de desarrollo dentro de este repositorio.**

```text
       CURRÍCULO CANÓNICO                       TU ESPACIO DE TRABAJO
  (github.com/.../extracurricular)          (github.com/tu-usuario/tu-proyecto)
   • Especificaciones y clases               • Código fuente de tu proyecto (src/)
   • Catálogo de competencias                • Tus suites de tests (tests/)
   • Rúbricas de evaluación                  • Tu historial de Git y branches
   • Plantillas de consulta                  • Tu pyproject.toml y lockfile
```

1. **`extracurricular`** se clona para lectura local o se consulta directamente desde GitHub.
2. **Tu proyecto de ingeniería** vive en **tu propio repositorio** (público o privado) bajo tu cuenta de Git.

Esta separación simula el entorno profesional real: las especificaciones de negocio y arquitectura vienen del cliente o Tech Lead, mientras que vos gestionás el ciclo de vida de tu propio repositorio.

---

## 2. Configuración Inicial de tu Proyecto

Tanto si vas a desarrollar el **Reference Project** (sistema de consultorio médico) como un **proyecto propio**:

### Paso 1: Crear tu repositorio
1. Creá un nuevo repositorio en GitHub: por ejemplo `consultorio-s1` o el nombre de tu dominio.
2. Clonaló en tu máquina local en una carpeta independiente a `extracurricular`:
   ```bash
   git clone git@github.com:tu-usuario/consultorio-s1.git
   cd consultorio-s1
   ```

### Paso 2: Inicializar el paquete con `uv`
Siguiendo las pautas de [`practice/s1/classes/S1-01.md`](../practice/s1/classes/S1-01.md):
```bash
# Inicializar paquete estructurado
uv init . --package

# Agregar dependencia de testing
uv add --dev pytest
```

### Paso 3: Estructura mínima de directorios
Tu repositorio debe adoptar el layout profesional `src/`:
```text
mi-proyecto/
├── .gitignore
├── pyproject.toml
├── uv.lock
├── README.md
├── src/
│   └── <mi_paquete>/
│       └── __init__.py
└── tests/
    ├── __init__.py
    └── test_placeholder.py
```

Commiteá esta estructura base como tu primer commit:
```bash
git add .
git commit -m "chore: inicializar proyecto con layout src/ y pytest vía uv"
git push origin main
```

---

## 3. Dinámica de Trabajo por Clase

Para cada clase de [`practice/s1/`](../practice/s1/README.md):

1. **Estudio conceptual y demostración:** Leé el problema que la clase busca resolver y entendé qué hace la demostración.
2. **Laboratorio y ejercicios:** Realizalos sin copiar y pegar. Podés usar una carpeta temporal de pruebas (`scratch/`) o scripts descartables.
3. **Rama de trabajo para el Project Task:** Creá una rama en tu proyecto personal para la funcionalidad de la clase:
   ```bash
   git checkout -b feature/s1-04-domain-models
   ```
4. **Implementación y tests:** Desarrollá la lógica de negocio y escribí tests que protejan el comportamiento contra regresiones.
5. **Verificación contra Definition of Done:** Cada clase incluye una lista de control al final (*Evidencia — Definition of Done*). No cierres la clase hasta que todos los puntos estén en verde.
6. **Merge limpio a `main`:**
   ```bash
   git checkout main
   git merge --no-ff feature/s1-04-domain-models
   git push origin main
   ```

---

## 4. Cierre de Semestre y Preparación de Milestone

Al completar la última clase del semestre (ej. `S1-11`):

1. **Corré tus tests y linters:**
   ```bash
   uv run pytest -v
   ```
2. **Autoauditoría de Hito:** Revisá los requisitos de entrega en [`practice/s1/milestone.md`](../practice/s1/milestone.md) y completá la plantilla [`tutoring/templates/milestone-check.md`](../tutoring/templates/milestone-check.md).
3. **Etiquetá tu versión:**
   ```bash
   git tag -a v0.1.0 -m "Milestone S1 completado: Dominio puro y suite de tests en verde"
   git push origin v0.1.0
   ```
4. **Defensa técnica:**
   - **Autodidactas:** Respondé por escrito las preguntas de defensa de `milestone.md` en un documento `docs/defense-m-s1.md` de tu proyecto.
   - **Con tutoría:** Enviá tu tag y formulario para coordinar la sesión sincrónica de defensa oral y code review.
