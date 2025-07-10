# MiniVault API

A simple local REST API that simulates ModelVault's on-prem AI prompt/response system.

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

