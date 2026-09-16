from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI(title="Bengaluru Real Estate Predictor API")

# Load the saved model weights and scaler
theta = np.load('model_weights.npy')
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# The 4 features we trained on
class HouseFeatures(BaseModel):
    total_sqft: float
    bath: float
    balcony: float
    bhk: float

@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Convert input to a numpy array
    input_data = np.array([[features.total_sqft, features.bath, features.balcony, features.bhk]])
    
    # Scale the input data
    input_scaled = scaler.transform(input_data)
    
    # Add the bias term (column of 1s)
    input_scaled = np.c_[np.ones(input_scaled.shape[0]), input_scaled]
    
    # Calculate the prediction
    prediction = input_scaled.dot(theta)
    
    return {"estimated_value_in_lakhs": round(prediction[0], 2)}