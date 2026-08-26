# Reference Project — Requirements S1

## Functional requirements

### Appointment

Permitir:

- crear;
- confirmar;
- cancelar;
- marcar como atendido.

## Invariants

- un turno no puede tener dos estados;
- no puede confirmarse uno cancelado;
- no puede cancelarse uno atendido;
- fecha/hora debe ser válida.

## Non-goals

En S1 no se requiere:

- base de datos;
- autenticación;
- interfaz web;
- API;
- Docker;
- deployment;
- concurrencia real.
