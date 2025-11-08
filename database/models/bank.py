
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.base import Base
from database.models.credit_card import CreditCard


if TYPE_CHECKING:
    from database.models.client import Client

class Bank(Base):
    __tablename__ = 'bank'
    
    id : Mapped[int] = mapped_column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(200), nullable= False)

    clients = relationship('Client', back_populates= 'bank', uselist= True) # type: ignore

    def __init__(self, name: str):
        self.name = name
        self.clients : list['Client'] = []

    def register(self, client: 'Client'):
        self.clients.append(client)

    def request_cb(self, client: 'Client'):
        cb = CreditCard(client.account)
        return cb
    
    def __repr__(self):
        return f"{self.name}"
