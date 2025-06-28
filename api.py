from huggingface_hub import login
import os
from dotenv import load_dotenv

load_dotenv()

hftoken = os.getenv("HF_TOKEN")
login(token=hftoken) #My personal token

from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="jy46604790/Fake-News-Bert-Detect",
    framework="pt"  # Force PyTorch # Using a hugging face model which using pytorch tensors
)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/predict/")
def predict_fake_news(request: TextRequest):
    result = classifier(request.text)
    label_id = result[0]["label"]  # e.g., "LABEL_0" or "LABEL_1"
    
    # Map labels
    label_map = {
        "LABEL_0": "FAKE",
        "LABEL_1": "REAL"
    }
    
    readable_label = label_map.get(label_id, label_id)  # fallback to raw if unknown
    return {"label": readable_label, "score": result[0]["score"]}

