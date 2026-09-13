# Especificación de Requerimientos: Consultorio Médico (S1)

## 1. Alcance
Desarrollo de un motor de dominio puro en memoria para la gestión de turnos y agendas profesionales.

## 2. Entidades Principales
- **Patient:** Identificador único, nombre, apellido, teléfono y correo electrónico.
- **Professional:** Identificador único, nombre, especialidad médica y horario de atención.
- **Appointment (Turno):** Paciente, profesional, fecha/hora y estado (`PROGRAMADO`, `CONFIRMADO`, `ATENDIDO`, `CANCELADO`).

## 3. Invariantes y Reglas de Negocio
1. **No retroactividad:** No se pueden agendar ni confirmar turnos en fechas/horas pasadas.
2. **No superposición:** Un profesional no puede tener dos turnos confirmados en el mismo intervalo de tiempo para el mismo profesional.
3. **Política de cancelación:**
   - La cancelación con 24 horas o más de anticipación se realiza sin penalidad.
   - La cancelación con menos de 24 horas registra penalidad en el historial.
4. **Inmutabilidad de estado final:** Un turno en estado `ATENDIDO` o `CANCELADO` no puede cambiar de estado ni reprogramarse.
