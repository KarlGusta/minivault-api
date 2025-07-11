# MiniVault API

A lightweight local REST API that simulates a core feature of ModelVault's product, which is receiving a prompt and returning a generated response using a local (LLM GPT-2). Supports word-by-word streaming and logs all interactions locally.   

---

## Features

- `POST /generate` endpoint accepts a prompt and streams the response.
- Uses a local GPT-2 model (no cloud APIs).
- Word-by-word streaming output.
- Logs all interactions to `logs/log.jsonl`
- Includes CLI tool and Postman collection for easy testing. 

## Stack

- **Python 3.12**
- **FastAPI** - For API
- **Transformers(HuggingFace)** - for local model inference
- **PyTorch** - model backend
- **pytest** - for testing

---

## How to Run

### 1: Clone and Install

```bash
git clone https://github.com/KarlGusta/minivault-api.git
cd minivault-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2: Start the server
```bash
uvicorn app:app --reload
```

The API will be available at: `http://localhost:8000`



### Testing Options

#### Option 1: Postman

Use the included Postman collection:

- Open `postman_collection.json` in Postman.
- Run the `Generate Response` request.

#### Options 2: Command-line(CLI)

Use the CLI tool:

```bash
python cli.py "Hello AI!"
```

Notes:
- `logs/log.jsonl` will be created automatically after your first API call to `/generate`.
- The virtual environment (`venv/`) is excluded - use `requirements.txt` to install dependencies.

