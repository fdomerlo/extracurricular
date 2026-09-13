# Evaluación Diagnóstica Inicial

Este documento constituye el instrumento de evaluación diagnóstica de **Extracurricular**.

Su propósito es conocer tu punto de partida técnico, tus hábitos de trabajo y tu razonamiento para determinar la ruta curricular más adecuada (nivelación previa, ingreso directo a S1 o aceleración).

---

## Instrucciones para el estudiante

- **Objetivo:** Queremos ver cómo pensás, cómo resolvés problemas y cómo verificás tu propio trabajo. La evaluación combina selección de opciones (para responder de forma ágil) con ejercicios prácticos de programación.
- **Tiempo sugerido:** Entre 45 y 60 minutos. Trabajá con calma y a tu ritmo.
- **Requisitos:** Una computadora con acceso a terminal, Python (3.10 o superior) y tu editor de código o IDE de preferencia.
- **Política sobre uso de IA y documentación:**
  - Podés consultar la documentación oficial o buscar sintaxis si lo necesitás.
  - Podés usar asistentes de IA para consultar conceptos, pero **todo el código entregado debe ser de tu autoría o auditado y comprendido por vos**.
- **Forma de realización:** Completá las opciones marcando con `[X]` la casilla correspondiente y escribí tu código en los bloques indicados.
- **Uso de este diagnóstico:**
  - *Si sos autodidacta:* Te sirve como autodiagnóstico para verificar que alcanzás el nivel mínimo operativo en las competencias bloqueantes definidas en [`competency-map.md`](competency-map.md) antes de comenzar S1.
  - *Si contás con un tutor o facilitador:* Entregale este archivo completado junto con tu script de código para que realice la devolución de tu perfil inicial.

---

# Parte 1 — Cuestionario Cualitativo y Conceptual

### Sección A: Trayectoria y Experiencia

1. **Completá la siguiente matriz marcando con una `X` tu nivel de experiencia en cada área:**

| Área / Tecnología | No la conozco | La estudié / hice cursos | La practiqué en ejercicios | La usé en un proyecto propio | La usé profesionalmente |
|---|:---:|:---:|:---:|:---:|:---:|
| Terminal / Línea de comandos (bash, zsh, powershell) | | | | | |
| Python (fundamentos: funciones, listas, diccionarios) | | | | | |
| Tipado / Type hints en Python | | | | | |
| Control de versiones con Git (commits, ramas) | | | | | |
| Manejo de errores y excepciones (`try / except`) | | | | | |
| Testing automatizado (`unittest`, `pytest` o aserciones) | | | | | |
| Bases de datos relacionales y SQL (`SELECT`, `JOIN`) | | | | | |
| Protocolo HTTP y desarrollo web básico | | | | | |
| Asistentes de IA para programar (ChatGPT, Copilot, Claude) | | | | | |

2. **Tu contexto formativo principal proviene de (marcar una opción con `[X]`):**
- [ ] Autodidacta (documentación oficial, libros, proyectos personales independientes)
- [ ] Cursos online o tutoriales guiados
- [ ] Carrera técnica o terciaria en desarrollo de software / informática
- [ ] Carrera universitaria de grado en Ciencias de la Computación, Informática o Sistemas
- [ ] Formación en otra ingeniería o ciencias duras (física, matemáticas, etc.)
- [ ] Reconversión laboral desde un área no vinculada a la tecnología

*(Opcional, 1 línea si querés aclarar carrera, año o bootcamp):*
> Detalle:

---

### Sección B: Hábitos de Trabajo y Resolución de Problemas

Marcá con `[X]` la opción que mejor refleje cómo actuás en cada situación:

