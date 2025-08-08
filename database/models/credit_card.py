from datetime import date
from random import randint
from typing import TYPE_CHECKING
from dateutil.relativedelta import relativedelta
from sqlalchemy import CHAR, Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

if TYPE_CHECKING:
    from database.models.account import Account

class CreditCard(Base):
    __tablename__ = 'credit_card'

    id = Column(Integer, primary_key= True, autoincrement= True)
    card_number = Column(String(20), nullable= False)
    cvv = Column(CHAR(3), nullable= False)
    expiry_date = Column(CHAR(5), nullable= False)

    account = relationship('Account', back_populates= 'credit_card', uselist= False)

    def __init__(self, account: 'Account'):
        self.card_number = self.generate_card_number()
        self.cvv = self.generate_cvv()
        self.expiry_date = self.generate_expiry_date()
        self.account = account

    def generate_card_number(self):
        numero = ''.join([str(randint(0, 9)) for _ in range(16)])
        return ' '.join([numero[i: i + 4] for i in range(0, 16, 4)])

    def generate_cvv(self):
        return ''.join([str(randint(0, 9)) for _ in range(3)])

    def generate_expiry_date(self):
        return (date.today() + relativedelta(years= 5)).strftime('%m/%y')

    def __repr__(self):
        return f"{self.card_number} - {self.cvv} - {self.expiry_date}"
