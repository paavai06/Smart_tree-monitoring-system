import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Create models folder
if not os.path.exists("models"):
    os.makedirs("models")

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

def generate_species_data(seed, moisture_threshold, temp_threshold, humidity_threshold):
    np.random.seed(seed)

    moisture = np.random.randint(10, 100, 600)
    temp = np.random.randint(20, 45, 600)
    humidity = np.random.randint(30, 100, 600)
    light = np.random.randint(30, 100, 600)

    survival = (
        (moisture > moisture_threshold) &
        (temp < temp_threshold) &
        (humidity > humidity_threshold)
    ).astype(int)

    return pd.DataFrame({
        "moisture": moisture,
        "temperature": temp,
        "humidity": humidity,
        "light": light,
        "survival": survival
    })

# Different thresholds per species (species-specific logic)
species_conditions = {
"Hopea erosa": (50, 35, 60),
"Aglaia malabarica": (45, 36, 55),
"Vateria indica": (55, 34, 65),
"Dipterocarpus bengalensis": (60, 33, 70),
"Shorea talura": (50, 37, 60),
"Hildegardia populifolia": (45, 38, 55),
"Drypetes malabarica": (55, 35, 65),
"Hydnocarpus macrocarpus": (50, 36, 60),
"Prioria pinnata": (65, 32, 75),
"Dipterocarpus indicus": (60, 34, 70),
"Cynometra travancorica": (70, 32, 80),
"Litsea kakkachensis": (50, 36, 60),
"Santapauia madurensis": (55, 35, 70),
"Madhuca ponuru": (45, 38, 55),
"Shorea roxburghii": (50, 37, 60),
"Cinnamomum riparium": (60, 34, 70),
"Arenga wightii": (50, 36, 65),
"Palaquium raeburghii": (55, 35, 70),
"Semecarpus travancoricus": (60, 34, 75),
"Gluta travancorica": (65, 33, 75)
}

for i, species in enumerate(species_list):
    thresholds = species_conditions[species]

    df = generate_species_data(
        seed=i+1,
        moisture_threshold=thresholds[0],
        temp_threshold=thresholds[1],
        humidity_threshold=thresholds[2]
    )

    X = df[["moisture","temperature","humidity","light"]]
    y = df["survival"]

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    filename = species.replace(" ", "_") + ".pkl"
    joblib.dump(model, f"models/{filename}")

    print(f"Model trained and saved for {species}")

print("All species models trained successfully.")