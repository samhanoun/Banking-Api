from sqlalchemy import DECIMAL, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from database.models.account import Account


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key= True, autoincrement= True)
    firstname = Column(String(200), nullable= False)
    lastname = Column(String(200), nullable= False)
    city = Column(String(200))
    salary = Column(DECIMAL)

    bank_id = Column(Integer, ForeignKey('bank.id'), nullable= False)

    bank = relationship('Bank', back_populates= 'clients')
    account = relationship('Account', back_populates= 'client', uselist= False)

    def __init__(self, firstname: str, lastname: str, city: str, salary: float, initial_deposit: float = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.salary = salary
        self.account = Account(initial_deposit)

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"
