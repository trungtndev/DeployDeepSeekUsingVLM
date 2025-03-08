from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Define request body structure
class TextRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "DeepSeek R1 Distill API is running"}

@app.post("/generate/")
def generate_text(request: TextRequest):
    url = "http://localhost:8000/generate"
    payload = {"prompt": request.prompt}
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
