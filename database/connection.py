from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = 'sqlite:///database/banque.db'

def get_engine():
    return create_engine(url= db_url)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind= engine)
    return Session()