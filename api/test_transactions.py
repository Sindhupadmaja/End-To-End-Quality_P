from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_create_valid_transaction():
    response = client.post("/transactions", json={
        "amount": 125.50,
        "source": "ACCOUNT-A",
        "destination": "ACCOUNT-B",
        "idempotency_key": "key-001"
    })
    assert response.status_code == 201
    assert response.json()["status"] == "AUTHORIZED"

def test_duplicate_transaction_is_rejected():
    payload = {
        "amount": 75,
        "source": "ACCOUNT-A",
        "destination": "ACCOUNT-B",
        "idempotency_key": "duplicate-001"
    }
    first = client.post("/transactions", json=payload)
    second = client.post("/transactions", json=payload)
    assert first.status_code == 201
    assert second.status_code == 409

def test_zero_amount_is_rejected():
    response = client.post("/transactions", json={
        "amount": 0,
        "source": "ACCOUNT-A",
        "destination": "ACCOUNT-B",
        "idempotency_key": "zero-001"
    })
    assert response.status_code == 422

def test_negative_amount_is_rejected():
    response = client.post("/transactions", json={
        "amount": -10,
        "source": "ACCOUNT-A",
        "destination": "ACCOUNT-B",
        "idempotency_key": "negative-001"
    })
    assert response.status_code == 422

def test_unknown_transaction_returns_404():
    response = client.get("/transactions/TX-9999")
    assert response.status_code == 404
