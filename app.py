import streamlit as st
import numpy as np
import pandas as pd
import time
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(layout="wide")

# -----------------------------
# Species List
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
# Species Survival Conditions
# (moisture, temp, humidity thresholds)
# -----------------------------

species_rules = {
sp: (np.random.randint(45,65),
     np.random.randint(33,38),
     np.random.randint(55,75))
for sp in species_list
}

# -----------------------------
# Dataset Generator
# -----------------------------

def generate_dataset(seed, thresholds):

    np.random.seed(seed)

    moisture = np.random.uniform(10,100,600)
    temp = np.random.uniform(20,45,600)
    humidity = np.random.uniform(30,95,600)
    gas = np.random.uniform(100,900,600)

    survival = (
        (moisture > thresholds[0]) &
        (temp < thresholds[1]) &
        (humidity > thresholds[2]) &
        (gas < 650)
    ).astype(int)

    return pd.DataFrame({
        "moisture": moisture,
        "temperature": temp,
        "humidity": humidity,
        "gas": gas,
        "survival": survival
    })

# -----------------------------
# Train Models (per species)
# -----------------------------

models = {}

for i, sp in enumerate(species_list):

    df = generate_dataset(i+1, species_rules[sp])

    X = df[["moisture","temperature","humidity","gas"]]
    y = df["survival"]

    model = RandomForestClassifier()
    model.fit(X,y)

    models[sp] = model

# -----------------------------
# Cloud Storage Simulation
# -----------------------------

if "cloud" not in st.session_state:
    st.session_state.cloud = pd.DataFrame(columns=[
        "tree_id","species",
        "moisture","temperature",
        "humidity","gas",
        "probability","status"
    ])

# -----------------------------
# UI Header
# -----------------------------

st.title("🌳 Smart Tree Survival Dashboard")

col1, col2 = st.columns(2)

with col1:
    tree_id = st.text_input("Tree ID")
    species = st.selectbox("Species", species_list)

with col2:
    stream = st.checkbox("Live Cloud Streaming")

# -----------------------------
# Live Sensor Simulation
# -----------------------------

def sensor_stream():

    return {
        "moisture": np.random.uniform(10,100),
        "temperature": np.random.uniform(20,45),
        "humidity": np.random.uniform(30,95),
        "gas": np.random.uniform(100,900)
    }

# -----------------------------
# Streaming Engine
# -----------------------------

if stream and tree_id != "":

    live = sensor_stream()

    model = models[species]

    input_data = [[
        live["moisture"],
        live["temperature"],
        live["humidity"],
        live["gas"]
    ]]

    prob = model.predict_proba(input_data)[0][1]
    status = "Healthy" if prob > 0.6 else "At Risk"

    row = {
        "tree_id": tree_id,
        "species": species,
        "moisture": round(live["moisture"],2),
        "temperature": round(live["temperature"],2),
        "humidity": round(live["humidity"],2),
        "gas": round(live["gas"],2),
        "probability": round(prob*100,2),
        "status": status
    }

    st.session_state.cloud = pd.concat(
        [st.session_state.cloud, pd.DataFrame([row])],
        ignore_index=True
    )

    time.sleep(1)
    st.rerun()

# -----------------------------
# Tree Monitoring Panel
# -----------------------------

if tree_id != "":

    data = st.session_state.cloud[
        st.session_state.cloud["tree_id"] == tree_id
    ]

    st.subheader(f"📊 Monitoring Tree: {tree_id}")

    if not data.empty:

        latest = data.iloc[-1]

        colA, colB = st.columns(2)

        with colA:
            st.metric("Samples Collected", len(data))
            st.metric("Survival Probability",
                      f"{latest['probability']}%")

        with colB:
            if latest["status"] == "Healthy":
                st.success("Status: Healthy 🌱")
            else:
                st.error("Status: At Risk ⚠")

        st.subheader("Sensor Fluctuation")

        st.line_chart(
            data[["moisture","temperature","humidity","gas"]]
        )

        # Alerts
        if latest["probability"] < 50:
            st.warning("🚨 CRITICAL ALERT — Immediate Action Needed")
        elif latest["probability"] < 65:
            st.info("⚠ Moderate Risk — Monitor Closely")

    else:
        st.info("Waiting for sensor data...")

# -----------------------------
# Cloud Overview
# -----------------------------

st.subheader("☁ Cloud Database View")

st.dataframe(st.session_state.cloud)