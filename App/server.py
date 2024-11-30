from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/predict")
def predict(data: dict):
    feature = np.array([list(data.values())])
    model = joblib.load('./Model/model.pkl')
    encoder = joblib.load('./Model/encoder.pkl')
    feature[:, [1, 2, 3]] = encoder.transform(feature[:, [1, 2, 3]])
    prediction = model.predict(feature)
    prediction = encoder.inverse_transform(prediction)
    return {"prediction": prediction[0]}