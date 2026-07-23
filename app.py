import streamlit as st
import random

# =====================================================================
# 1. CONFIGURACIÓN COMPATIBLE DE LA PÁGINA E IMAGEN DE FONDO
# =====================================================================
st.set_page_config(page_title="Simulador de Técnico de Farmacia", layout="wide")

def set_bg_image():
    url_imagen = "https://unsplash.com"
    
    st.html(f"""
    <style>
    .stApp {{
        background-image: url("{url_imagen}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    div.stMainBlockContainer {{
        background-color: rgba(17, 22, 27, 0.95) !important;
        border-radius: 12px;
        padding: 30px !important;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }}
    </style>
    """)

set_bg_image()

# =====================================================================
# 2. BANCO DE DATOS INTEGRADO (10 EJERCICIOS POR SECCIÓN)
# =====================================================================
ejercicios_masspat = [
    {
        "caso": "Paciente presenta receta de Oxycodone 10mg (Schedule II).",
        "pregunta": "¿Cuál es el paso correcto ANTES de dispensar esta receta?",
        "opciones": [
            "Dispensar de inmediato, ya que la receta parece válida.",
            "Consultar el historial del paciente en MassPAT para verificar patrones de uso.",
            "Pedirle al paciente que pague en efectivo antes de revisar nada."
        ],
        "correcta": "Consultar el historial del paciente en MassPAT para verificar patrones de uso.",
        "explicacion": "MassPAT es obligatorio antes de dispensar Schedule II-V en Massachusetts para detectar duplicidad."
    },
    {
        "caso": "Paciente solicita un refill de Tramadol (Schedule IV). En MassPAT ves que lo recibió en otra farmacia hace 5 días.",
        "pregunta": "¿Qué acción debes tomar?",
        "opciones": [
            "Llenar la receta sin decir nada para no molestar al paciente.",
            "Retener la dispensación, alertar al farmacéutico y contactar al médico.",
            "Decirle al paciente que regrese cuando no haya nadie en el mostrador."
        ],
        "correcta": "Retener la dispensación, alertar al farmacéutico y contactar al médico.",
        "explicacion": "Los surtidos tempranos en múltiples farmacias son banderas rojas críticas en el sistema MassPAT."
    },
    {
        "caso": "Un cliente nuevo trae una receta de Adderall XR 20mg escrita por un médico de otro estado.",
        "pregunta": "¿Cómo asiste MassPAT en esta situación?",
        "opciones": [
            "MassPAT no funciona con médicos de fuera del estado.",
            "Permite revisar el historial multiestatal de prescripciones para asegurar que no haya duplicidad.",
            "El sistema cobra una tarifa automática al paciente por ser de otro estado."
        ],
        "correcta": "Permite revisar el historial multiestatal de prescripciones para asegurar que no haya duplicidad.",
        "explicacion": "MassPAT está interconectado con bases de datos de otros estados para monitoreo interestatal."
    },
    {
        "caso": "Estás procesando Lorazepam. El sistema MassPAT arroja un 'score' de riesgo de sobredosis muy elevado.",
        "pregunta": "¿Cuál es el protocolo a seguir?",
        "opciones": [
            "Ignorar el puntaje ya que el Lorazepam es Schedule IV.",
            "Informar al farmacéutico de inmediato para una evaluación clínica.",
            "Llamar a la policía directamente desde el mostrador."
        ],
        "correcta": "Informar al farmacéutico de inmediato para una evaluación clínica.",
        "explicacion": "Los puntajes de riesgo alertan sobre interacciones peligrosas que pueden deprimir el sistema respiratorio."
    },
    {
        "caso": "Un médico llama para que dispenses Codeína basándote en su palabra sin receta electrónica aún.",
        "pregunta": "¿Qué normativa del PDMP/MassPAT aplica aquí?",
        "opciones": [
            "Se puede dispensar si el médico promete enviar el papel el próximo mes.",
            "Las sustancias Schedule II-V requieren transmisión electrónica obligatoria o receta física válida.",
            "El técnico puede escribir una receta provisional."
        ],
        "correcta": "Las sustancias Schedule II-V requieren transmisión electrónica obligatoria o receta física válida.",
        "explicacion": "La ley exige métodos de transmisión estrictos para el registro fidedigno en el MassPAT."
    },
    {
        "caso": "Al consultar MassPAT para una receta de Metadona, el sistema no muestra ningún historial clínico previo.",
        "pregunta": "¿Qué significa esto?",
        "opciones": [
            "El paciente nunca ha recibido sustancias controladas registradas en el estado.",
            "El sistema está roto y permanentemente fuera de servicio.",
            "La receta es automáticamente ilegal."
        ],
        "correcta": "El paciente nunca ha recibido sustancias controladas registradas en el estado.",
        "explicacion": "Un historial vacío requiere verificación minuciosa de la identidad antes de proceder."
    },
    {
        "caso": "Un paciente te pide una copia impresa de su propio reporte de MassPAT.",
        "pregunta": "¿Está permitido entregar este documento?",
        "opciones": [
            "Sí, cualquier documento de la farmacia se le puede regalar.",
            "No. Los datos de MassPAT son confidenciales y protegidos por HIPAA.",
            "Sí, cobrándole una tarifa de impresión."
        ],
        "correcta": "No. Los datos de MassPAT son confidenciales y protegidos por HIPAA.",
        "explicacion": "El acceso a los datos de los PDMP está estrictamente regulado por leyes de privacidad de salud."
    },
    {
        "caso": "Estás ingresando los datos de una receta de fentanilo en el sistema de la farmacia.",
        "pregunta": "¿En cuánto tiempo debe reportarse esta dispensación a la base de datos de MassPAT?",
        "opciones": [
            "Al final de cada mes en un reporte acumulativo.",
            "Al cierre del siguiente día hábil por normativa estatal.",
            "No es necesario transmitirlo de forma manual."
        ],
        "correcta": "Al cierre del siguiente día hábil por normativa estatal.",
        "explicacion": "La actualización dentro de 24 horas hábiles garantiza que los datos eviten abusos inmediatos."
    },
    {
        "caso": "El sistema MassPAT está lento y tarda en cargar en un momento de alta demanda en el mostrador.",
        "pregunta": "¿Qué se debe hacer?",
        "opciones": [
            "Saltarse la verificación para mantener la fila avanzando rápido.",
            "Esperar a que el sistema cargue correctamente y completar la verificación obligatoria.",
            "Darle al paciente el medicamento a mitad de precio por la espera."
        ],
        "correcta": "Esperar a que el sistema cargue correctamente y completar la verificación obligatoria.",
        "explicacion": "Los problemas técnicos de red no eximen a la farmacia de cumplir con las regulaciones de seguridad."
    },
    {
        "caso": "Al revisar MassPAT descubres que tres médicos diferentes le han recetado el mismo narcótico en 30 días.",
        "pregunta": "¿Cómo se conoce técnicamente esta conducta de alerta?",
        "opciones": [
            "Fidelización de clientes médicos.",
            "Doctor Shopping (Búsqueda múltiple de prescriptores).",
            "Rotación de inventario clínico."
        ],
        "correcta": "Doctor Shopping (Búsqueda múltiple de prescriptores).",
        "explicacion": "El 'Doctor shopping' es uno de los principales problemas que los sistemas PDMP buscan mitigar."
    }
]

