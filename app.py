import streamlit as st
import numpy as np
import joblib

model = joblib.load(r"D:\ماشين مشاريع\Diabetes project\diabetes_model.pkl")

st.title("Diabetes Prediction System 🩺")

pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
blood_pressure = st.number_input("Blood Pressure")
skin_thickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

input_data = np.array([
    pregnancies, glucose, blood_pressure,
    skin_thickness, insulin, bmi, dpf, age
]).reshape(1, -1)

if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Diabetic ❌")
    else:
        st.success("Non-Diabetic ✅")