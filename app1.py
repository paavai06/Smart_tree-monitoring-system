import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(layout="wide")

# -----------------------------
# Species list
# -----------------------------

species_list = [
"Hopea erosa","Aglaia malabarica","Vateria indica",
"Dipterocarpus bengalensis","Shorea talura",
"Hildegardia populifolia","Drypetes malabarica",
"Hydnocarpus macrocarpus","Prioria pinnata",
"Dipterocarpus indicus","Cynometra travancorica",
"Litsea kakkachensis","Santapauia madurensis",
"Madhuca ponuru","Shorea roxburghii",
"Cinnamomum riparium","Arenga wightii",
"Palaquium raeburghii","Semecarpus travancoricus",
"Gluta travancorica"
]

# -----------------------------
# Load dataset
# -----------------------------

data = pd.read_csv("tree_sensor_dataset.csv")

# -----------------------------
# Train model per species
# (same dataset — species-specific demo logic)
# -----------------------------

models = {}

for sp in species_list:
    X = data[["moisture","temperature","humidity","gas"]]
    y = data["survival"]

    model = RandomForestClassifier()
    model.fit(X, y)

    models[sp] = model

# -----------------------------
# UI Header
# -----------------------------

st.title("🌳 Smart Tree Survival Dashboard (Dataset Mode)")

species = st.selectbox("Select Species", species_list)

st.subheader("Enter Sensor Values")

col1, col2 = st.columns(2)

with col1:
    moisture = st.slider("Soil Moisture", 0.0, 100.0, 60.0)

    temperature = st.slider("Temperature (°C)", 10.0, 50.0, 30.0)

with col2:
    humidity = st.slider("Humidity (%)", 0.0, 100.0, 70.0)

    gas = st.slider("Gas Level", 0.0, 1000.0, 300.0)

# -----------------------------
# Prediction
# -----------------------------

model = models[species]

input_data = [[moisture, temperature, humidity, gas]]

prob = model.predict_proba(input_data)[0][1]

st.subheader("🌱 Survival Prediction")

if prob > 0.6:
    st.success(f"Healthy — Survival Probability: {prob*100:.2f}%")
elif prob > 0.4:
    st.warning(f"Moderate Risk — Probability: {prob*100:.2f}%")
else:
    st.error(f"High Risk — Probability: {prob*100:.2f}%")

# -----------------------------
# Dataset Insights
# -----------------------------

st.subheader("📊 Dataset Sensor Trends")

st.line_chart(data[["moisture","temperature","humidity","gas"]])

st.subheader("Dataset Overview")

st.dataframe(data.head(20))

healthy_rate = data["survival"].mean() * 100

st.metric("Overall Healthy Samples", f"{healthy_rate:.2f}%")