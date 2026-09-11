from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Release Quality Demo API", version="1.0.0")

transactions = {}
idempotency_keys = set()

class Transaction(BaseModel):
    amount: float = Field(gt=0)
    source: str = Field(min_length=3)
    destination: str = Field(min_length=3)
    idempotency_key: str = Field(min_length=3)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/transactions", status_code=201)
def create_transaction(tx: Transaction):
    if tx.idempotency_key in idempotency_keys:
        raise HTTPException(status_code=409, detail="Duplicate transaction")
    transaction_id = f"TX-{len(transactions)+1:04d}"
    idempotency_keys.add(tx.idempotency_key)
    transactions[transaction_id] = {
        "transaction_id": transaction_id,
        "amount": tx.amount,
        "source": tx.source,
        "destination": tx.destination,
        "status": "AUTHORIZED",
    }
    return transactions[transaction_id]

@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: str):
    if transaction_id not in transactions:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transactions[transaction_id]
