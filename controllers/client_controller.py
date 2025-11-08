from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.models.client import Client
from dtos.client_dto import CreateClientDTO, UpdateClientDTO

def get_client(db: Session, client_id: int):
    """
    Get a client by ID.
    """
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

def update_client(db: Session, client_id: int, client_data: UpdateClientDTO):
    """
    Update a client by ID.
    """
    client = get_client(db, client_id)
    for key, value in client_data.model_dump(exclude_unset=True).items():
        setattr(client, key, value)
    db.commit()
    db.refresh(client)
    return client

def delete_client(db: Session, client_id: int):
    """
    Delete a client by ID.
    """
    client = get_client(db, client_id)
    db.delete(client)
    db.commit()
    return {"message": "Client deleted successfully"}
