# Starter Kit — Semestre 2: Consultorio Médico Persistente

Plantilla inicial de trabajo para los estudiantes de **Extracurricular S2 (Persistir y servir)**.

## Requisitos Previos

- Python 3.12 o superior.
- Gestor de paquetes [`uv`](https://docs.astral.sh/uv/).
- Docker y Docker Compose para el motor PostgreSQL.

## Puesta en Marcha Rápida (5 minutos)

### 1. Iniciar la Base de Datos PostgreSQL
Levantá el contenedor local con PostgreSQL 16:
```bash
docker compose up -d
```
Podés verificar que el motor esté listo ejecutando:
```bash
docker compose ps
```

### 2. Instalar dependencias con `uv`
Sincronizá el entorno virtual reproducible:
```bash
uv sync
```

### 3. Configuración de Variables de Entorno
Copiá el archivo de variables de entorno de ejemplo:
```bash
cp .env.example .env
```

### 4. Ejecutar Migraciones
Aplicá las migraciones de Django sobre la base de datos PostgreSQL:
```bash
uv run python manage.py migrate
```

### 5. Correr la Suite de Tests de Integración
Verificá que las pruebas contra la base de datos pasen limpiamente:
```bash
uv run pytest
```

### 6. Levantar el Backoffice de Administración
Creá un superusuario y ejecutá el servidor:
```bash
uv run python manage.py createsuperuser
uv run python manage.py runserver
```
Abrí `http://127.0.0.1:8000/admin/` en tu navegador.
