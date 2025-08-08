from sqlalchemy.orm import declarative_base, DeclarativeMeta

from database.connection import get_engine

Base : DeclarativeMeta = declarative_base()
engine = get_engine()

from database.models.account import Account
from database.models.bank import Bank
from database.models.client import Client
from database.models.credit_card import CreditCard

Base.metadata.create_all(bind= engine)