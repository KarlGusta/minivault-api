from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from datetime import datetime
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import json
import os
import time

app = FastAPI()

# Load GPT-2 model and tokenizer once(on startup)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2") 
model.eval() # Set to evaluation mode

LOG_FILE = "logs/log.jsonl"

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_response(request: PromptRequest):
    prompt = request.prompt
    
    # Encode prompt and generate response using GPT-2
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    output_ids = model.generate(
        input_ids,
        max_length=100,
        num_return_sequences=1,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.9,
    )

    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Log prompt and full response
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": output_text
    }    
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    # Stream word-by-word
    def stream_response():
        for word in output_text.split():
            yield word + " "
            time.sleep(0.15)
            
    return StreamingResponse(stream_response(), media_type="text/plain")        