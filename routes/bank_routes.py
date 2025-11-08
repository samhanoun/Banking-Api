from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.connection import get_session
from controllers.bank_controller import create_new_bank, get_all_banks
from dtos.bank_dto import CreateBankDTO
from database.models.bank import Bank
from database.models.client import Client

router = APIRouter()

@router.post('/bank/new') # Endpoint
async def create_bank(data: CreateBankDTO):
    """
    Create a new bank.
    """
    try:
        response = create_new_bank(data)
        return JSONResponse(response['data'], response['status_code'])
    except Exception as msg:
        return JSONResponse(str(msg), 409)

@router.get('/bank')
async def fetch_all_banks():
    """
    Get all banks.
    """
    banks = get_all_banks()
    return JSONResponse({'banks': banks})

@router.post("/bank/{bank_id}/request_cb/{client_id}")
def request_cb(bank_id: int, client_id: int, db: Session = Depends(get_session)):
    """
    Request a credit card for a client.
    """
    bank = db.query(Bank).filter(Bank.id == bank_id).first()
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")

    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    if client.bank_id != bank_id:
        raise HTTPException(status_code=403, detail="Client does not belong to this bank")

    cb = bank.request_cb(client)
    db.add(cb)
    db.commit()
    return {"message": "Credit card requested successfully"}