1. **Cuando tu programa se rompe con un error que nunca viste:**
   - [ ] Pruebo modificar líneas o sintaxis al azar en mi código hasta que deje de fallar.
   - [ ] Copio y pego el error completo en Google o ChatGPT sin mirar el traceback.
   - [ ] Leo el traceback para ubicar el archivo y la línea de mi código, y agrego `print` o uso el debugger para inspeccionar los valores.
   - [ ] Aíslo el problema en un caso mínimo, formulo una hipótesis sobre la causa raíz y consulto la documentación o el test correspondiente.

2. **Para verificar que una función o script que escribiste realmente funciona:**
   - [ ] Lo ejecuto una vez con un dato normal; si no falla, lo doy por terminado.
   - [ ] Hago varias pruebas manuales cambiando valores en la consola para abarcar casos normales y casos límite (vacíos, None, extremos).
   - [ ] Escribo aserciones (`assert`) o una suite de tests con `pytest`/`unittest` que cubran casos válidos y de fallo.
   - [ ] Le pido a un asistente de IA que revise el código y confío en su confirmación.

3. **Si un tutorial que encontraste dice una cosa pero la documentación oficial de la librería dice otra:**
   - [ ] Sigo el tutorial porque generalmente es más simple y práctico de entender.
   - [ ] Pruebo ambos enfoques en mi código y me quedo con el primero que compile o corra sin error.
   - [ ] Priorizo la documentación oficial correspondiente a la versión que tengo instalada, ya que los tutoriales suelen desactualizarse.
   - [ ] Consulto a una IA cuál de los dos recursos tiene razón y sigo su indicación.

4. **Tu criterio habitual frente a los asistentes de Inteligencia Artificial:**
   - [ ] No utilizo herramientas de IA para programar.
   - [ ] Las uso frecuentemente y suelo aceptar sus sugerencias de código directamente para ir más rápido.
   - [ ] Las uso como generador de borradores o ideas, pero audito cada línea y solo conservo lo que comprendo y puedo justificar por mi cuenta.
   - [ ] Las uso como interlocutor para comparar alternativas o entender conceptos teóricos, pero escribo la implementación personalmente.

---

### Sección C: Razonamiento Conceptual

#### Caso C1 — Flujo y Mutabilidad
Observá el siguiente fragmento de código Python sin ejecutarlo en la terminal:

```python
def agregar_item(item, lista=[]):
    lista.append(item)
    return lista

resultado_1 = agregar_item("A")
resultado_2 = agregar_item("B")

print("1:", resultado_1)
print("2:", resultado_2)
```

1. **¿Qué salida esperás que imprima en pantalla? (marcar con `[X]`):**
   - [ ] `1: ['A']` y `2: ['B']`
   - [ ] `1: ['A']` y `2: ['A', 'B']`
   - [ ] Error de ejecución en consola (`TypeError`)
   - [ ] `1: ['A', 'B']` y `2: ['A', 'B']`

2. **¿Por qué ocurre ese comportamiento y cuál es el diseño correcto? (marcar con `[X]`):**
   - [ ] En Python las listas se limpian solas al salir de la función si no se asignan a una variable global.
   - [ ] El argumento por defecto mutable se evalúa una sola vez cuando se define la función y se comparte entre todas las llamadas; la solución idiomática es definir `lista=None` e inicializar `if lista is None: lista = []` dentro de la función.
   - [ ] Es un bug de la versión de Python que ocurre al usar `.append()`; la solución es hacer `lista = lista + [item]`.
   - [ ] Es una restricción de alcance (`scope`) que se soluciona agregando la sentencia `global lista`.

---

#### Caso C2 — Manejo de Situaciones Excepcionales
Imaginá una función que busca un paciente en una lista de registros por su número de identificación (`dni`):

```python
def buscar_paciente(dni, pacientes):
    for p in pacientes:
        if p["dni"] == dni:
            return p
    return None
```

