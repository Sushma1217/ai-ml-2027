
from pathlib import Path

import joblib
import pandas as pd
import torch
import torch.nn as nn
from fastapi import FastAPI

BASE_DIR = Path(__file__).resolve().parent.parent

# Must match the architecture used during training
class ChurnNetwork(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1)
        )

    def forward(self, x):
        return self.network(x)


app = FastAPI(title="Customer Churn Prediction API")

preprocessor = joblib.load(
    BASE_DIR / "churn_preprocessor.joblib"
)

input_size = len(preprocessor.get_feature_names_out())
model = ChurnNetwork(input_size)

model.load_state_dict(
    torch.load(
        BASE_DIR / "churn_model.pth",
        map_location="cpu",
        weights_only=True
    )
)
model.eval()


@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}


@app.post("/predict")
def predict(customer: dict):
    df = pd.DataFrame([customer])

    processed = preprocessor.transform(df)
    tensor = torch.tensor(processed, dtype=torch.float32)

    with torch.no_grad():
        logit = model(tensor)
        probability = torch.sigmoid(logit).item()

    return {
        "churn_probability": round(probability, 4),
        "prediction": "Yes" if probability >= 0.5 else "No"
    }
