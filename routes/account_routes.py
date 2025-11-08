from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_session
from controllers import account_controller
from dtos.transaction_dto import CreateTransactionDTO
from database.models.account import Account

router = APIRouter()

@router.post("/account/{account_id}/deposit")
def deposit(account_id: int, transaction: CreateTransactionDTO, db: Session = Depends(get_session)):
    """
    Deposit money into an account.
    """
    return account_controller.deposit(db, account_id, transaction.amount)

@router.post("/account/{account_id}/withdraw")
def withdraw(account_id: int, transaction: CreateTransactionDTO, db: Session = Depends(get_session)):
    """
    Withdraw money from an account.
    """
    return account_controller.withdraw(db, account_id, transaction.amount)

@router.get("/account/{account_id}/transactions")
def get_transactions(account_id: int, db: Session = Depends(get_session)):
    """
    Get the transaction history of an account.
    """
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account.transactions
