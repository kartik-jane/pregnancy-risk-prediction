

# import streamlit as st
# import pandas as pd
# import joblib

# # Load model
# model = joblib.load("models/best_model.pkl")

# # --- Page Config ---
# st.set_page_config(page_title="Pregnancy Risk Predictor", layout="centered")

# # --- Title ---
# st.title("🤰 Pregnancy Risk Prediction App")
# st.markdown("Predict maternal health risk based on medical and pregnancy-related parameters.")

# # --- Sidebar ---
# st.sidebar.header("📋 Instructions")
# st.sidebar.markdown("""
# Fill in the following medical details of the patient.  
# The model will analyze the information and predict the **risk level** of the pregnancy.
# """)

# # --- Layout Columns ---
# col1, col2 = st.columns(2)

# with col1:
#     age = st.number_input("Age", 10, 60, 30)
#     weight = st.number_input("Weight (kg)", 30, 150, 65)
#     height = st.number_input("Height (cm)", 100, 200, 160)
#     preg_num = st.number_input("Pregnancy Number", 1, 10, 1)
#     multi_preg = st.selectbox("Multiple Pregnancy", [0, 1])
#     diabetes = st.selectbox("Diabetes", [0, 1])
#     clotting_disorder = st.selectbox("Blood Clotting Disorder", [0, 1])
#     placenta_prob = st.selectbox("Placenta Problems", [0, 1])
#     preterm_labour = st.selectbox("Preterm Labour", [0, 1])
#     ecg_abnormal = st.selectbox("ECG Abnormal", [0, 1])
#     uterine_contractions = st.selectbox("Uterine Contractions", [0, 1])
#     fetal_ecg = st.selectbox("Fetal ECG Abnormal", [0, 1])

# with col2:
#     maternal_hr = st.slider("Maternal Heart Rate (bpm)", 50, 180, 85)
#     sys_bp = st.slider("BP Systolic (mmHg)", 80, 200, 120)
#     dia_bp = st.slider("BP Diastolic (mmHg)", 50, 130, 80)
#     spo2 = st.slider("Oxygen Saturation (%)", 70, 100, 98)
#     temp = st.slider("Body Temperature (C)", 34.0, 42.0, 37.0)
#     glucose = st.slider("Glucose Level (mg/dL)", 60, 250, 90)
#     resp_rate = st.slider("Respiratory Rate", 10, 40, 18)
#     fetal_hr = st.slider("Fetal Heart Rate (bpm)", 80, 200, 140)
#     fetal_movements = st.slider("Fetal Movements", 0, 10, 5)
#     fetal_position = st.selectbox("Fetal Position", [0, 1, 2])
#     amniotic_index = st.slider("Amniotic Fluid Index (cm)", 0.0, 30.0, 12.0)
#     cbc_wbc = st.slider("CBC WBC (x10^9/L)", 2.0, 30.0, 8.0)

# # --- Prediction ---
# if st.button("🔍 Predict Risk Level"):
#     input_df = pd.DataFrame([{
#         "Age": age,
#         "Weight (kg)": weight,
#         "Height (cm)": height,
#         "Pregnancy Number": preg_num,
#         "Multiple Pregnancy": multi_preg,
#         "Diabetes": diabetes,
#         "Blood Clotting Disorder": clotting_disorder,
#         "Placenta Problems": placenta_prob,
#         "Preterm Labour": preterm_labour,
#         "Maternal Heart Rate (bpm)": maternal_hr,
#         "BP Systolic (mmHg)": sys_bp,
#         "BP Diastolic (mmHg)": dia_bp,
#         "Oxygen Saturation (%)": spo2,
#         "Body Temperature (C)": temp,
#         "Glucose Level (mg/dL)": glucose,
#         "ECG Abnormal": ecg_abnormal,
#         "Respiratory Rate (breaths/min)": resp_rate,
#         "Uterine Contractions": uterine_contractions,
#         "Fetal Heart Rate (bpm)": fetal_hr,
#         "Fetal Movements": fetal_movements,
#         "Fetal Position": fetal_position,
#         "Amniotic Fluid Index (cm)": amniotic_index,
#         "Fetal ECG Abnormal": fetal_ecg,
#         "CBC WBC (x10^9/L)": cbc_wbc,
#     }])

#     prediction = model.predict(input_df)[0]
    
#     st.subheader("🩺 Prediction Result")
#     st.success(f"Predicted Pregnancy Risk Level: **{prediction}**")

# import streamlit as st
# import pandas as pd
# import joblib



# # Binary inputs with Yes/No dropdowns
# multi_preg = st.selectbox("Multiple Pregnancy", ["No", "Yes"])
# diabetes = st.selectbox("Diabetes", ["No", "Yes"])
# clotting_disorder = st.selectbox("Blood Clotting Disorder", ["No", "Yes"])
# placenta_prob = st.selectbox("Placenta Problems", ["No", "Yes"])
# preterm_labour = st.selectbox("Preterm Labour", ["No", "Yes"])
# ecg_abnormal = st.selectbox("ECG Abnormal", ["No", "Yes"])
# uterine_contractions = st.selectbox("Uterine Contractions", ["No", "Yes"])
# fetal_ecg = st.selectbox("Fetal ECG Abnormal", ["No", "Yes"])

