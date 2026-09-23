# Semester 02 — Persistir y servir

Implementación canónica del segundo semestre del currículum.

## Objetivo

Comprender la persistencia relacional a fondo y exponer el sistema desarrollado en S1 mediante una interfaz de acceso controlada y autenticada.

El semestre utiliza **PostgreSQL 16+**, **SQL estándar (DDL/DML)**, **Django 5.x (ORM y Admin)**, **pytest-django** para testing de integración contra base real, y el proyecto longitudinal del estudiante como contexto continuo de evolución.

## Resultado esperado

Al finalizar S2 el estudiante debe poder:

- modelar un esquema relacional con tipos de datos estrictos, claves primarias UUID, claves foráneas y restricciones `CHECK`;
- escribir consultas complejas a mano con `JOIN`, agregaciones y CTEs sin depender del ORM;
- leer e interpretar planes de ejecución con `EXPLAIN ANALYZE` y diseñar índices compuestos con criterio de selectividad;
- explicar las propiedades ACID y resolver condiciones de carrera concurrentes mediante transacciones y bloqueos;
- mapear el dominio en modelos de ORM y gestionar la evolución del esquema mediante migraciones versionadas y auditables;
- diagnosticar y erradicar el problema N+1 utilizando `select_related` y `prefetch_related`;
- configurar un backoffice operativo en Django Admin con filtros, búsquedas y restricciones de acceso por rol (RBAC);
- escribir tests de integración reproducibles contra una base PostgreSQL real;
- automatizar respaldos (`pg_dump`), restauraciones (`pg_restore`) y verificar la consistencia de datos en simulacros de recuperación;
- auditar críticamente código SQL y ORM asistido por IA, garantizando que ninguna línea entre al repositorio sin verificación humana.

## Duración

22 semanas lectivas (`curriculum/study-plan.md` §6):
- Semanas 1 a 15: 11 clases de contenido con 3 semanas intermedias de consolidación técnica (semanas 7, 9 y 13).
- Semanas 16 a 22: recuperación, 2 semanas de integración, entrega del milestone `M-S2`, defensa técnica oral, buffer y retrospectiva.
El detalle cronológico se encuentra en [`schedule.md`](schedule.md).

## Clases

**11 clases canónicas**, listadas en [`class-catalog.md`](class-catalog.md). El contenido completo vive en [`classes/`](classes/) y constituye la fuente de verdad.

## Proyecto

El estudiante continúa desarrollando el mismo sistema iniciado en S1 (sea su proyecto propio o el Reference Project del consultorio médico), transformando las entidades en memoria en una aplicación persistente, transaccional y administrable.

## Regla del semestre

> **Primero el fundamento, después la abstracción.** Escribimos y entendemos SQL a mano antes de usar el ORM. Gestionamos la concurrencia en la base de datos antes de exponer interfaces concurrentes.
