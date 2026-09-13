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

Para facilitar tu arranque, disponés de dos opciones:

### Opción A: Comenzar con el Starter Boilerplate (Recomendada)
En [`practice/s1/boilerplate/`](../practice/s1/boilerplate/) tenés una plantilla completa y preconfigurada con:
- `requirements.md` con las entidades e invariantes de dominio listos para ser leídos por la **Plataforma de Tutoría Socrática con IA**.
- `pyproject.toml` configurado para Python 3.12+, `uv`, `pytest` y `ruff`.
- Layout `src/consultorio` y tests iniciales en verde.
- `.github/workflows/ci.yml` para correr automáticamente tests en GitHub Actions en cada push.

Podés copiar el contenido de [`practice/s1/boilerplate/`](../practice/s1/boilerplate/) a la carpeta de tu nuevo repositorio:
```bash
# 1. Creá tu repo local
mkdir mi-consultorio && cd mi-consultorio
git init

# 2. Copiá el boilerplate desde extracurricular
cp -r /ruta/a/extracurricular/practice/s1/boilerplate/* .
cp /ruta/a/extracurricular/practice/s1/boilerplate/.gitignore .
mkdir -p .github/workflows
cp /ruta/a/extracurricular/practice/s1/boilerplate/.github/workflows/ci.yml .github/workflows/

# 3. Instalá el entorno y verificá los tests
uv sync
uv run pytest

# 4. Primer commit y subida a tu GitHub personal
git add .
git commit -m "chore: inicializar proyecto S1 desde boilerplate con layout src y CI"
git remote add origin git@github.com:tu-usuario/mi-consultorio.git
git branch -M main
git push -u origin main
```

### Opción B: Inicialización manual desde cero
Si preferís construir la estructura paso a paso siguiendo [`practice/s1/classes/S1-01.md`](../practice/s1/classes/S1-01.md):
```bash
mkdir mi-consultorio && cd mi-consultorio
git init
uv init . --package
uv add --dev pytest ruff
```

Estructura mínima esperada:
```text
mi-proyecto/
├── .gitignore
├── pyproject.toml
├── uv.lock
├── README.md
├── requirements.md               # Especificación del dominio e invariantes
├── .github/
│   └── workflows/
│       └── ci.yml                # CI automatizado con pytest
├── src/
│   └── <mi_paquete>/
│       └── __init__.py
└── tests/
    ├── __init__.py
    └── test_smoke.py
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
6. **Auditoría con el Tutor Socrático de IA (Opcional / 24/7):** Antes de fusionar tu rama, podés ingresar a la [Plataforma de Tutoría Socrática con IA](../tutoring/README.md#modalidad-2-tutoría-socrática-asistida-por-ia-247-saas-arancelado) e iniciar sesión con tu cuenta de GitHub. Al seleccionar tu repositorio y rama activa (`feature/...`), el agente inspeccionará tu diff, tu `requirements.md` y el estado de tus tests en GitHub Actions para orientar tu razonamiento y auditar tu entrega frente a la *Definition of Done*.
7. **Merge limpio a `main`:**
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