ejercicios_pos = [
    {"costo": 120.00, "cobertura": 0.80, "concepto": "Medicamento de mantenimiento básico"},
    {"costo": 45.50, "cobertura": 0.70, "concepto": "Antibiótico de amplio espectro"},
    {"costo": 250.00, "cobertura": 0.90, "concepto": "Insulina para diabetes"},
    {"costo": 85.00, "cobertura": 0.50, "concepto": "Crema dermatológica especializada"},
    {"costo": 15.00, "cobertura": 0.60, "concepto": "Medicamento genérico para la presión"},
    {"costo": 310.00, "cobertura": 0.85, "concepto": "Inhalador para el asma severa (Marca)"},
    {"costo": 65.20, "cobertura": 0.75, "concepto": "Antiviral para tratamiento agudo"},
    {"costo": 190.00, "cobertura": 0.40, "concepto": "Suplemento metabólico de alta gama"},
    {"costo": 55.00, "cobertura": 0.20, "concepto": "Tratamiento con cobertura limitada"},
    {"costo": 420.00, "cobertura": 0.95, "concepto": "Medicamento biológico de alta prioridad"}
]

# =====================================================================
# 3. CONTROL DE ESTADO DE LOS EJERCICIOS (SESSION STATE)
# =====================================================================
if "id_masspat" not in st.session_state:
    st.session_state.id_masspat = random.randint(0, 9)
if "id_pos" not in st.session_state:
    st.session_state.id_pos = random.randint(0, 9)

def cambiar_ejercicio_masspat():
    st.session_state.id_masspat = random.randint(0, 9)

def cambiar_ejercicio_pos():
    st.session_state.id_pos = random.randint(0, 9)

# =====================================================================
# 4. MENÚ EN LA BARRA LATERAL
# =====================================================================
opcion = st.sidebar.selectbox(
    "Selecciona un Módulo del Simulador:",
    [
        "1. Patient Intake & Prescription Entry",
        "2. Drug Lookup & Inventory",
        "3. Controlled Substances (MassPAT)",
        "4. Patient POS & Copay"
    ]
)

