from random import randint

from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import Base


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key= True, autoincrement= True)
    number = Column(Integer, nullable= False)
    balance = Column(Float, nullable= False, default= 0)

    client_id = Column(Integer, ForeignKey('client.id'), nullable= False)
    credit_card_id = Column(Integer, ForeignKey('credit_card.id'))

    client = relationship('Client', back_populates= 'account')
    credit_card = relationship('CreditCard', back_populates= 'account')
    transactions = relationship('Transaction', back_populates='account', cascade="all, delete-orphan")


    def __init__(self, initial_deposit: float):
        self.number = randint(1000000, 9999999)
        self.balance = initial_deposit

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def __repr__(self):
        return f"Compte {self.number} - {self.balance}Eur"
