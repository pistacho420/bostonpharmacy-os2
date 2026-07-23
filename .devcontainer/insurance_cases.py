# ==========================================================
# BostonPharmacy-OS v2026
# Banco de Casos - Insurance Billing
# 10 Casos de Práctica
# ==========================================================


casos_insurance = [

{
"titulo":"Caso 1 - Prior Authorization Required",

"rechazo":
"Prior Authorization Required",

"caso":
"El seguro rechaza Lipitor 20mg porque necesita autorización del médico.",

"pregunta":
"¿Cuál es el siguiente paso correcto?",

"opciones":[
"Cambiar el medicamento sin avisar al médico.",
"Informar al paciente y contactar al consultorio médico para solicitar autorización.",
"Cobrar el precio completo automáticamente."
],

"respuesta":
"Informar al paciente y contactar al consultorio médico para solicitar autorización.",

"explicacion":
"El técnico debe seguir el proceso del seguro y comunicar al médico para obtener la autorización previa."
},


{
"titulo":"Caso 2 - Refill Too Soon",

"rechazo":
"Refill Too Soon",

"caso":
"El paciente intenta recoger su medicamento 10 días antes de la fecha permitida.",

"pregunta":
"¿Qué significa este mensaje?",

"opciones":[
"El seguro no cubre el medicamento.",
"El paciente está intentando surtir demasiado pronto.",
"La farmacia tiene problemas con el sistema."
],

"respuesta":
"El paciente está intentando surtir demasiado pronto.",

"explicacion":
"El seguro bloquea los surtidos antes del tiempo establecido."
},


{
"titulo":"Caso 3 - Drug Not Covered",

"rechazo":
"Drug Not Covered",

"caso":
"El seguro rechaza un medicamento de marca porque no está en el formulario.",

"pregunta":
"¿Qué puede hacer la farmacia?",

"opciones":[
"Enviar solicitud de alternativa o contactar al médico.",
"Eliminar al paciente del sistema.",
"Cambiar la dosis automáticamente."
],

"respuesta":
"Enviar solicitud de alternativa o contactar al médico.",

"explicacion":
"El medicamento debe ser evaluado por el médico o seguro."
},


{
"titulo":"Caso 4 - Patient Not Found",

"rechazo":
"Patient Not Found",

"caso":
"El seguro no reconoce la información del paciente.",

"pregunta":
"¿Qué información se debe verificar?",

"opciones":[
"Nombre, fecha de nacimiento y Member ID.",
"Color favorito del paciente.",
"Dirección del médico solamente."
],

"respuesta":
"Nombre, fecha de nacimiento y Member ID.",

"explicacion":
"Los datos demográficos deben coincidir con la información del seguro."
},


{
"titulo":"Caso 5 - Invalid Member ID",

"rechazo":
"Invalid Member ID",

"caso":
"La tarjeta del seguro tiene un número incorrecto.",

"pregunta":
"¿Qué debe hacer el técnico?",

"opciones":[
"Verificar la tarjeta y corregir la información.",
"Inventar un número nuevo.",
"Eliminar el seguro."
],

"respuesta":
"Verificar la tarjeta y corregir la información.",

"explicacion":
"Un Member ID incorrecto causa rechazo automático."
},


{
"titulo":"Caso 6 - Quantity Limit",

"rechazo":
"Quantity Limit Exceeded",

"caso":
"El seguro permite solamente 30 tabletas pero la receta indica 90.",

"pregunta":
"¿Cuál es el procedimiento?",

"opciones":[
"Contactar al médico o solicitar excepción.",
"Entregar las 90 sin autorización.",
"Cancelar la receta."
],

"respuesta":
"Contactar al médico o solicitar excepción.",

"explicacion":
"El seguro establece límites de cantidad."
},


{
"titulo":"Caso 7 - Duplicate Claim",

"rechazo":
"Duplicate Claim",

"caso":
"El sistema indica que la reclamación ya fue procesada.",

"pregunta":
"¿Qué se debe revisar?",

"opciones":[
"Confirmar si la receta ya fue facturada.",
"Cobrar dos veces al paciente.",
"Crear otro paciente."
],

"respuesta":
"Confirmar si la receta ya fue facturada.",

"explicacion":
"Evita cobros duplicados y errores de facturación."
},


{
"titulo":"Caso 8 - Step Therapy",

"rechazo":
"Step Therapy Required",

"caso":
"El seguro requiere probar primero un medicamento diferente.",

"pregunta":
"¿Qué significa?",

"opciones":[
"El paciente debe usar otro medicamento antes.",
"El seguro pagará cualquier medicamento.",
"La receta está falsificada."
],

"respuesta":
"El paciente debe usar otro medicamento antes.",

"explicacion":
"Algunos seguros requieren tratamientos escalonados."
},


{
"titulo":"Caso 9 - Coordination of Benefits",

"rechazo":
"COB Required",

"caso":
"El paciente tiene dos seguros activos.",

"pregunta":
"¿Qué debe determinarse?",

"opciones":[
"Cuál seguro es primario y cuál secundario.",
"Eliminar ambos seguros.",
"Cobrar siempre efectivo."
],

"respuesta":
"Cuál seguro es primario y cuál secundario.",

"explicacion":
"El orden correcto de seguros evita rechazos."
},


{
"titulo":"Caso 10 - DUR Reject",

"rechazo":
"DUR Reject",

"caso":
"El seguro alerta una interacción medicamento-medicamento.",

"pregunta":
"¿Qué debe hacer el técnico?",

"opciones":[
"Notificar al farmacéutico para evaluación.",
"Ignorar la alerta.",
"Cambiar el medicamento."
],

"respuesta":
"Notificar al farmacéutico para evaluación.",

"explicacion":
"Las decisiones clínicas corresponden al farmacéutico."
}

]
