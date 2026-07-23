import streamlit as st
import base64
import random

# =====================================================================
# 1. CONFIGURACIÓN DE LA PÁGINA E IMAGEN DE FONDO
# =====================================================================
st.set_page_config(page_title="Simulador de Técnico de Farmacia", layout="wide")

def set_bg_image(image_file):
    try:
        with open(image_file, "rb") as f:
            img_data = f.read()
        b64_encoded = base64.b64encode(img_data).decode()
        
        style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64_encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .block-container {{
            background-color: rgba(17, 22, 27, 0.90);
            border-radius: 15px;
            padding: 30px !important;
            margin-top: 20px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
        }}
        </style>
        """
        st.markdown(style, unsafe_allowed_html=True)
    except FileNotFoundError:
        st.sidebar.warning("⚠️ Guarda 'fondo_simulador.png' junto a tu script para ver el fondo.")

set_bg_image("fondo_simulador.png")

# =====================================================================
# 2. BANCO DE DATOS INTEGRADO (ESTRUCTURAS CERRADAS CORRECTAMENTE)
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