1. **¿Cuándo conviene retornar `None` (o valor centinela) y cuándo lanzar una excepción? (marcar con `[X]`):**
   - [ ] Conviene retornar `None` cuando que el elemento no exista sea un resultado esperable dentro del flujo normal (búsqueda consultiva); conviene lanzar excepción cuando la ausencia del paciente viole una precondición obligatoria para continuar la operación.
   - [ ] Conviene siempre retornar `None`, porque lanzar excepciones es costoso y se considera mala práctica en cualquier contexto.
   - [ ] Conviene siempre lanzar excepción, porque retornar `None` está desaconsejado en Python moderno.

2. **¿Qué ventaja aporta lanzar una excepción propia (`PacienteNoEncontradoError`) en lugar de `ValueError` o `Exception`? (marcar con `[X]`):**
   - [ ] Ninguna; agrega clases redundantes que no alteran el funcionamiento.
   - [ ] Permite capturarla de forma selectiva (`except PacienteNoEncontradoError:`) en capas superiores sin atrapar accidentalmente otros fallos, dotando de semántica clara al dominio.
   - [ ] Sirve exclusivamente para que el mensaje aparezca destacado en la consola.

---

# Parte 2 — Prueba Práctica de Programación

En esta parte vas a resolver un problema concreto en Python.

### Contexto: "Gestión de reservas de una clínica"
Un profesional atiende consultas con turnos de 30 minutos. Cada reserva se representa con un diccionario con la siguiente estructura:

```python
reserva_ejemplo = {
    "id": 1,
    "paciente": "Ana Gómez",
    "hora_inicio": 900,   # 09:00 hs representada como entero militar
    "hora_fin": 930,      # 09:30 hs
    "estado": "confirmada" # "confirmada" o "cancelada"
}
```

---

### Task 1 — Entorno y Ejecución (Herramientas)

1. En tu máquina, creá una carpeta llamada `diagnostico_tu_apellido`.
2. Verificá la versión de Python instalada ejecutando en la terminal `python --version` (o `python3 --version`).
3. Creá un archivo `main.py` dentro de esa carpeta con un script que imprima:
   `"Entorno listo para evaluación diagnóstica"`.
4. Ejecutalo desde la terminal.

*Pegá acá el comando ejecutado y la salida obtenida:*
```text
[Pegá acá comando y salida de la terminal]
```

---

### Task 2 — Programación y Lógica de Negocio

Implementá una función `calcular_horas_ocupadas(reservas)` que reciba una lista de reservas y devuelva:
- La cantidad total de turnos **confirmados**.
- La lista de nombres de pacientes con turnos confirmados ordenados alfabéticamente.
- Las reservas canceladas deben ser ignoradas.

*Escribí tu solución a continuación:*

```python
# Task 2: Implementación
def calcular_horas_ocupadas(reservas):
    # Tu código acá
    pass
```

---

### Task 3 — Debugging Sistemático

Un colega intentó escribir una función para detectar si una nueva reserva se solapa en horario con alguna reserva ya existente en la agenda:

```python
def hay_solapamiento(nueva_reserva, reservas_existentes):
    """
    Retorna True si nueva_reserva se superpone con alguna reserva confirmada.
    Dos turnos se solapan si uno empieza antes de que el otro termine
    y termina después de que el otro empiece.
    """
    for r in reservas_existentes:
        if r["estado"] == "confirmada":
            # Condición que escribió tu colega:
            if nueva_reserva["hora_inicio"] >= r["hora_inicio"] and nueva_reserva["hora_inicio"] < r["hora_fin"]:
                return True
            elif nueva_reserva["hora_fin"] > r["hora_inicio"] and nueva_reserva["hora_fin"] <= r["hora_fin"]:
                return True
    return False
```

Al probar la función, reportan dos fallos:
1. Si entra una reserva larga que engloba completamente a una existente (por ejemplo, nueva de 08:00 a 11:00 y existente de 09:00 a 09:30), la función devuelve `False` (no detecta solapamiento).
2. Si un turno nuevo empieza exactamente a la misma hora en que termina el anterior (ejemplo: existente 09:00 a 09:30 y nuevo 09:30 a 10:00), a veces produce resultados ambiguos.

