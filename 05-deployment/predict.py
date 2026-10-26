import pickle
from fastapi import FastAPI

with open("pipeline.bin", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(lead: dict):
    # FastAPI автоматически превратит JSON-запрос в словарь
    prob = float(model.predict_proba([lead])[0, 1])
    return {
        "conversion_probability": round(prob, 3),
        "conversion": bool(prob >= 0.5)
    }