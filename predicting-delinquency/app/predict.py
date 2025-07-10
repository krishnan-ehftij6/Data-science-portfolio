# predict.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load RF model
model = joblib.load("model/rf_model.pkl")

# Initialize app
app = FastAPI()

# Define input schema
class CustomerInput(BaseModel):
    Age: float
    Income: float
    Credit_Score: float
    Credit_Utilization: float
    Missed_Payments: int
    Debt_to_Income_Ratio: float
    Account_Tenure: int

# Define predict route
@app.post("/predict")
def predict(input_data: CustomerInput):
    data = pd.DataFrame([input_data.dict()])
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    return {
        "prediction": int(prediction),
        "delinquency_probability": round(probability, 3)
    }


