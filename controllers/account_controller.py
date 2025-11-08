from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.models.account import Account
from database.models.transaction import Transaction

def deposit(db: Session, account_id: int, amount: float):
    """
    Deposit money into an account.
    """
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    account.balance += amount
    transaction = Transaction(amount=amount, type="deposit", account_id=account.id)
    db.add(transaction)
    db.commit()
    db.refresh(account)
    return account

def withdraw(db: Session, account_id: int, amount: float):
    """
    Withdraw money from an account.
    """
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    if account.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    account.balance -= amount
    transaction = Transaction(amount=amount, type="withdrawal", account_id=account.id)
    db.add(transaction)
    db.commit()
    db.refresh(account)
    return account
