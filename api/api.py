from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class TextRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "DeepSeek R1 Distill API is running"}

@app.post("/generate/")
def generate_text(request: TextRequest):
    url = "http://localhost:8000/generate"
    payload = {"prompt": request.prompt}

    try:
        response = requests.post(url, json=payload, timeout=10)
        print("🔹 VLLM Response Status Code:", response.status_code)
        print("🔹 VLLM Response Content:", response.text)

        response.raise_for_status()  # Raise error for HTTP issues
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error contacting VLLM server: {str(e)}")
    except ValueError:
        raise HTTPException(status_code=500, detail="Invalid response from VLLM server")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
