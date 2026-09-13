# Consultorio Médico — Extracurricular S1 Starter

Repositorio inicial del estudiante para el **Semestre 1 (Construir)** de [Extracurricular](https://github.com/fdomerlo/extracurricular).

## Inicio Rápido con `uv`

1. **Instalar dependencias y crear entorno virtual:**
   ```bash
   uv sync
   ```

2. **Ejecutar la suite de tests:**
   ```bash
   uv run pytest
   ```

3. **Verificar calidad de código:**
   ```bash
   uv run ruff check .
   ```

## Flujo de Trabajo por Ramas

- Desarrollá cada clase del currículum en una rama de feature dedicada:
  ```bash
  git checkout -b feature/s1-01-entorno
  git checkout -b feature/s1-04-testing-unitario
  ```
- Realizá commits atómicos y descriptivos.
- Subí tu rama (`git push origin feature/...`) para que la **Plataforma de Tutoría Socrática con IA** pueda inspeccionar tu diff y auditar tus tests de GitHub Actions.
