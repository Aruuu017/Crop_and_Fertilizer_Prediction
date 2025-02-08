import streamlit as st
import joblib
import numpy as np
import os

# ----------------- Load Models & Encoders -----------------
try:
    crop_model = joblib.load("decision_tree_model.pkl")  # Crop prediction model
    fertilizer_model = joblib.load("fertilizer_model.pkl")  # Fertilizer recommendation model
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()  # Stop execution if models fail to load

# Crop names mapping (update as per your dataset labels)
crop_mapping = {
    0: "Rice",
    1: "Wheat",
    2: "Maize",
    3: "Chickpea",
    4: "Kidney Beans",
    5: "Pigeon Peas",
    6: "Moth Beans",
    7: "Mung Beans",
    8: "Black Gram",
    9: "Lentil",
    10: "Pomegranate",
    11: "Banana",
    12: "Mango",
    13: "Grapes",
    14: "Watermelon",
    15: "Muskmelon",
    16: "Apple",
    17: "Orange",
    18: "Papaya",
    19: "Coconut",
    20: "Cotton",
    21: "Jute",
    22: "Coffee"
}

# ----------------- App Configuration -----------------
st.set_page_config(page_title="Smart Farming Assistant", layout="wide", page_icon="🌾")

# ----------------- Sidebar -----------------
st.sidebar.image("https://www.isaaa.org/kc/cropbiotechupdate/files/images/1232019115251PM.jpg", width=200)

st.sidebar.title("🌱 Smart Farming Assistant")
st.sidebar.write("Predict the best **crop** & **fertilizer** for your farm.")

# ----------------- Tabs for Navigation -----------------
tab1, tab2 = st.tabs(["🚜 Crop Prediction", "🧪 Fertilizer Recommendation"])

# ----------------- CROP PREDICTION TAB -----------------
with tab1:
    st.header("🚜 Crop Recommendation System")

    col1, col2 = st.columns(2)
    with col1:
        N = st.number_input("Nitrogen (N)", min_value=10, max_value=100, value=50, key="crop_n")
        P = st.number_input("Phosphorus (P)", min_value=10, max_value=100, value=50, key="crop_p")
        K = st.number_input("Potassium (K)", min_value=10, max_value=100, value=50, key="crop_k")
        temperature = st.slider("Temperature (°C)", 0.0, 50.0, 25.0, key="crop_temp")
    
    with col2:
        humidity = st.slider("Humidity (%)", 10.0, 100.0, 50.0, key="crop_humidity")
        ph = st.slider("Soil pH", 10.0, 14.0, 7.0, key="crop_ph")
        rainfall = st.slider("Rainfall (mm)", 10.0, 500.0, 100.0, key="crop_rainfall")

    if st.button("🌾 Predict Crop", key="crop_predict"):
        try:
            crop_input = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            predicted_crop_index = crop_model.predict(crop_input)[0]
            predicted_crop = crop_mapping.get(predicted_crop_index, "Unknown Crop")
            st.success(f"✅ Recommended Crop: **{predicted_crop}**")
        except Exception as e:
            st.error(f"Error in crop prediction: {e}")

# ----------------- FERTILIZER RECOMMENDATION TAB -----------------
with tab2:
    st.header("🧪 Fertilizer Recommendation System")

    col3, col4 = st.columns(2)
    with col3:
        nitrogen = st.number_input("Nitrogen", value=0.0, key="fert_n")
        phosphorus = st.number_input("Phosphorus", value=0.0, key="fert_p")
        potassium = st.number_input("Potassium", value=0.0, key="fert_k")
        temperature = st.number_input("Temperature", value=0.0, key="fert_temp")
    
    with col4:
        humidity = st.number_input("Humidity", value=0.0, key="fert_humidity")
        ph = st.number_input("pH", value=0.0, key="fert_ph")
        rainfall = st.number_input("Rainfall", value=0.0, key="fert_rainfall")
        soil_type = st.number_input("Soil Type (Categorical or Numeric)", value=0.0, key="fert_soil")
    
    if st.button("🔬 Recommend Fertilizer", key="fert_recommend"):
        try:
            input_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall, soil_type]])
            prediction = fertilizer_model.predict(input_data)
            fertilizer_mapping = {
                0: "Urea",
                1: "DAP (Diammonium Phosphate)",
                2: "MOP (Muriate of Potash)",
                3: "Super Phosphate",
                4: "Ammonium Sulphate",
                5: "Organic Manure",
                6: "NPK (Nitrogen, Phosphorus, Potassium)"
            }
            fertilizer_name = fertilizer_mapping.get(prediction[0], "Unknown Fertilizer")
            st.success(f"✅ Recommended Fertilizer: **{fertilizer_name}**")
        except Exception as e:
            st.error(f"Error in fertilizer recommendation: {e}")

# ----------------- Footer -----------------
st.markdown("---")
st.caption("Developed by Aryan Zende | © 2025 Smart Farming Assistant")