1. **¿Cuál es la causa raíz del fallo en la condición de tu colega? (marcar con `[X]`):**
   - [ ] No convirtió los números enteros a objetos `datetime.time`.
   - [ ] Solo evalúa si los extremos de la nueva reserva caen dentro de la existente; no detecta cuando la nueva reserva contiene por completo a la existente (`nueva.inicio <= exist.inicio` y `nueva.fin >= exist.fin`), y además los operadores `>=` y `<=` generan falsos positivos en turnos contiguos.
   - [ ] La función itera con un ciclo `for` en lugar de usar un diccionario indexado.
   - [ ] En Python el bloque `elif` descarta las evaluaciones del bloque `if`.

2. **Escribí la versión corregida de la función `hay_solapamiento` (limpia, robusta y libre de errores):**

```python
# Task 3: Código corregido
def hay_solapamiento(nueva_reserva, reservas_existentes):
    # Tu código corregido acá
    pass
```

---

### Task 4 — Evolución y Caso de Prueba

La clínica agrega una nueva regla de negocio:
> *"No se pueden agendar reservas fuera del horario de atención de la clínica (de 08:00 a 18:00 hs — es decir, `hora_inicio >= 800` y `hora_fin <= 1800`), ni reservas donde la hora de inicio sea mayor o igual a la hora de fin."*

1. Implementá una función `validar_reserva(reserva)` que verifique esta regla y devuelva un booleano (`True` / `False`) o lance un error según tu diseño.
2. Escribí al menos 3 pruebas simples (usando `assert` o `pytest`) que comprueben:
   - Un caso válido dentro del horario.
   - Un caso inválido por estar fuera del horario de atención.
   - Un caso inválido donde `hora_inicio >= hora_fin`.

```python
# Task 4: Código y pruebas con assert
def validar_reserva(reserva):
    # Tu código acá
    pass

# Pruebas de verificación:
def test_validar_reserva():
    # Tus aserciones acá
    pass
```

---

### Task 5 — Verificación y Defensa

Marcá con `[X]` las opciones que describan cómo resolviste la evaluación:

1. **Enfoque lógico aplicado en la condición de Task 3 (marcar una opción con `[X]`):**
   - [ ] Condición directa de intersección: `nueva.hora_inicio < r.hora_fin and nueva.hora_fin > r.hora_inicio`
   - [ ] Condición por negación de no-solapamiento: `not (nueva.hora_fin <= r.hora_inicio or nueva.hora_inicio >= r.hora_fin)`
   - [ ] Estructura extendida con múltiples `if/elif` evaluando cada caso borde por separado
   - [ ] Otra formulación matemática equivalente

2. **Estrategia principal de verificación que utilizaste durante la prueba (marcar con `[X]`):**
   - [ ] Ejecución manual en consola observando las salidas a ojo
   - [ ] Aserciones automatizadas (`assert` o `pytest`) con casos representativos y casos límite
   - [ ] Depuración interactiva paso a paso con debugger (pdb o IDE)
   - [ ] Confié en el razonamiento lógico sin correr pruebas exhaustivas

3. **Apoyo externo o asistencia de IA durante la prueba (marcar con `[X]`):**
   - [ ] Ninguno: resuelto de forma 100% autónoma con conocimientos propios
   - [ ] Consulta puntual de sintaxis en documentación oficial de Python o internet
   - [ ] Consulta con asistente de IA para clarificar conceptos o alternativas, auditando y comprendiendo el resultado final
   - [ ] Generación íntegra de código mediante IA

*(Opcional, 1 línea si utilizaste IA o documentación y querés aclarar qué consultaste):*
> Detalle:

---

### Fin de la evaluación
¡Muchas gracias por completar la evaluación diagnóstica! Guardá tus respuestas y envialas para su revisión pedagógica.