# =====================================================================
# 5. LÓGICA DE RENDERIZADO POR MÓDULOS
# =====================================================================

# ==============================
# MÓDULO 1 DATA ENTRY
# ==============================

if opcion == "1. Patient Intake & Prescription Entry":

    st.header("📝 Patient Intake & Prescription Entry")

    st.image(
        "https://images.unsplash.com/photo-1580281657527-47f249e8f3df",
        caption="Electronic Prescription System",
        use_container_width=True
    )

    st.info(
        "Caso de práctica: Recibir, interpretar e ingresar una receta electrónica."
    )


    receta = {
        "Paciente": "Maria Johnson",
        "DOB": "05/12/1985",
        "Doctor": "Dr. Robert Williams",
        "Medicamento": "Amoxicillin 500mg",
        "SIG": "Take 1 capsule by mouth three times daily",
        "Quantity": "30 capsules"
    }


    for clave, valor in receta.items():
        st.write(f"**{clave}:** {valor}")


    respuesta = st.text_input(
        "¿Cuántos días de suministro tiene esta receta?"
    )


    if st.button("Verificar Data Entry"):

        if respuesta == "10":
            st.success(
                "✅ Correcto. 30 cápsulas / 3 cápsulas al día = 10 días."
            )

        else:
            st.error(
                "❌ Incorrecto. El Days Supply correcto es 10 días."
            )


# ==============================
# MÓDULO 2 INVENTORY
# ==============================


elif opcion == "2. Drug Lookup & Inventory":

    st.header("📦 Drug Lookup & Inventory")

    st.image(
        "https://images.unsplash.com/photo-1587854692152-cbe660dbde88",
        caption="Pharmacy Inventory",
        use_container_width=True
    )


    st.info(
        "Caso: El sistema muestra bajo inventario de un medicamento."
    )


    medicamento = st.selectbox(
        "Medicamento:",
        [
            "Metformin 500mg",
            "Lisinopril 10mg",
            "Atorvastatin 20mg"
        ]
    )


    inventario = st.number_input(
        "Cantidad disponible:",
        min_value=0,
        value=5
    )


    if st.button("Revisar Inventario"):

        if inventario < 10:

            st.warning(
                f"⚠️ {medicamento} necesita orden de compra."
            )

        else:

            st.success(
                "✅ Inventario suficiente."
            )


# ==============================
# MÓDULO 3 MASS PAT
# ==============================


elif opcion == "3. Controlled Substances (MassPAT)":

    st.header("🔒 Controlled Substances - MassPAT")


    st.image(
        "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae",
        caption="Controlled Substance Monitoring",
        use_container_width=True
    )


    caso_actual = ejercicios_masspat[
        st.session_state.id_masspat
    ]


    st.subheader(
        caso_actual["caso"]
    )


    st.write(
        caso_actual["pregunta"]
    )


    respuesta = st.radio(
        "Seleccione la respuesta:",
        caso_actual["opciones"]
    )


    if st.button("Evaluar respuesta MassPAT"):

        if respuesta == caso_actual["correcta"]:

            st.success(
                "✅ Respuesta correcta"
            )

            st.info(
                caso_actual["explicacion"]
            )

        else:

            st.error(
                "❌ Respuesta incorrecta"
            )

            st.info(
                caso_actual["explicacion"]
            )


    if st.button("🔄 Nuevo Caso MassPAT"):

        cambiar_ejercicio_masspat()

        st.rerun()



# ==============================
# MÓDULO 4 POS
# ==============================


elif opcion == "4. Patient POS & Copay":


    st.header("💳 Patient POS & Copay")


    st.image(
        "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d",
        caption="Patient Checkout",
        use_container_width=True
    )


    caso = ejercicios_pos[
        st.session_state.id_pos
    ]


    st.info(
        caso["concepto"]
    )


    st.write(
        f"💊 Precio medicamento: ${caso['costo']}"
    )


    st.write(
        f"🏥 Seguro cubre: {caso['cobertura']*100}%"
    )


    pago = st.number_input(
        "Ingrese copago del paciente:",
        min_value=0.0,
        step=0.01
    )


    if st.button("Calcular Copago"):


        correcto = round(
            caso["costo"] *
            (1-caso["cobertura"]),
            2
        )


        if pago == correcto:

            st.success(
                f"✅ Correcto. Copago ${correcto}"
            )

        else:

            st.error(
                f"❌ Incorrecto. Debe pagar ${correcto}"
            )


    if st.button("🔄 Nuevo Caso POS"):

        cambiar_ejercicio_pos()

        st.rerun()



# =====================================================================
# PIE DE PÁGINA
# =====================================================================

st.divider()

st.caption(
    "BostonPharmacy-OS v2026 | Pharmacy Technician Training Simulator | Massachusetts"
)

