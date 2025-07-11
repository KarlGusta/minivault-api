# MiniVault API

A lightweight local REST API that simulates a core feature of ModelVault's product, which is receiving a prompt and returning a generated response using a local (LLM GPT-2). Supports word-by-word streaming and logs all interactions locally.   

## How to Run

```bash
git clone https://github.com/KarlGusta/minivault-api.git
cd minivault-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload 
```

Notes:
- `logs/log.jsonl` will be created automatically after your first API call to `/generate`.
- The virtual environment (`venv/`) is excluded - use `requirements.txt` to install dependencies.

