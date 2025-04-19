import streamlit as st
import pickle
import numpy as np

# Load model and preprocessing tools
model = pickle.load(open("yield_model.pkl", "rb"))
label_encoders, scaler = pickle.load(open("encoders_scaler.pkl", "rb"))

st.title("🌾 Agricultural Yield Prediction")

# Input fields
crop = st.selectbox("Crop Type", label_encoders['Crop_Type'].classes_)
irrigation = st.selectbox("Irrigation Type", label_encoders['Irrigation_Type'].classes_)
soil = st.selectbox("Soil Type", label_encoders['Soil_Type'].classes_)
season = st.selectbox("Season", label_encoders['Season'].classes_)

farm_area = st.number_input("Farm Area (acres)", min_value=0.1)
fertilizer = st.number_input("Fertilizer Used (tons)", min_value=0.0)
pesticide = st.number_input("Pesticide Used (kg)", min_value=0.0)
water = st.number_input("Water Usage (cubic meters)", min_value=0.0)

# Prepare input
input_data = [[
    label_encoders['Crop_Type'].transform([crop])[0],
    label_encoders['Irrigation_Type'].transform([irrigation])[0],
    label_encoders['Soil_Type'].transform([soil])[0],
    label_encoders['Season'].transform([season])[0],
    farm_area, fertilizer, pesticide, water
]]

# Scale numeric inputs
input_data[0][4:] = scaler.transform([input_data[0][4:]])[0]

# Predict
if st.button("Predict Yield"):
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Estimated Yield: {prediction:.2f} tons")

   
