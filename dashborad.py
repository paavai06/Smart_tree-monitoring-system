import streamlit as st
import numpy as np
import pandas as pd
import time
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(layout="wide")

# -------------------------
# Species List
# -------------------------

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

# -------------------------
# Dataset Generator
# -------------------------

def generate_data(seed):
    np.random.seed(seed)
    moisture = np.random.randint(10, 100, 500)
    temp = np.random.randint(20, 45, 500)
    humidity = np.random.randint(30, 100, 500)
    light = np.random.randint(30, 100, 500)

    survival = ((moisture > 40) &
                (temp < 38) &
                (humidity > 50)).astype(int)

    return pd.DataFrame({
        "moisture": moisture,
        "temperature": temp,
        "humidity": humidity,
        "light": light,
        "survival": survival
    })

# -------------------------
# Train Model per Species
# -------------------------

models = {}

for i, sp in enumerate(species_list):
    df = generate_data(i+1)
    X = df[["moisture","temperature","humidity","light"]]
    y = df["survival"]
    model = RandomForestClassifier()
    model.fit(X, y)
    models[sp] = model

# -------------------------
# Cloud Database Simulation
# -------------------------

if "cloud_data" not in st.session_state:
    st.session_state.cloud_data = pd.DataFrame(columns=[
        "tree_id","species","moisture","temperature",
        "humidity","light","probability","status"
    ])

# -------------------------
# Dashboard UI
# -------------------------

st.title("🌳 Smart Tree Survival Monitoring System")

col1, col2 = st.columns(2)

with col1:
    tree_id = st.text_input("Enter Tree ID")
    species = st.selectbox("Select Species", species_list)

with col2:
    auto_stream = st.checkbox("Enable Live Cloud Streaming")

# -------------------------
# Live Data Simulation
# -------------------------

def generate_live_data():
    return {
        "moisture": np.random.randint(10,100),
        "temperature": np.random.randint(20,45),
        "humidity": np.random.randint(30,100),
        "light": np.random.randint(30,100)
    }

if auto_stream and tree_id != "":
    live = generate_live_data()
    model = models[species]

    input_data = [[live["moisture"], live["temperature"],
                   live["humidity"], live["light"]]]

    prob = model.predict_proba(input_data)[0][1]
    status = "Healthy" if prob > 0.6 else "At Risk"

    new_row = {
        "tree_id": tree_id,
        "species": species,
        "moisture": live["moisture"],
        "temperature": live["temperature"],
        "humidity": live["humidity"],
        "light": live["light"],
        "probability": round(prob*100,2),
        "status": status
    }

    st.session_state.cloud_data = pd.concat(
        [st.session_state.cloud_data, pd.DataFrame([new_row])],
        ignore_index=True
    )

    time.sleep(1)
    st.rerun()

# -------------------------
# Tree Tracking
# -------------------------

if tree_id != "":
    tree_data = st.session_state.cloud_data[
        st.session_state.cloud_data["tree_id"] == tree_id
    ]

    st.subheader(f"📊 Tree ID: {tree_id} Monitoring")

    if not tree_data.empty:

        st.write("Total Samples Collected:",
                 len(tree_data))

        latest = tree_data.iloc[-1]

        st.metric("Latest Survival Probability",
                  f"{latest['probability']}%")

        if latest["status"] == "Healthy":
            st.success("Status: Healthy 🌱")
        else:
            st.error("Status: At Risk ⚠")

        st.line_chart(
            tree_data[["moisture","temperature","humidity","light"]]
        )

        # Alert System
        if latest["probability"] < 50:
            st.warning("🚨 ALERT: Immediate Intervention Required!")
    else:
        st.info("No data available for this Tree ID.")

# -------------------------
# Full Cloud View
# -------------------------

st.subheader("☁ Cloud Database View")
st.dataframe(st.session_state.cloud_data)