import numpy as np
import pandas as pd

np.random.seed(42)

rows = 3000

temperature = np.random.uniform(20, 45, rows)
humidity = np.random.uniform(30, 95, rows)
gas_level = np.random.uniform(100, 900, rows)
soil_moisture = np.random.uniform(10, 100, rows)

# Survival logic (biological stress model)
survival = (
    (temperature < 37) &
    (humidity > 50) &
    (gas_level < 600) &
    (soil_moisture > 40)
).astype(int)

dataset = pd.DataFrame({
    "temperature": temperature,
    "humidity": humidity,
    "gas_level": gas_level,
    "soil_moisture": soil_moisture,
    "survival": survival
})

dataset.to_csv("tree_sensor_dataset.csv", index=False)

print("Dataset generated successfully!")
print(dataset.head())