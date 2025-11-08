from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_session
from controllers import client_controller
from dtos.client_dto import CreateClientDTO, UpdateClientDTO
from database.models.bank import Bank
from database.models.client import Client

router = APIRouter()

@router.post("/bank/{bank_id}/client")
def create_client(bank_id: int, client: CreateClientDTO, db: Session = Depends(get_session)):
    """
    Create a new client for a bank.
    """
    bank = db.query(Bank).filter(Bank.id == bank_id).first()
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")
    client_obj = Client(**client.model_dump(), bank_id=bank_id)
    db.add(client_obj)
    db.commit()
    db.refresh(client_obj)
    return client_obj

@router.get("/client/{client_id}")
def get_client(client_id: int, db: Session = Depends(get_session)):
    """
    Get a client by ID.
    """
    return client_controller.get_client(db, client_id)

@router.put("/client/{client_id}")
def update_client(client_id: int, client: UpdateClientDTO, db: Session = Depends(get_session)):
    """
    Update a client by ID.
    """
    return client_controller.update_client(db, client_id, client)

@router.delete("/client/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_session)):
    """
    Delete a client by ID.
    """
    return client_controller.delete_client(db, client_id)
