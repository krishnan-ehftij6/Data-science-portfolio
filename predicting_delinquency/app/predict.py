# predict.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load RF model
model = joblib.load("model/rf_model.pkl")

# Initialize app
app = FastAPI()

# Define input schema with validation
class CustomerInput(BaseModel):
    Age: float = Field(..., ge=18, le=100)
    Income: float = Field(..., ge=0)
    Credit_Score: float = Field(..., ge=300, le=850)
    Credit_Utilization: float = Field(..., ge=0, le=1)
    Missed_Payments: int = Field(..., ge=0)
    Debt_to_Income_Ratio: float = Field(..., ge=0, le=2)
    Account_Tenure: int = Field(..., ge=0)

# Define predict route
@app.post("/predict")
def predict(input_data: CustomerInput):
    logging.info(f"Received input: {input_data.dict()}")
    data = pd.DataFrame([input_data.dict()])
    
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    
    result = {
        "prediction": int(prediction),
        "delinquency_probability": round(probability, 3)
    }

    logging.info(f"Prediction result: {result}")
    return result
