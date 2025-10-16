from fastapi.testclient import TestClient
from main import app
import httpx
from httpx import AsyncClient
import pytest

client = TestClient(app)

url = "https://catfact.ninja/fact"

fact = httpx.get(url).json()["fact"]

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = client.get("/me")
    assert response.status_code == 200

