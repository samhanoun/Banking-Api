import pytest
from fastapi.testclient import TestClient
from main import api
from database.connection import get_session
from database.models.bank import Bank
from database.models.client import Client

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

def test_create_client(db_session, test_bank):
    client_data = {
        "firstname": "John",
        "lastname": "Doe",
        "city": "New York",
        "salary": 50000.0,
        "initial_deposit": 0,
    }
    response = client.post(f"/api/bank/{test_bank.id}/client", json=client_data)
    assert response.status_code == 200
    assert response.json()["id"] is not None

def test_get_client(db_session, test_bank):
    client_obj = Client(firstname="Jane", lastname="Doe", city="London", salary=60000.0, bank_id=test_bank.id)
    db_session.add(client_obj)
    db_session.commit()
    db_session.refresh(client_obj)

    response = client.get(f"/api/client/{client_obj.id}")
    assert response.status_code == 200
    assert response.json()["firstname"] == "Jane"

def test_update_client(db_session, test_bank):
    client_obj = Client(firstname="Jim", lastname="Beam", city="Kentucky", salary=70000.0, bank_id=test_bank.id)
    db_session.add(client_obj)
    db_session.commit()
    db_session.refresh(client_obj)

    update_data = {"city": "Boston"}
    response = client.put(f"/api/client/{client_obj.id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["city"] == "Boston"

def test_delete_client(db_session, test_bank):
    client_obj = Client(firstname="Jack", lastname="Daniels", city="Tennessee", salary=80000.0, bank_id=test_bank.id)
    db_session.add(client_obj)
    db_session.commit()
    db_session.refresh(client_obj)

    response = client.delete(f"/api/client/{client_obj.id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Client deleted successfully"
