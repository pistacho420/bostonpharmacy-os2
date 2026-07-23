import streamlit as st
# Configuración de la página web local
st.set_page_config(page_title="BostonPharmacy-OS", page_icon="💊", layout="centered")
st.title("💊 BostonPharmacy-OS v2026")
st.subheader("Simulador Técnico de Farmacia - Boston, MA")
st.write("---")
# Menú de navegación lateral
opcion = st.sidebar.selectbox(
    "Selecciona una función del sistema:",
    ["1. Data Entry & E-Prescribing", 
     "2. Insurance Billing (MassHealth)", 
     "3. Controlled Substances (MassPAT)", 
     "4. Patient POS & Copay"]
)
# Lógica del menú
if opcion == "1. Data Entry & E-Prescribing":
    st.header("📝 Módulo de Ingreso de Recetas (Data Entry)")
    st.info("Caso de práctica: Receta electrónica recibida desde Massachusetts General Hospital.")
    
    st.text_area(
        "Receta Digital Recibida:", 
        value="PATIENT: John Doe\nDOB: 11/14/1982\nDR: Dr. Elizabeth Smith (NPI: 1234567890)\nMED: Amoxicillin 500mg capsules\nSIG: 1 cap PO tid x 10 days\nQTY: 30", 
        height=120
    )
    
    sig_input = st.text_input("Traduce el código SIG a instrucciones para el paciente (en inglés o español):")
    days_supply = st.number_input("¿Para cuántos días de suministro (Days Supply) es esta receta?", min_value=0, value=0)
    
    if st.button("Verificar Receta"):
        if "3 veces al día" in sig_input.lower() or "three times a day" in sig_input.lower():
            if days_supply == 10:
                st.success("✅ ¡Excelente! El SIG y los días de suministro son correctos. Receta lista para producción.")
            else:
                st.error("❌ Error en Days Supply. Si toma 3 cápsulas al día y se le dan 30, el suministro es para 10 días.")
        else:
            st.warning("⚠️ Revisa la traducción del código SIG 'tid' (Three times a day / 3 veces al día).")
elif opcion == "2. Insurance Billing (MassHealth)":
    st.header("💳 Adjudicación de Seguros Médicos")
    st.warning("ALERTA DEL SISTEMA: Reclamo Rechazado por MassHealth.")
    st.error("RECHAZO: 'Prior Authorization Required' (Se requiere autorización previa para Lipitor 20mg).")
    
    st.write("Como Técnico en Farmacia, ¿cuál es tu siguiente paso legal?")
    accion = st.radio("Selecciona la acción correcta:", [
        "Llamar a la policía.",
        "Cambiar el medicamento por uno genérico sin avisar al médico.",
        "Notificar al paciente y enviar un fax/alerta electrónica al consultorio del médico para que tramite la autorización."
    ])
    
    if st.button("Procesar Acción"):
        if accion == "Notificar al paciente y enviar un fax/alerta electrónica al consultorio del médico para que tramite la autorización.":
            st.success("✅ ¡Correcto! Esa es la práctica estándar en Massachusetts. El médico debe justificar el uso ante MassHealth.")
        else:
            st.error("❌ Incorrecto. Esa acción viola los protocolos de seguridad o los derechos del paciente.")
# Nota al pie sobre leyes
st.write("---")
st.caption("Cumple con normativas HIPAA y el Massachusetts Board of Registration in Pharmacy.")
