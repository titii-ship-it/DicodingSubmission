import streamlit as st
import pandas as pd
import joblib

# ======== Load Model dan Preprocessing ========
model = joblib.load("model/model.pkl")
feature_names = joblib.load("model/columns.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

# ======== Kolom yang diminta user ========
# Kolom yang kamu ingin user isi secara manual
manual_input = [
    'Age_at_enrollment', 'Debtor', 'Gender', 'Marital_status',
    'Previous_qualification_grade', 'Displaced', 'Admission_grade',
    'Scholarship_holder', 'Tuition_fees_up_to_date',
    'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_approved',
    'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_approved',
    'GDP', 'Inflation_rate', 'Unemployment_rate'
]

# ======== Streamlit Layout ========
st.set_page_config(page_title="Prediksi Status Mahasiswa", layout="centered")
st.title("🎓 Prediksi Status Mahasiswa")

with st.form("form_prediksi"):
    st.markdown("### 📋 Masukkan Data Mahasiswa")

    col1, col2 = st.columns(2)
    with col1:
        umur = st.number_input("Age at Enrollment", 15, 80, 18)
        debtor = st.selectbox("Debtor", [1, 0], format_func=lambda x: "Yes" if x else "No")
        gender = st.selectbox("Gender", [1, 0], format_func=lambda x: "Male" if x else "Female")
        marital = st.selectbox("Marital Status", [1, 2, 3, 4, 5, 6])
        prev_grade = st.number_input("Previous Qualification Grade", 0.0, 200.0, 130.0)
        displaced = st.selectbox("Displaced", [1, 0], format_func=lambda x: "Yes" if x else "No")
        admission = st.number_input("Admission Grade", 0.0, 200.0, 130.0)
        scholarship = st.selectbox("Scholarship Holder", [1, 0], format_func=lambda x: "Yes" if x else "No")

    with col2:
        tuition = st.selectbox("Tuition Paid", [1, 0], format_func=lambda x: "Yes" if x else "No")
        grade1 = st.number_input("1st Sem Grade", 0.0, 20.0, 12.0)
        approve1 = st.number_input("1st Sem Approved Units", 0, 10, 5)
        grade2 = st.number_input("2nd Sem Grade", 0.0, 20.0, 11.0)
        approve2 = st.number_input("2nd Sem Approved Units", 0, 10, 4)
        gdp = st.slider("GDP", -10.0, 10.0, 0.0)
        inflation = st.slider("Inflation Rate", -5.0, 5.0, 1.0)
        unemployment = st.slider("Unemployment Rate", 0.0, 20.0, 10.0)

    submit = st.form_submit_button("🔍 Prediksi")

# ======== Prediksi ========
if submit:
    # Siapkan input user
    user_values = {
        'Age_at_enrollment': umur,
        'Debtor': debtor,
        'Gender': gender,
        'Marital_status': marital,
        'Previous_qualification_grade': prev_grade,
        'Displaced': displaced,
        'Admission_grade': admission,
        'Scholarship_holder': scholarship,
        'Tuition_fees_up_to_date': tuition,
        'Curricular_units_1st_sem_grade': grade1,
        'Curricular_units_1st_sem_approved': approve1,
        'Curricular_units_2nd_sem_grade': grade2,
        'Curricular_units_2nd_sem_approved': approve2,
        'GDP': gdp,
        'Inflation_rate': inflation,
        'Unemployment_rate': unemployment
    }

    # Siapkan dataframe dengan semua kolom
    full_data = {col: 0 for col in feature_names}
    full_data.update(user_values)
    input_df = pd.DataFrame([full_data])[feature_names]  # pastikan urutan benar

    # Prediksi
    prediction = model.predict(input_df)[0]
    label = label_encoder.inverse_transform([prediction])[0]

    st.success(f"✅ Prediksi Status Mahasiswa: **{label}**")
