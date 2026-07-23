import streamlit as st

# ============================================================
# PAGE CONFIG AND BACKGROUND
# ============================================================
st.set_page_config(page_title="BostonPharmacy-OS", page_icon="💊", layout="centered")

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at center, #2f8fd1 0%, #1a5f9e 45%, #0d3b6b 100%);
}
[data-testid="stAppViewContainer"] > .main .block-container {
    background-color: rgba(255, 255, 255, 0.93);
    border-radius: 14px;
    padding: 2rem 2.5rem;
}
[data-testid="stSidebar"] {
    background-color: rgba(13, 59, 107, 0.92);
}
[data-testid="stSidebar"] * {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

st.title("💊 BostonPharmacy-OS v2026")
st.subheader("Pharmacy Technician Practice Simulator - Boston, MA")
st.write("---")

# ============================================================
# CASE DATABASE
# ============================================================

# ---------- MODULE 1: DATA ENTRY & E-PRESCRIBING ----------
casos_m1 = [
    {"med": "Amoxicillin 500mg capsules", "sig": "1 cap PO tid x 10 days", "qty": "30",
     "keywords": ["tid", "three times a day", "three times daily"], "dias": 10},
    {"med": "Metformin 500mg tablets", "sig": "1 tab PO bid x 30 days", "qty": "60",
     "keywords": ["bid", "twice a day", "twice daily"], "dias": 30},
    {"med": "Lisinopril 10mg tablets", "sig": "1 tab PO qd x 30 days", "qty": "30",
     "keywords": ["qd", "once a day", "once daily"], "dias": 30},
    {"med": "Ibuprofen 400mg tablets", "sig": "1 tab PO q6h prn pain x 5 days", "qty": "20",
     "keywords": ["q6h", "every 6 hours"], "dias": 5},
    {"med": "Prednisone 10mg tablets", "sig": "1 tab PO qid x 7 days", "qty": "28",
     "keywords": ["qid", "four times a day", "four times daily"], "dias": 7},
    {"med": "Warfarin 5mg tablets", "sig": "1 tab PO qhs x 30 days", "qty": "30",
     "keywords": ["qhs", "at bedtime", "before bed"], "dias": 30},
    {"med": "Levothyroxine 50mcg tablets", "sig": "1 tab PO qam x 90 days", "qty": "90",
     "keywords": ["qam", "every morning", "in the morning"], "dias": 90},
    {"med": "Cephalexin 500mg capsules", "sig": "1 cap PO q8h x 10 days", "qty": "30",
     "keywords": ["q8h", "every 8 hours"], "dias": 10},
    {"med": "Allopurinol 300mg tablets", "sig": "1 tab PO qod x 30 days", "qty": "15",
     "keywords": ["qod", "every other day"], "dias": 30},
    {"med": "Tramadol 50mg tablets", "sig": "1 tab PO q4-6h prn pain x 5 days", "qty": "20",
     "keywords": ["q4-6h", "every 4 to 6 hours", "as needed"], "dias": 5},
]

# ---------- MODULE 2: INSURANCE BILLING (MASSHEALTH) ----------
casos_m2 = [
    {"rechazo": "'Prior Authorization Required' (Lipitor 20mg).",
     "opciones": ["Call the police.",
                  "Switch to a generic medication without notifying the prescriber.",
                  "Notify the patient and send a fax/electronic alert to the prescriber's office to initiate the authorization."],
     "correcta": 2,
     "explicacion": "The prescriber must justify the use to MassHealth through the Prior Authorization process."},
    {"rechazo": "'Refill Too Soon' — the patient requests an early refill of Metformin.",
     "opciones": ["Override the rejection without asking anything.",
                  "Ask the reason (travel, lost medication) and consult the pharmacist about a possible override.",
                  "Tell the patient to pay cash without any explanation."],
     "correcta": 1,
     "explicacion": "Always investigate the reason before an override; the pharmacist decides if it's appropriate."},
    {"rechazo": "'Non-Formulary Drug' — the prescribed medication is not on the plan's formulary.",
     "opciones": ["Contact the prescriber to suggest a covered therapeutic alternative or request a formulary exception.",
                  "Dispense the medication and charge the difference without telling anyone.",
                  "Tell the patient to try another pharmacy."],
     "correcta": 0,
     "explicacion": "The technician coordinates with the prescriber's office to find a covered alternative or request an exception."},
    {"rechazo": "'Patient/Member Not Found' — the system does not recognize the patient's eligibility.",
     "opciones": ["Verify the insurance card details and confirm eligibility with MassHealth.",
                  "Assume the patient no longer has insurance and charge full price without checking.",
                  "Ignore the rejection and resubmit without changing anything."],
     "correcta": 0,
     "explicacion": "Data entry errors (ID, date of birth) are the most common cause; always verify before assuming no coverage."},
    {"rechazo": "'Quantity Limit Exceeded' — the prescribed quantity exceeds the plan's limit.",
     "opciones": ["Reduce the quantity without telling the prescriber or the patient.",
                  "Check the plan's limit and contact the prescriber to request an exception if clinically justified.",
                  "Cancel the prescription entirely."],
     "correcta": 1,
     "explicacion": "The technician requests the quantity override from the prescriber; they never make that clinical decision alone."},
    {"rechazo": "A Drug Utilization Review (DUR) alert for a possible drug interaction.",
     "opciones": ["Dispense anyway since the system could be wrong.",
                  "Ignore the alert if the patient insists everything is fine.",
                  "Alert the pharmacist immediately before continuing the dispensing process."],
     "correcta": 2,
     "explicacion": "DUR alerts related to interactions always require pharmacist review before dispensing."},
    {"rechazo": "The prescription has expired.",
     "opciones": ["Dispense anyway because the patient urgently needs it.",
                  "Contact the prescriber's office to get a new prescription or a renewal.",
                  "Change the date in the system so it passes validation."],
     "correcta": 1,
     "explicacion": "Never dispense on an expired prescription or alter the date; a new one must be requested from the prescriber."},
    {"rechazo": "The patient has two insurance plans and the claim was rejected for 'Coordination of Benefits'.",
     "opciones": ["Bill the primary insurance first, then bill the secondary for the remainder.",
                  "Bill only the secondary insurance because it's simpler.",
                  "Charge the patient the full amount and let them seek reimbursement."],
     "correcta": 0,
     "explicacion": "Coordination of benefits requires billing the primary insurance first, then the secondary."},
    {"rechazo": "'NDC Not Covered' — the specific manufacturer's NDC is not covered by the plan.",
     "opciones": ["Check whether a covered generic/equivalent NDC is available to substitute.",
                  "Charge the patient full price without looking for alternatives.",
                  "Leave the prescription unfilled indefinitely."],
     "correcta": 0,
     "explicacion": "Often the same generic drug from a different manufacturer is covered under the plan."},
    {"rechazo": "Rejection due to a missing DAW (Dispense as Written) code on a brand-name prescription.",
     "opciones": ["Check with the prescriber whether brand-only use is justified and enter the correct DAW code, or dispense the generic if allowed.",
                  "Enter a random DAW code so the system accepts the claim.",
                  "Dispense the brand without a code and have the pharmacy absorb the cost."],
     "correcta": 0,
     "explicacion": "The DAW code must accurately reflect the prescriber's instruction or the actual clinical situation."},
]

# ---------- MODULE 3: CONTROLLED SUBSTANCES (MASSPAT) ----------
casos_m3 = [
    {"caso": "A new patient presents a prescription for Oxycodone 10mg (Schedule II).",
     "opciones": ["Dispense right away since the prescription looks valid.",
                  "Check MassPAT to review usage patterns, other active prescriptions, or red flags.",
                  "Ask for cash payment before reviewing anything."],
     "correcta": 1,
     "explicacion": "MassPAT is mandatory before dispensing Schedule II-V medications in Massachusetts."},
    {"caso": "A patient requests an early refill of Xanax (Schedule IV, benzodiazepine).",
     "opciones": ["Review the MassPAT history and consult the pharmacist before deciding.",
                  "Give the refill right away since they're a known patient.",
                  "Refuse outright without checking anything."],
     "correcta": 0,
     "explicacion": "Any early refill of a controlled substance requires a history review and pharmacist approval."},
    {"caso": "A patient says they lost their Percocet (Schedule II) prescription and asks for a replacement.",
     "opciones": ["Refill the same quantity without issue since they're a regular customer.",
                  "Do not replace it without a new prescription from the prescriber; a police report may be required per pharmacy policy.",
                  "Give half the quantity as a compromise."],
     "correcta": 1,
     "explicacion": "Lost Schedule II medications are not automatically replaced; a new prescription is required."},
    {"caso": "A patient asks to transfer their Oxycodone (Schedule II) prescription to another pharmacy.",
     "opciones": ["It can be transferred without any issue, just like any other medication.",
                  "Schedule II prescriptions generally CANNOT be transferred between pharmacies.",
                  "It can only be transferred if the patient pays an extra fee."],
     "correcta": 1,
     "explicacion": "Unlike Schedule III-V, Schedule II prescriptions are not transferable between pharmacies (with very limited exceptions)."},
    {"caso": "A patient arrives at the counter to pick up a controlled substance.",
     "opciones": ["Verify a government-issued photo ID that matches the name on the prescription.",
                  "No ID is needed if the patient is already known.",
                  "Simply asking the patient to state their name out loud is enough."],
     "correcta": 0,
     "explicacion": "A government-issued photo ID is always verified when handing over a controlled substance."},
    {"caso": "A prescriber calls in a verbal order for Oxycodone (Schedule II).",
     "opciones": ["It's accepted without issue, just like any verbal prescription.",
                  "Verbal orders for Schedule II are generally NOT permitted, except in very specific emergencies.",
                  "It's accepted only if the prescriber confirms it twice by phone."],
     "correcta": 1,
     "explicacion": "Schedule II requires a written or electronic prescription; verbal orders are allowed only in very limited emergencies defined by law."},
    {"caso": "MassPAT shows the patient has multiple opioid prescriptions from different prescribers ('doctor shopping').",
     "opciones": ["Dispense anyway; it's not the technician's job to judge the patient.",
                  "Alert the pharmacist immediately before continuing with the dispensing process.",
                  "Call all the prescribers directly without telling the pharmacist."],
     "correcta": 1,
     "explicacion": "Any red flag in MassPAT is reported to the pharmacist first, who decides the next step."},
    {"caso": "A patient on Suboxone (Schedule III, buprenorphine) requests their monthly refill.",
     "opciones": ["Check MassPAT and confirm the refill authorization is active in the system.",
                  "Give the refill without checking anything since it's a chronic treatment.",
                  "Automatically deny the refill because it's a controlled substance."],
     "correcta": 0,
     "explicacion": "Even for chronic treatments, MassPAT and refill authorization are checked before dispensing."},
    {"caso": "A family member wants to pick up the patient's Adderall (Schedule II) on their behalf.",
     "opciones": ["It can be given to any family member without issue.",
                  "It is only given to the patient or to a documented, authorized agent under state law.",
                  "It can be given if the family member pays in cash."],
     "correcta": 1,
     "explicacion": "Dispensing of Schedule II is restricted to the patient or a formally authorized agent."},
    {"caso": "The pharmacy doesn't have the full quantity of a Schedule II medication and needs to do a partial fill.",
     "opciones": ["It is not allowed under any circumstances.",
                  "It is allowed under DEA rules if properly documented, with the remainder filled within 72 hours.",
                  "It can be completed at any time with no time limit."],
     "correcta": 1,
     "explicacion": "The DEA allows documented partial fills of Schedule II, with the remaining quantity provided within 72 hours."},
]

# ---------- MODULE 4: PATIENT POS & COPAY ----------
casos_m4 = [
    {"costo": 120.00, "tipo": "porcentaje", "cobertura": 0.80, "descripcion": "The insurance covers 80% of the cost."},
    {"costo": 200.00, "tipo": "porcentaje", "cobertura": 0.90, "descripcion": "The insurance covers 90% of the cost."},
    {"costo": 75.00, "tipo": "fijo", "copago_fijo": 10.00, "descripcion": "The plan has a flat $10 copay for this medication."},
    {"costo": 150.00, "tipo": "porcentaje", "cobertura": 0.70, "descripcion": "The insurance covers 70% of the cost."},
    {"costo": 50.00, "tipo": "porcentaje", "cobertura": 1.00, "descripcion": "MassHealth covers 100% of the cost for this medication."},
    {"costo": 300.00, "tipo": "porcentaje", "cobertura": 0.60, "descripcion": "The insurance covers 60% of the cost."},
    {"costo": 40.00, "tipo": "fijo", "copago_fijo": 5.00, "descripcion": "The plan has a flat $5 copay (generic Tier 1 medication)."},
    {"costo": 500.00, "tipo": "porcentaje", "cobertura": 0.85, "descripcion": "The insurance covers 85% of the cost."},
    {"costo": 90.00, "tipo": "porcentaje", "cobertura": 0.75, "descripcion": "The insurance covers 75% of the cost."},
    {"costo": 25.00, "tipo": "fijo", "copago_fijo": 3.00, "descripcion": "The plan has a flat $3 copay (preferred generic medication)."},
]

# ============================================================
# SIDE MENU
# ============================================================
opcion = st.sidebar.selectbox(
    "Select a system function:",
    ["1. Data Entry & E-Prescribing",
     "2. Insurance Billing (MassHealth)",
     "3. Controlled Substances (MassPAT)",
     "4. Patient POS & Copay"]
)

# ============================================================
# MODULE 1
# ============================================================
if opcion == "1. Data Entry & E-Prescribing":
    st.header("📝 Prescription Data Entry Module")

    num_caso = st.sidebar.selectbox("Practice case:", list(range(1, 11)), key="caso_m1")
    caso = casos_m1[num_caso - 1]

    st.info(f"Case {num_caso} of 10: Electronic prescription received from Massachusetts General Hospital.")

    receta_texto = (
        f"PATIENT: John Doe\nDOB: 11/14/1982\nDR: Dr. Elizabeth Smith (NPI: 1234567890)\n"
        f"MED: {caso['med']}\nSIG: {caso['sig']}\nQTY: {caso['qty']}"
    )
    st.text_area("Digital Prescription Received:", value=receta_texto, height=120, key=f"ta_{num_caso}")

    sig_input = st.text_input("Translate the SIG code into patient instructions (in English):", key=f"sig_{num_caso}")
    days_supply = st.number_input("How many days supply is this prescription for?", min_value=0, value=0, key=f"days_{num_caso}")

    if st.button("Verify Prescription", key=f"btn_{num_caso}"):
        sig_ok = any(k in sig_input.lower() for k in caso["keywords"])
        dias_ok = days_supply == caso["dias"]
        if sig_ok and dias_ok:
            st.success("✅ Excellent! The SIG translation and days supply are correct. Prescription ready for production.")
        elif not sig_ok and not dias_ok:
            st.error(f"❌ Review both the SIG translation and the days supply calculation. Correct days supply: {caso['dias']}.")
        elif not sig_ok:
            st.warning(f"⚠️ Review the translation of the SIG code: '{caso['sig']}'.")
        else:
            st.error(f"❌ Days Supply error. The correct calculation for this prescription is {caso['dias']} days.")

# ============================================================
# MODULE 2
# ============================================================
elif opcion == "2. Insurance Billing (MassHealth)":
    st.header("💳 Insurance Claim Adjudication")

    num_caso = st.sidebar.selectbox("Practice case:", list(range(1, 11)), key="caso_m2")
    caso = casos_m2[num_caso - 1]

    st.warning(f"SYSTEM ALERT — Case {num_caso} of 10: Claim Rejected by MassHealth.")
    st.error(f"REJECTION: {caso['rechazo']}")

    st.write("As a Pharmacy Technician, what is your correct next step?")
    accion = st.radio("Select the correct action:", caso["opciones"], key=f"radio_m2_{num_caso}")

    if st.button("Process Action", key=f"btn_m2_{num_caso}"):
        if caso["opciones"].index(accion) == caso["correcta"]:
            st.success(f"✅ Correct! {caso['explicacion']}")
        else:
            st.error(f"❌ Incorrect. {caso['explicacion']}")

# ============================================================
# MODULE 3
# ============================================================
elif opcion == "3. Controlled Substances (MassPAT)":
    st.header("🔒 Controlled Substance Verification")

    num_caso = st.sidebar.selectbox("Practice case:", list(range(1, 11)), key="caso_m3")
    caso = casos_m3[num_caso - 1]

    st.info(f"Case {num_caso} of 10: {caso['caso']}")
    st.write("What is the correct action according to Massachusetts (MassPAT / DEA) regulations?")

    accion = st.radio("Select the correct action:", caso["opciones"], key=f"radio_m3_{num_caso}")

    if st.button("Process Verification", key=f"btn_m3_{num_caso}"):
        if caso["opciones"].index(accion) == caso["correcta"]:
            st.success(f"✅ Correct! {caso['explicacion']}")
        else:
            st.error(f"❌ Incorrect. {caso['explicacion']}")

# ============================================================
# MODULE 4
# ============================================================
elif opcion == "4. Patient POS & Copay":
    st.header("💵 Point of Sale and Copay Calculation")

    num_caso = st.sidebar.selectbox("Practice case:", list(range(1, 11)), key="caso_m4")
    caso = casos_m4[num_caso - 1]

    st.info(f"Case {num_caso} of 10: Patient at the counter picking up their medication.")
    st.write("**Insurance details:**")
    st.write(f"- Total cost of medication: **${caso['costo']:.2f}**")
    st.write(f"- {caso['descripcion']}")

    copay_input = st.number_input(
        "Calculate the copay the patient must pay ($):",
        min_value=0.0, value=0.0, step=0.01, format="%.2f", key=f"copay_{num_caso}"
    )

    if st.button("Verify Copay", key=f"btn_m4_{num_caso}"):
        if caso["tipo"] == "porcentaje":
            copago_correcto = round(caso["costo"] * (1 - caso["cobertura"]), 2)
        else:
            copago_correcto = caso["copago_fijo"]

        if abs(copay_input - copago_correcto) < 0.01:
            st.success(f"✅ Correct! The copay is ${copago_correcto:.2f}.")
        else:
            st.error(f"❌ Incorrect. The correct copay is ${copago_correcto:.2f}.")

# ============================================================
# FOOTER
# ============================================================
st.write("---")
st.caption("Compliant with HIPAA regulations and the Massachusetts Board of Registration in Pharmacy.")
