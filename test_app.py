from fastapi.testclient import TestClient
from app import app
import os
import json

client = TestClient(app)

def test_generate_endpoint_success():
    payload = {"prompt": "Hello AI!"}
    response = client.post("/generate", json=payload)

    assert response.status_code == 200
    assert len(response.text.strip()) > 0

def test_log_file_created():
    assert os.path.exists("logs/log.jsonl")

def test_log_contains_last_interaction():
    with open("logs/log.jsonl", "r") as f:
        lines = f.readlines()
        assert len(lines) > 0
        last = json.loads(lines[-1])
        assert "prompt" in last
        assert "response" in last        