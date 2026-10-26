import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv("tree_constraint_dataset.csv")

X = data[["temperature", "humidity"]]
y = data["status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model accuracy:", model.score(X_test, y_test))

joblib.dump(model, "tree_model.pkl")