# # Convert Yes/No to 1/0
# multi_preg = 1 if multi_preg == "Yes" else 0
# diabetes = 1 if diabetes == "Yes" else 0
# clotting_disorder = 1 if clotting_disorder == "Yes" else 0
# placenta_prob = 1 if placenta_prob == "Yes" else 0
# preterm_labour = 1 if preterm_labour == "Yes" else 0
# ecg_abnormal = 1 if ecg_abnormal == "Yes" else 0
# uterine_contractions = 1 if uterine_contractions == "Yes" else 0
# fetal_ecg = 1 if fetal_ecg == "Yes" else 0






import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/best_model.pkl")

# Page config
st.set_page_config(page_title="Pregnancy Risk Predictor", layout="centered")

# Title and instructions
st.title("🤰 Pregnancy Risk Prediction App")
st.markdown("Enter medical and pregnancy information to assess the risk level.")

st.sidebar.header("📋 Instructions")
st.sidebar.markdown("""
This app predicts the risk level of a pregnancy based on maternal health data.  
Fill in all the fields below to receive a risk assessment.
""")

# Layout columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 10, 60, 30)
    weight = st.number_input("Weight (kg)", 30, 150, 65)
    height = st.number_input("Height (cm)", 100, 200, 160)
    preg_num = st.number_input("Pregnancy Number", 1, 10, 1)
    multi_preg = st.selectbox("Multiple Pregnancy", ["No", "Yes"])
    diabetes = st.selectbox("Diabetes", ["No", "Yes"])
    clotting_disorder = st.selectbox("Blood Clotting Disorder", ["No", "Yes"])
    placenta_prob = st.selectbox("Placenta Problems", ["No", "Yes"])
    preterm_labour = st.selectbox("Preterm Labour", ["No", "Yes"])
    ecg_abnormal = st.selectbox("ECG Abnormal", ["No", "Yes"])
    uterine_contractions = st.selectbox("Uterine Contractions", ["No", "Yes"])
    fetal_ecg = st.selectbox("Fetal ECG Abnormal", ["No", "Yes"])

with col2:
    maternal_hr = st.slider("Maternal Heart Rate (bpm)", 50, 180, 85)
    sys_bp = st.slider("BP Systolic (mmHg)", 80, 200, 120)
    dia_bp = st.slider("BP Diastolic (mmHg)", 50, 130, 80)
    spo2 = st.slider("Oxygen Saturation (%)", 70, 100, 98)
    temp = st.slider("Body Temperature (C)", 34.0, 42.0, 37.0)
    glucose = st.slider("Glucose Level (mg/dL)", 60, 250, 90)
    resp_rate = st.slider("Respiratory Rate", 10, 40, 18)
    fetal_hr = st.slider("Fetal Heart Rate (bpm)", 80, 200, 140)
    fetal_movements = st.slider("Fetal Movements", 0, 10, 5)
    fetal_position = st.selectbox("Fetal Position", [0, 1, 2])
    amniotic_index = st.slider("Amniotic Fluid Index (cm)", 0.0, 30.0, 12.0)
    cbc_wbc = st.slider("CBC WBC (x10⁹/L)", 2.0, 30.0, 8.0)

# Convert Yes/No to 0/1
multi_preg = 1 if multi_preg == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0
clotting_disorder = 1 if clotting_disorder == "Yes" else 0
placenta_prob = 1 if placenta_prob == "Yes" else 0
preterm_labour = 1 if preterm_labour == "Yes" else 0
ecg_abnormal = 1 if ecg_abnormal == "Yes" else 0
uterine_contractions = 1 if uterine_contractions == "Yes" else 0
fetal_ecg = 1 if fetal_ecg == "Yes" else 0

# Predict
if st.button("🔍 Predict Risk Level"):
    input_df = pd.DataFrame([{
        "Age": age,
        "Weight (kg)": weight,
        "Height (cm)": height,
        "Pregnancy Number": preg_num,
        "Multiple Pregnancy": multi_preg,
        "Diabetes": diabetes,
        "Blood Clotting Disorder": clotting_disorder,
        "Placenta Problems": placenta_prob,
        "Preterm Labour": preterm_labour,
        "Maternal Heart Rate (bpm)": maternal_hr,
        "BP Systolic (mmHg)": sys_bp,
        "BP Diastolic (mmHg)": dia_bp,
        "Oxygen Saturation (%)": spo2,
        "Body Temperature (C)": temp,
        "Glucose Level (mg/dL)": glucose,
        "ECG Abnormal": ecg_abnormal,
        "Respiratory Rate (breaths/min)": resp_rate,
        "Uterine Contractions": uterine_contractions,
        "Fetal Heart Rate (bpm)": fetal_hr,
        "Fetal Movements": fetal_movements,
        "Fetal Position": fetal_position,
        "Amniotic Fluid Index (cm)": amniotic_index,
        "Fetal ECG Abnormal": fetal_ecg,
        "CBC WBC (x10^9/L)": cbc_wbc,
    }])

    # prediction = model.predict(input_df)[0]

    # st.subheader("🩺 Prediction Result")
    # st.success(f"Predicted Pregnancy Risk Level: {prediction}")



    prediction = model.predict(input_df)[0]

    st.subheader("🩺 Prediction Result")

    if prediction == "Low":
        st.success("✅ Low Risk Pregnancy\n\nEverything looks good. Regular check-ups are recommended.")
    elif prediction == "Medium":
        st.warning("⚠️ Medium Risk Pregnancy\n\nPlease monitor your health carefully and follow up with your doctor.")
    elif prediction == "High":
        st.error("🚨 High Risk Pregnancy\n\nImmediate medical attention may be required. Consult your healthcare provider.")
    else:
        st.info(f"Predicted Risk Level: {prediction}")
