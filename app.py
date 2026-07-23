import streamlit as st
import base64
import random

# =====================================================================
# 1. FUNCIÓN PARA CONFIGURAR LA IMAGEN DE FONDO (MODO OSCURO)
# =====================================================================
def set_bg_image(image_file):
    try:
        with open(image_file, "rb") as f:
            img_data = f.read()
        b64_encoded = base64.b64encode(img_data).decode()
        
        # Estilos CSS para fijar el fondo y opacar levemente el contenedor para legibilidad
        style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64_encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* Capa oscura semi-transparente sobre el contenido para maximizar contraste */
        .block-container {{
            background-color: rgba(17, 22, 27, 0.85);
            border-radius: 15px;
            padding: 30px !important;
            margin-top: 20px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
        }}
        </style>
        """
        st.markdown(style, unsafe_allowed_html=True)
    except FileNotFoundError:
        st.warning("⚠️ No se encontró el archivo 'fondo_simulador.png'. Colócalo en la misma carpeta de tu script.")

# Llamar a la función del fondo al iniciar la app
set_bg_image("fondo_simulador.png")

# =====================================================================
# 2. BANCO DE DATOS: 10 EJERCICIOS POR FUNCIÓN
# =====================================================================
ejercicios_masspat = [
    {
        "caso": "Paciente presenta receta de Oxycodone 10mg (Schedule II).",
        "pregunta": "¿Cuál es el paso correcto ANTES de dispensar esta receta?",
        "opciones": [
            "Dispensar de inmediato, ya que la receta parece válida.",
            "Consultar el historial del paciente en MassPAT para verificar patrones de uso, otras recetas activas de opioides o señales de alerta.",
            "Pedirle al paciente que pague en efectivo antes de revisar nada."
        ],
        "correcta": "Consultar el historial del paciente en MassPAT para verificar patrones de uso, otras recetas activas de opioides o señales de alerta.",
        "explicacion": "MassPAT es obligatorio antes de dispensar Schedule II-V en Massachusetts para detectar 'doctor shopping' y duplicidad."
    },
    {
        "caso": "Un paciente solicita un refill de Tramadol (Schedule IV). Al revisar MassPAT, notas que recibió la misma dosis en otra farmacia hace 5 días.",
        "pregunta": "¿Qué acción debes tomar?",
        "opciones": [
            "Llenar la receta sin decir nada para no molestar al paciente.",
            "Retener la dispensación, alertar al farmacéutico y contactar al médico debido a una alerta de duplicidad terapéutica / uso indebido.",
            "Decirle al paciente que regrese cuando no haya nadie en el mostrador."
        ],
        "correcta": "Retener la dispensación, alertar al farmacéutico and contactar al médico debido a una alerta de duplicidad terapéutica / uso indebido.",
        "explicacion": "Los surtidos tempranos en múltiples farmacias son banderas rojas críticas en el sistema MassPAT."
    },
    {
        "caso": "Un cliente nuevo trae una receta de Adderall XR 20mg escrita por un médico de otro estado.",
        "pregunta": "¿Cómo asiste MassPAT en esta situación?",
        "opciones": [
            "MassPAT no funciona con médicos de fuera del estado, se debe rechazar la receta de inmediato.",
            "Permite al farmacéutico revisar el historial multiestatal de prescripciones para asegurar que el paciente no esté duplicando sustancias controladas.",
            "El sistema cobra una tarifa automática al paciente por ser de otro estado."
        ],
        "correcta": "Permite al farmacéutico revisar el historial multiestatal de prescripciones para asegurar que el paciente no esté duplicando sustancias controladas.",
        "explicacion": "MassPAT está interconectado con bases de datos de otros estados participantes para monitoreo interestatal."
    },
    {
        "caso": "Estás procesando una receta de Lorazepam. El sistema MassPAT arroja un 'score' de riesgo de sobredosis muy elevado para el paciente.",
        "pregunta": "¿Cuál es el protocolo a seguir?",
        "opciones": [
            "Ignorar el puntaje ya que el Lorazepam es Schedule IV y no un opioide.",
            "Informar al farmacéutico de inmediato para que realice una evaluación clínica y considere ofrecer Naloxona (Narcan).",
            "Llamar a la policía directamente desde el mostrador."
        ],
        "correcta": "Informar al farmacéutico de inmediato para que realice una evaluación clínica y considere ofrecer Naloxona (Narcan).",
        "explicacion": "Los puntajes de riesgo alertan sobre interacciones peligrosas (como benzodiacepinas + opioides) que pueden deprimir el sistema respiratorio."
    },
    {
        "caso": "Un médico llama indicando que olvidó registrar una receta electrónica de Codeína en el sistema y pide que la dispenses basándote en su palabra.",
        "pregunta": "¿Qué normativa del PDMP/MassPAT aplica aquí?",
        "opciones": [
            "Se puede dispensar si el médico promete enviar el papel el próximo mes.",
            "Las sustancias controladas Schedule II-V requieren transmisión electrónica obligatoria o receta física válida; MassPAT registrará el método de recepción.",
            "El técnico puede escribir una receta falsa para avanzar el proceso."
        ],
        "correcta": "Las sustancias controladas Schedule II-V requieren transmisión electrónica obligatoria o receta física válida; MassPAT registrará el método de recepción.",
        "explicacion": "La ley exige métodos de transmisión sumamente estrictos y seguros para el registro fidedigno en el MassPAT."
    },
    {
        "caso": "Al consultar MassPAT para una receta de Metadona, el sistema no muestra ningún historial clínico previo para este paciente.",
        "pregunta": "¿Qué significa esto?",
        "opciones": [
            "El paciente nunca ha recibido sustancias controladas registradas en el estado o está usando una identificación falsa.",
            "El sistema está roto y permanentemente fuera de servicio.",
            "La receta es automáticamente ilegal y debe destruirse."
        ],
        "correcta": "El paciente nunca ha recibido sustancias controladas registradas en el estado o está usando una identificación falsa.",
        "explicacion": "Un historial vacío requiere verificación minuciosa de la identidad del paciente antes de proceder con controlados."
    },
    {
        "caso": "Un paciente te pide una copia impresa de su propio reporte de MassPAT porque quiere ver lo que los médicos dicen de él.",
        "pregunta": "¿Está permitido entregar este documento?",
        "opciones": [
            "Sí, cualquier documento de la farmacia se le puede regalar al cliente si lo pide.",
            "No. Los datos de MassPAT son confidenciales y protegidos por HIPAA; solo personal médico autorizado puede consultarlo dentro del flujo de atención.",
            "Sí, pero cobrándole una tarifa de impresión de $10.00."
        ],
        "correcta": "No. Los datos de MassPAT son confidenciales y protegidos por HIPAA; solo personal médico autorizado puede consultarlo dentro del flujo de atención.",
        "explicacion": "El acceso a los datos de los PDMP está estrictamente regulado por leyes de privacidad de salud."
    },
    {
        "caso": "Estás ingresando los datos de una receta de fentanilo en el sistema de la farmacia.",
        "pregunta": "¿En cuánto tiempo debe reportarse esta dispensación a la base de datos de MassPAT?",
        "opciones": [
            "Al final de cada mes en un reporte acumulativo.",
            "Por ley, las farmacias deben transmitir los datos de dispensación de controlados al cierre del siguiente día hábil.",
            "No es necesario transmitirlo, el sistema lo adivina solo."
        ],
        "correcta": "Por ley, las farmacias deben transmitir los datos de dispensación de controlados al cierre del siguiente día hábil.",
        "explicacion": "La actualización oportuna (dentro de 24 horas hábiles generalmente) garantiza que los datos sean útiles para evitar abusos inmediatos."
    },
    {
        "caso": "Un farmacéutico te pide verificar a un paciente en MassPAT, pero el sistema está lento y tarda en cargar.",
        "pregunta": "¿Qué se debe hacer en este escenario de alta demanda en el mostrador?",
        "opciones": [
            "Saltarse la verificación para mantener la fila avanzando rápido.",
            "Esperar a que el sistema cargue correctamente y completar la verificación obligatoria antes de que el farmacéutico firme el producto.",
            "Darle al paciente el medicamento a mitad de precio por la molestia de la espera."
        ],
        "correcta": "Esperar a que el sistema cargue correctamente y completar la verificación obligatoria antes de que el farmacéutico firme el producto.",
        "explicacion": "Los problemas técnicos de red no eximen a la farmacia de cumplir con las regulaciones de seguridad estatales."
    },
    {
        "caso": "Revisando el MassPAT de un paciente, descubres que tres médicos diferentes le han recetado el mismo narcótico en los últimos 30 días.",
        "pregunta": "¿Cómo se conoce técnicamente esta conducta de alerta?",
        "opciones": [
            "Fidelización de clientes médicos.",
            "Doctor Shopping (Búsqueda múltiple de prescriptores para obtener fármacos).",
            "Rotación de inventario clínico."
        ],
        "correcta": "Doctor Shopping (Búsqueda múltiple de prescriptores para obtener fármacos).",
