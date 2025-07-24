import numpy as np
import pandas as pd
import streamlit as st
import joblib

# Load trained pipeline
model = joblib.load("best_model.pkl")

st.title("🌌 Cosmic Ray Classifier Simulator")
st.subheader("Cherenkov Telescope Event Prediction")

st.markdown("Enter the observed parameters:")

# Correct input sliders directly for model’s real features
fLength = st.slider("fLength", 0.0, 200.0, 120.0)
fWidth = st.slider("fWidth", 0.0, 50.0, 5.0)
fWidth1 = 2.35  # average value, or make a slider if you want
fConc = st.slider("fConc", 0.0, 2000.0, 1000.0)
fConc1 = 0.32
fAsym = 0.05
fM3Long = st.slider("fM3Long", -2.0, 2.0, 0.2)
fM3Trans = 1.12
fAlpha = st.slider("fAlpha", 0.0, 180.0, 20.0)
fDist = st.slider("fDist", 0.0, 300.0, 110.0)

# Prepare input DataFrame in correct column order
input_data = pd.DataFrame([{
    'fLength': fLength,
    'fWidth': fWidth,
    'fWidth1': fWidth1,
    'fConc': fConc,
    'fConc1': fConc1,
    'fAsym': fAsym,
    'fM3Long': fM3Long,
    'fM3Trans': fM3Trans,
    'fAlpha': fAlpha,
    'fDist': fDist
}])

st.write("🔍 Input sent to model:")
st.dataframe(input_data)

# Predict
if st.button("Predict Class"):
    prediction = model.predict(input_data)[0]
    probs = model.predict_proba(input_data)[0]

    label = "🌟 Gamma Ray" if prediction == 1 else "☄️ Hadron"
    st.success(f"Prediction: {label}")
    st.info(f"Confidence (Gamma): {probs[1]*100:.2f}%")

    st.write("📊 Probability Distribution:")
    st.bar_chart(pd.DataFrame({"Probability": probs}, index=["Hadron", "Gamma"]))
