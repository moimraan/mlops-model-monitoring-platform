import mlflow.pyfunc
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

model = mlflow.pyfunc.load_model("models:/model/latest")


@app.post("/predict")

def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return {"prediction": prediction.tolist()}
