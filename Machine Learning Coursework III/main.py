import joblib
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Player(BaseModel):
    features: list

def load_model():
    model = joblib.load('model.joblib')
    encoder = joblib.load('label_encoder.joblib')
    scaler = joblib.load('scaler.joblib')
    return model, encoder, scaler
model, encoder, scaler = load_model()

@app.post("/predict")
def predict(data : Player):
    try:
        # Convert input data to NumPy array
        features = np.array(data.features).reshape(1, -1)
        
        # Apply scaling
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)
        
        return {"predicted_value": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
def home():
    return {"message": "KNN Model API is running!"}

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)