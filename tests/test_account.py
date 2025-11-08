import pytest
from fastapi.testclient import TestClient
from main import api
from database.connection import get_session
from database.models.bank import Bank
from database.models.client import Client
from database.models.account import Account

client = TestClient(api)

@pytest.fixture(scope="function")
def db_session():
    session = get_session()
    yield session
    session.rollback()

@pytest.fixture(scope="function")
def test_bank(db_session):
    bank = Bank(name="Test Bank")
    db_session.add(bank)
    db_session.commit()
    db_session.refresh(bank)
    return bank

@pytest.fixture(scope="function")
def test_client(db_session, test_bank):
    client_obj = Client(firstname="John", lastname="Doe", city="New York", salary=50000.0, initial_deposit=0, bank_id=test_bank.id)
    db_session.add(client_obj)
    db_session.commit()
    db_session.refresh(client_obj)
    return client_obj

def test_deposit(db_session, test_client):
    account = test_client.account
    initial_balance = account.balance

    response = client.post(f"/api/account/{account.id}/deposit", json={"amount": 100.0, "type": "deposit"})
    assert response.status_code == 200
    assert response.json()["balance"] == initial_balance + 100.0

def test_withdraw(db_session, test_client):
    account = test_client.account
    account.balance = 200.0
    db_session.commit()

    response = client.post(f"/api/account/{account.id}/withdraw", json={"amount": 50.0, "type": "withdrawal"})
    assert response.status_code == 200
    assert response.json()["balance"] == 150.0

def test_get_transactions(db_session, test_client):
    account = test_client.account
    client.post(f"/api/account/{account.id}/deposit", json={"amount": 100.0, "type": "deposit"})
    client.post(f"/api/account/{account.id}/withdraw", json={"amount": 50.0, "type": "withdrawal"})

    response = client.get(f"/api/account/{account.id}/transactions")
    assert response.status_code == 200
    assert len(response.json()) == 2
