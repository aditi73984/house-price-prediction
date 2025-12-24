from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
with open("model/house_model.pkl", "rb") as f:
    model = pickle.load(f)

class HouseData(BaseModel):
    OverallQual: int
    GrLivArea: int
    GarageCars: int
    TotalBsmtSF: int

@app.post("/predict")
def predict_price(data: HouseData):
    input_data = np.array([[data.OverallQual, data.GrLivArea,
                             data.GarageCars, data.TotalBsmtSF]])
    prediction = model.predict(input_data)[0]
    return {"predicted_price": round(prediction, 2)}
