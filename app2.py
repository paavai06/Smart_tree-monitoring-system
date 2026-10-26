import streamlit as st
import joblib

model = joblib.load("tree_model.pkl")

st.title("🌳 Constraint-Based Tree Survival Model")

temp = st.slider("Temperature", 20.0, 45.0, 30.0)
humidity = st.slider("Humidity", 20.0, 95.0, 70.0)

prediction = model.predict([[temp, humidity]])[0]

st.subheader("Prediction")

if prediction == "Healthy":
    st.success("🌱 Healthy")

elif prediction == "Vulnerable":
    st.warning("⚠ Vulnerable")

else:
    st.error("❌ Dead")