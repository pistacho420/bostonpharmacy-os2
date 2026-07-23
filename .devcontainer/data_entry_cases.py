# ==========================================================
# BostonPharmacy-OS v2026
# Banco de Casos - Data Entry & E-Prescribing
# 10 Casos de Práctica
# ==========================================================


casos_data_entry = [

{
"titulo":"Caso 1 - Amoxicillin",
"paciente":"John Smith",
"dob":"11/14/1982",
"doctor":"Dr. Elizabeth Smith",
"npi":"1234567890",

"medicamento":"Amoxicillin 500mg capsules",

"sig":"Take 1 capsule by mouth three times daily for 10 days",

"cantidad":30,

"pregunta":
"¿Cuál es el Days Supply correcto?",

"opciones":[
"5 días",
"10 días",
"15 días",
"30 días"
],

"respuesta":
"10 días",

"explicacion":
"30 cápsulas ÷ 3 cápsulas diarias = 10 días."
},


{
"titulo":"Caso 2 - Metformin",

"paciente":"Sarah Johnson",

"dob":"03/21/1978",

"doctor":"Dr. Michael Brown",

"npi":"4567891230",

"medicamento":
"Metformin 500mg tablet",

"sig":
"Take 1 tablet by mouth twice daily",

"cantidad":60,


"pregunta":
"¿Cuál es el suministro aproximado?",

"opciones":[
"15 días",
"30 días",
"60 días",
"90 días"
],

"respuesta":
"30 días",

"explicacion":
"60 tabletas tomando 2 al día equivalen a 30 días."
},



{
"titulo":"Caso 3 - Lisinopril",

"paciente":"Robert Davis",

"dob":"08/10/1965",

"doctor":"Dr. Kevin Miller",

"npi":"7894561230",

"medicamento":
"Lisinopril 10mg",

"sig":
"Take 1 tablet daily",

"cantidad":90,


"pregunta":
"¿Cuál es el Days Supply?",

"opciones":[
"30 días",
"60 días",
"90 días",
"120 días"
],

"respuesta":
"90 días",

"explicacion":
"Una tableta diaria con 90 tabletas equivale a 90 días."
},



{
"titulo":"Caso 4 - Atorvastatin",

"paciente":"Linda Wilson",

"dob":"01/15/1970",

"doctor":"Dr. Anderson",

"npi":"555666777",

"medicamento":
"Atorvastatin 20mg",

"sig":
"Take 1 tablet at bedtime",

"cantidad":30,


"pregunta":
"¿Cuántos días cubre?",

"opciones":[
"15 días",
"30 días",
"60 días",
"90 días"
],

"respuesta":
"30 días",

"explicacion":
"Una tableta diaria = 30 días."
},



{
"titulo":"Caso 5 - Levothyroxine",

"paciente":"Maria Garcia",

"dob":"09/09/1980",

"doctor":"Dr. Thomas Lee",

"npi":"888999111",

"medicamento":
"Levothyroxine 50mcg",

"sig":
"Take 1 tablet every morning",

"cantidad":30,


"pregunta":
"¿Qué frecuencia indica el SIG?",

"opciones":[
"Dos veces al día",
"Una vez al día",
"Cada 12 horas",
"Al acostarse"
],

"respuesta":
"Una vez al día",

"explicacion":
"Every morning significa una dosis diaria."
},



{
"titulo":"Caso 6 - Albuterol",

"paciente":"James White",

"dob":"06/11/1992",

"doctor":"Dr. Clark",

"npi":"444555666",

"medicamento":
"Albuterol inhaler",

"sig":
"Use 2 puffs every 4-6 hours as needed",

"cantidad":1,


"pregunta":
"¿Qué significa PRN?",

"opciones":[
"Después de comer",
"Según necesidad",
"Antes de dormir",
"Cada día"
],

"respuesta":
"Según necesidad",

"explicacion":
"PRN significa pro re nata o cuando sea necesario."
},



{
"titulo":"Caso 7 - Omeprazole",

"paciente":"Carlos Martinez",

"dob":"12/02/1988",

"doctor":"Dr. Adams",

"npi":"222333444",

"medicamento":
"Omeprazole 20mg",

"sig":
"Take one capsule before breakfast",

"cantidad":30,


"pregunta":
"¿Cuándo toma el paciente el medicamento?",

"opciones":[
"Después de cenar",
"Antes del desayuno",
"Al dormir",
"Después del almuerzo"
],

"respuesta":
"Antes del desayuno",

"explicacion":
"Before breakfast indica antes del desayuno."
},



{
"titulo":"Caso 8 - Prednisone",

"paciente":"Kevin Brown",

"dob":"04/20/1975",

"doctor":"Dr. Wilson",

"npi":"777888999",

"medicamento":
"Prednisone 20mg",

"sig":
"Take 2 tablets daily",

"cantidad":10,


"pregunta":
"¿Cuántas tabletas toma diariamente?",

"opciones":[
"1",
"2",
"5",
"10"
],

"respuesta":
"2",

"explicacion":
"El SIG indica dos tabletas cada día."
},



{
"titulo":"Caso 9 - Ibuprofen",

"paciente":"Anna Lopez",

"dob":"07/07/1995",

"doctor":"Dr. King",

"npi":"333444555",

"medicamento":
"Ibuprofen 800mg",

"sig":
"Take 1 tablet every 8 hours",

"cantidad":30,


"pregunta":
"¿Cuántas dosis por día aproximadamente?",

"opciones":[
"1",
"2",
"3",
"8"
],

"respuesta":
"3",

"explicacion":
"Cada 8 horas equivale aproximadamente 3 veces al día."
},



{
"titulo":"Caso 10 - Azithromycin",

"paciente":"Daniel Thomas",

"dob":"10/30/1990",

"doctor":"Dr. Harris",

"npi":"999888777",

"medicamento":
"Azithromycin 250mg",

"sig":
"Take 2 tablets day 1, then 1 tablet daily",

"cantidad":6,


"pregunta":
"¿Qué tipo de receta es?",

"opciones":[
"Tratamiento corto con dosis inicial diferente",
"Medicamento mensual",
"Controlado Schedule II",
"Refill ilimitado"
],

"respuesta":
"Tratamiento corto con dosis inicial diferente",

"explicacion":
"Azithromycin suele usar una dosis inicial mayor seguida de mantenimiento."
}

]
