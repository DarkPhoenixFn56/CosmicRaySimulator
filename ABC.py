import numpy as np
import pandas as pd
import streamlit as st
import joblib

# trained pipeline
model = joblib.load("best_model.pkl")

st.title("🌌 Cosmic Ray Classifier Simulator")
st.subheader("Cherenkov Telescope Event Prediction")

st.markdown("Enter the observed parameters:")

# Correct input sliders
fLength = st.slider("fLength", 0.0, 200.0, 100.0,key='fLength')
fWidth = st.slider("fWidth", 0.0, 20.0, 5.0,key='fWidth')
fWidth1 = 2.35  
fConc = st.slider("fConc", 0.0, 2000.0, 1000.0,key='fConc')
fConc1 = 0.32
fAsym = st.slider("fAsym",-1.0,1.0,0.0,key='fAsym')
fM3Long = st.slider("fM3Long", -2.0, 2.0, 0.2,key='fM3Long')
fM3Trans =st.slider("fM3Trans",0.0,180.0,20.0,key='fM3Trans')
fAlpha = st.slider("fAlpha", 0.0, 180.0, 20.0,key='fAlpha')
fDist = st.slider("fDist", 0.0, 350.0, 100.0,key='fDist')

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

# Prediction
if st.button("Predict Class"):
    prediction = model.predict(input_data)[0]
    probs = model.predict_proba(input_data)[0]

    label = "🌟 Gamma Ray" if prediction == 1 else "☄️ Hadron"
    st.success(f"Prediction: {label}")
    st.info(f"Confidence (Gamma): {probs[1]*100:.2f}%")

    st.write("📊 Probability Distribution:")
    st.bar_chart(pd.DataFrame({"Probability": probs}, index=["Hadron", "Gamma"]))
