from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
import json
import os

app = FastAPI()

LOG_FILE = "logs/log.jsonl"

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_response(request: PromptRequest):
    prompt = request.prompt
    # Stubbed response (hardcoded)
    response = f"Stubbed response to: {prompt}"

    # Log interaction
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response
    }    
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    return {"response": response}    