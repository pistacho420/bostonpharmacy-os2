# ==========================================================
# BostonPharmacy-OS v2026
# Banco de Casos - Controlled Substances (MassPAT)
# 10 Casos de Práctica
# ==========================================================


casos_masspat = [

{
"titulo":"Caso 1 - Oxycodone Schedule II",

"caso":
"Paciente presenta receta de Oxycodone 10mg (Schedule II).",

"pregunta":
"¿Qué debe hacerse antes de dispensar?",

"opciones":[
"Dispensar inmediatamente.",
"Consultar MassPAT y revisar historial del paciente.",
"Enviar al paciente a otra farmacia."
],

"respuesta":
"Consultar MassPAT y revisar historial del paciente.",

"explicacion":
"MassPAT ayuda a identificar duplicidad, uso excesivo o múltiples prescriptores."
},


{
"titulo":"Caso 2 - Tramadol Multiple Pharmacies",

"caso":
"Paciente solicita refill de Tramadol. MassPAT muestra que obtuvo el mismo medicamento hace 5 días en otra farmacia.",

"pregunta":
"¿Cuál es la acción correcta?",

"opciones":[
"Llenar la receta sin preguntar.",
"Informar al farmacéutico y detener el proceso para evaluación.",
"Eliminar el historial del paciente."
],

"respuesta":
"Informar al farmacéutico y detener el proceso para evaluación.",

"explicacion":
"El patrón puede indicar abuso o duplicidad."
},


{
"titulo":"Caso 3 - Adderall XR",

"caso":
"Paciente nuevo trae receta de Adderall XR 20mg.",

"pregunta":
"¿Por qué revisar MassPAT?",

"opciones":[
"Para revisar historial de sustancias controladas.",
"Para calcular el copago.",
"Para cambiar la dosis."
],

"respuesta":
"Para revisar historial de sustancias controladas.",

"explicacion":
"Adderall es una sustancia controlada Schedule II."
},


{
"titulo":"Caso 4 - Benzodiazepine Alert",

"caso":
"MassPAT muestra que un paciente recibe Lorazepam y otros medicamentos de riesgo.",

"pregunta":
"¿Qué debe hacer el técnico?",

"opciones":[
"Informar al farmacéutico.",
"Ignorar la alerta.",
"Cancelar automáticamente la receta."
],

"respuesta":
"Informar al farmacéutico.",

"explicacion":
"El farmacéutico evalúa riesgos clínicos."
},


{
"titulo":"Caso 5 - Prescripción Telefónica",

"caso":
"Un médico quiere dictar una receta controlada por teléfono.",

"pregunta":
"¿Qué debe verificarse?",

"opciones":[
"Que cumpla las normas de prescripción permitidas.",
"Aceptarla siempre.",
"El técnico puede crear la receta."
],

"respuesta":
"Que cumpla las normas de prescripción permitidas.",

"explicacion":
"Los medicamentos controlados tienen reglas estrictas."
},


{
"titulo":"Caso 6 - Historial Vacío",

"caso":
"MassPAT no muestra historial previo del paciente.",

"pregunta":
"¿Qué significa?",

"opciones":[
"No hay registros encontrados en el sistema.",
"La receta es falsa automáticamente.",
"El paciente está bloqueado."
],

"respuesta":
"No hay registros encontrados en el sistema.",

"explicacion":
"Debe verificarse identidad y continuar según protocolo."
},


{
"titulo":"Caso 7 - Privacidad MassPAT",

"caso":
"Un paciente solicita una copia del reporte MassPAT de otra persona.",

"pregunta":
"¿Está permitido?",

"opciones":[
"No, la información es confidencial.",
"Sí, si paga una tarifa.",
"Sí, cualquier persona puede verla."
],

"respuesta":
"No, la información es confidencial.",

"explicacion":
"Los datos están protegidos por leyes de privacidad."
},


{
"titulo":"Caso 8 - Fentanyl Patch",

"caso":
"Se procesa una receta de Fentanyl Patch.",

"pregunta":
"¿Qué debe verificarse?",

"opciones":[
"Cumplimiento y registro de sustancia controlada.",
"Solo el precio.",
"Solo el color del medicamento."
],

"respuesta":
"Cumplimiento y registro de sustancia controlada.",

"explicacion":
"Fentanyl requiere controles estrictos."
},


{
"titulo":"Caso 9 - Sistema MassPAT Caído",

"caso":
"MassPAT presenta problemas técnicos.",

"pregunta":
"¿Qué debe hacer la farmacia?",

"opciones":[
"Seguir protocolo de contingencia y consultar al farmacéutico.",
"Ignorar siempre la verificación.",
"Entregar todos los medicamentos controlados."
],

"respuesta":
"Seguir protocolo de contingencia y consultar al farmacéutico.",

"explicacion":
"Los problemas técnicos no eliminan la responsabilidad legal."
},


{
"titulo":"Caso 10 - Doctor Shopping",

"caso":
"MassPAT muestra tres médicos diferentes recetando opioides al mismo paciente.",

"pregunta":
"¿Cómo se llama esta señal de alerta?",

"opciones":[
"Doctor Shopping.",
"Inventario alto.",
"Seguro primario."
],

"respuesta":
"Doctor Shopping.",

"explicacion":
"Es una conducta que los sistemas PDMP buscan detectar."
}

]
