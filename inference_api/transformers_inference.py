from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Load the transformer model
model = pipeline("feature-extraction", model="sentence-transformers/all-MiniLM-L6-v2")

@app.post("/vectorize/")
async def vectorize(text: str):
    """
    API to generate vector representations for the given text.
    """
    vector = model(text).tolist()
    return {"vector": vector}