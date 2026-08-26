# Project Milestones

## Propósito

Los milestones conectan el curriculum con el proyecto concreto del
estudiante.

El semestre define las competencias.

El milestone define cómo esas competencias se manifiestan en el
proyecto.

------------------------------------------------------------------------

# S1 --- Construir

## Objetivo

Obtener una primera versión funcional del dominio sin depender de
infraestructura compleja.

### Debe demostrar

-   modelo de dominio;
-   reglas de negocio;
-   estados;
-   manejo de errores;
-   tests;
-   debugging;
-   Git;
-   entorno reproducible.

### Entregables

``` text
project/
├── src/
├── tests/
├── README.md
└── pyproject.toml
```

### Evidencia

-   demo;
-   tests;
-   explicación del dominio;
-   historial Git.

------------------------------------------------------------------------

# S2 --- Persistir

## Objetivo

Convertir el sistema en una aplicación que mantenga correctamente su
estado.

### Debe demostrar

-   modelo relacional;
-   SQL;
-   PostgreSQL;
-   ORM;
-   migraciones;
-   transacciones;
-   concurrencia;
-   backup y restore.

### Evidencia especial

Debe existir al menos un escenario de concurrencia reproducible.

Ejemplo:

``` text
dos operaciones simultáneas
        ↓
estado compartido
        ↓
riesgo de inconsistencia
        ↓
solución
        ↓
test
```

------------------------------------------------------------------------

# S3 --- Aplicar

## Objetivo

Exponer el sistema mediante una aplicación web.

### Debe demostrar

-   HTTP;
-   HTML/CSS;
-   JavaScript práctico;
-   Django;
-   HTMX;
-   API cuando corresponda;
-   autenticación;
-   autorización;
-   seguridad web.

### Evidencia

-   aplicación funcional;
-   usuarios;
-   permisos;
-   tests;
-   documentación de API cuando exista.

------------------------------------------------------------------------

# S4 --- Ingeniar

## Objetivo

Convertir la aplicación en software reproducible, testeable y
entregable.

### Debe demostrar

-   arquitectura;
-   refactoring;
-   testing por niveles;
-   Docker;
-   CI;
-   CD;
-   quality gates;
-   seguridad del pipeline.

### Evidencia

``` text
commit
  ↓
CI
  ├── lint
  ├── tests
  ├── type checking
  └── security checks
        ↓
      build
        ↓
    deployment
```

------------------------------------------------------------------------

# S5 --- Operar

## Objetivo

Ejecutar el sistema fuera del entorno de desarrollo.

### Debe demostrar

-   Linux;
-   redes;
-   reverse proxy;
-   HTTPS;
-   workers;
-   queues;
-   Redis;
-   caching;
-   performance;
-   deployment;
-   rollback.

### Evidencia

-   sistema desplegado;
-   procedimiento de deployment;
-   procedimiento de rollback;
-   diagnóstico de al menos un fallo;
-   métricas de performance.

------------------------------------------------------------------------

# S6 --- Evolucionar

## Objetivo

Demostrar capacidad de trabajar sobre un sistema real y evolucionarlo.

### Debe demostrar

-   logging estructurado;
-   métricas;
-   tracing;
-   observabilidad;
-   SLI/SLO básicos;
-   incident response;
-   sistemas distribuidos a nivel práctico;
-   IA asistida;
-   lectura de código ajeno;
-   documentación;
-   defensa técnica.

### Evidencia

-   dashboard;
-   incidente simulado o real;
-   postmortem;
-   arquitectura final;
-   revisión de decisiones;
-   portfolio;
-   defensa.

------------------------------------------------------------------------

# Regla de los milestones

Un milestone no se completa simplemente agregando funcionalidades.

Debe demostrar las competencias correspondientes al semestre.

El proyecto puede ser diferente.

La evidencia requerida no.
