# Modelo de Proyecto del Estudiante

## Propósito

El proyecto es el vehículo mediante el cual el estudiante integra las
competencias del curriculum.

El curriculum define:

-   qué competencias debe desarrollar;
-   en qué semestre;
-   con qué nivel de profundidad;
-   qué evidencia debe producir.

El proyecto define:

-   qué problema intenta resolver;
-   para quién;
-   bajo qué restricciones;
-   qué decisiones debe tomar;
-   qué consecuencias tienen esas decisiones.

El proyecto puede ser propio o de referencia.

------------------------------------------------------------------------

## 1. Dos modalidades

### Proyecto propio

El estudiante propone un problema y desarrolla una solución.

Puede existir un cliente real, una organización, un usuario concreto o
simplemente una necesidad identificada por el estudiante.

### Proyecto de referencia

El estudiante que no dispone de un proyecto propio utiliza el proyecto
proporcionado por el repositorio.

El proyecto de referencia debe recorrer las mismas competencias y
milestones que un proyecto propio.

------------------------------------------------------------------------

## 2. Principio fundamental

> El curriculum es común. El contexto del proyecto puede ser diferente.

Dos estudiantes pueden estudiar exactamente las mismas competencias y
trabajar sobre sistemas completamente distintos.

Ejemplo:

``` text
S2 — Concurrencia

Alumno A
Sistema de turnos odontológicos
→ evitar double booking

Alumno B
Sistema de reservas deportivas
→ evitar doble reserva

Alumno C
E-commerce
→ evitar overselling

Reference Project
→ resolver el mismo problema en un dominio controlado
```

La competencia es la misma; la aplicación es contextual.

------------------------------------------------------------------------

## 3. Cliente

Cuando existe un cliente, su función es validar el problema y el
producto.

El cliente puede:

-   describir necesidades;
-   priorizar funcionalidades;
-   probar entregables;
-   proporcionar feedback;
-   aceptar o rechazar resultados.

El cliente no reemplaza al tutor técnico.

------------------------------------------------------------------------

## 4. Tutor

El tutor ayuda al estudiante a razonar.

El tutor puede:

-   cuestionar decisiones;
-   identificar riesgos;
-   proponer alternativas;
-   señalar conocimientos faltantes;
-   revisar entregables;
-   ayudar a definir milestones.

El tutor no debe convertirse en el desarrollador del proyecto.

Regla:

> El estudiante toma las decisiones y responde por ellas.

------------------------------------------------------------------------

## 5. Project Brief

Todo proyecto debe comenzar con un `brief.md`.

Debe responder:

-   ¿Qué problema se intenta resolver?
-   ¿Quiénes son los usuarios?
-   ¿Quién valida el resultado?
-   ¿Qué entra en el alcance?
-   ¿Qué queda explícitamente fuera?
-   ¿Qué restricciones existen?
-   ¿Cómo se define el éxito?
-   ¿Qué decisiones iniciales se proponen?
-   ¿Qué preguntas permanecen abiertas?

El brief no necesita contener una arquitectura definitiva.

------------------------------------------------------------------------

## 6. Evolución

El proyecto atraviesa los seis semestres:

``` text
S1  dominio
 ↓
S2  persistencia
 ↓
S3  aplicación
 ↓
S4  ingeniería y delivery
 ↓
S5  producción
 ↓
S6  observabilidad y evolución
```

No es obligatorio implementar todas las funcionalidades imaginables.

La complejidad debe crecer por necesidad, no por acumulación
tecnológica.

------------------------------------------------------------------------

## 7. Criterio de incorporación tecnológica

Antes de introducir una tecnología el estudiante debe poder responder:

1.  ¿Qué problema resuelve?
2.  ¿Por qué aparece ahora?
3.  ¿Qué alternativas existen?
4.  ¿Qué costo introduce?
5.  ¿Cómo sabremos que funcionó?

Si no existe una necesidad concreta, la tecnología no se incorpora.

------------------------------------------------------------------------

## 8. Decisiones

Las decisiones relevantes deben quedar registradas.

Formato recomendado:

``` text
docs/decisions/
├── ADR-001.md
├── ADR-002.md
└── ...
```

Cada decisión debe documentar:

-   contexto;
-   problema;
-   alternativas;
-   decisión;
-   consecuencias.

------------------------------------------------------------------------

## 9. Definition of Done del proyecto

Un milestone se considera terminado cuando:

-   el comportamiento solicitado funciona;
-   existen pruebas apropiadas;
-   el código es comprensible;
-   las decisiones relevantes están documentadas;
-   el sistema puede ser ejecutado por otra persona;
-   el estudiante puede explicar la implementación.

En etapas posteriores se agregan:

-   seguridad;
-   automatización;
-   deployment;
-   observabilidad;
-   recuperación.

------------------------------------------------------------------------

## 10. Proyecto como portfolio

El repositorio final debe permitir reconstruir la evolución del
estudiante.

Debe mostrar:

``` text
problema
→ decisiones
→ implementación
→ errores
→ refactorings
→ tests
→ deployments
→ incidentes
→ evolución
```

El objetivo no es ocultar los errores históricos, sino demostrar
capacidad de aprender y corregirlos.
