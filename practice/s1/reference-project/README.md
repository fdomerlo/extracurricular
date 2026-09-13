# Reference Project — S1

## Propósito

Proyecto de referencia para autodidactas que no tienen un proyecto propio.

## Dominio

Sistema de gestión de turnos.

En S1 se construye únicamente un **motor de dominio ejecutable desde CLI**.

## Entidades y Reglas de Negocio

El modelo formal y sus invariantes se detallan en [`requirements.md`](requirements.md) y la asignación por clase en [`project-task-map.md`](project-task-map.md):

- **Patient:** Datos del paciente (nombre, apellido, identificador, teléfono).
- **Professional:** Especialidad y agenda disponible.
- **Appointment:** El turno médico con sus transiciones de estado: `Creado` → `Confirmado` → `Atendido` (o `Cancelado`).
  - Invariante 1: No se puede confirmar un turno cancelado.
  - Invariante 2: No se puede cancelar un turno ya atendido.
  - Invariante 3: No pueden existir solapamientos de turnos confirmados para el mismo profesional.

---

## Guía de Inicialización Paso a Paso

Para comenzar a construir este proyecto en tu propio repositorio:

### 1. Inicializar tu repositorio local
```bash
# Creá la carpeta de tu proyecto (fuera de extracurricular)
mkdir consultorio-s1 && cd consultorio-s1

# Inicializá git y el paquete con uv
git init
uv init . --package

# Agregá pytest como dependencia de desarrollo
uv add --dev pytest
```

### 2. Estructura de carpetas recomendada
Al llegar a las clases de dominio (S1-04/S1-05), tu repositorio debería verse así:
```text
consultorio-s1/
├── pyproject.toml
├── uv.lock
├── .gitignore
├── README.md
├── src/
│   └── consultorio/
│       ├── __init__.py
│       ├── domain/
│       │   ├── __init__.py
│       │   ├── entities.py       # Patient, Professional, Appointment
│       │   ├── value_objects.py  # Slot, AppointmentStatus
│       │   └── exceptions.py     # AppointmentCancelledError, etc.
│       └── cli/
│           └── main.py           # CLI ejecutable de S1-10
└── tests/
    ├── __init__.py
    └── test_appointments.py      # Tests unitarios exhaustivos de S1-05
```

### 3. Ejecutar los tests
```bash
# Correr la suite de tests en memoria
uv run pytest -v

# Verificar con linters (opcional pero recomendado)
uv run ruff check .
```

*Recordá: En S1 no se utiliza base de datos ni frameworks web. Toda la lógica vive en memoria y se valida con tests unitarios.*
