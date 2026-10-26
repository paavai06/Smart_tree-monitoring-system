import numpy as np
import pandas as pd

np.random.seed(42)

rows = 2000

temperature = np.random.uniform(20, 45, rows)
humidity = np.random.uniform(20, 95, rows)

status = []

for t, h in zip(temperature, humidity):

    if 22 <= t <= 32 and 60 <= h <= 90:
        status.append("Healthy")

    elif (32 < t <= 38) or (40 <= h < 60):
        status.append("Vulnerable")

    else:
        status.append("Dead")

dataset = pd.DataFrame({
    "temperature": temperature,
    "humidity": humidity,
    "status": status
})

dataset.to_csv("tree_constraint_dataset.csv", index=False)

print("Dataset created!")
print(dataset.head())