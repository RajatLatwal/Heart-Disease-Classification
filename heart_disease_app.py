import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Heart Disease Classifier", page_icon="💓")

st.title("💓 Heart Disease Prediction App")
st.write("Fill in the details below to predict whether someone has heart disease.")

# User Inputs
age = st.slider("Age", 18, 100, 50)
sex = st.radio("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (in mm Hg)", 80, 200, 120)
chol = st.number_input("Serum Cholestoral (in mg/dl)", 100, 600, 240)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"])
restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
exang = st.radio("Exercise-Induced Angina?", ["Yes", "No"])
oldpeak = st.number_input("ST depression induced by exercise", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (0 = Normal; 1 = Fixed Defect; 2 = Reversible Defect)", [0, 1, 2])

# Mapping Inputs
input_data = np.array([[
    age,
    1 if sex == "Male" else 0,
    cp,
    trestbps,
    chol,
    1 if fbs == "Yes" else 0,
    restecg,
    thalach,
    1 if exang == "Yes" else 0,
    oldpeak,
    slope,
    ca,
    thal
]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "💔 Heart Disease Detected" if prediction[0] == 1 else "💖 No Heart Disease Detected"
    st.success(f"Prediction: {result}")
