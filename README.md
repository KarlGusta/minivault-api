# MiniVault API

A simple local REST API that simulates ModelVault's om-prem AI prompt/response system.

## How to Run

```bash
git clone https://github.com/KarlGusta/minivault-api.git
cd minivault-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload 