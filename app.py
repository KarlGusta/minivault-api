from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from datetime import datetime
import json
import os
import time

app = FastAPI()

LOG_FILE = "logs/log.jsonl"

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_response(request: PromptRequest):
    prompt = request.prompt
    
    response_text = f"Stubbed response to: {prompt}"

    # Log the full interaction before streaming
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response_text
    }    
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    # Stream the response word-by-word
    def stream_response():
        for word in response_text.split():
            yield word + " "
            time.sleep(0.2) # Simulate token streaming
            
    return StreamingResponse(stream_response(), media_type="text/plain")        