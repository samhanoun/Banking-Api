from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.base import Base
import database.models.bank
import database.models.client
import database.models.account
import database.models.credit_card
import database.models.transaction

db_url = 'sqlite:///database/banque.db'

def get_engine():
    return create_engine(url=db_url)

def get_session():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()