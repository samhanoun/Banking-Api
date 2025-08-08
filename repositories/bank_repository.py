from database.connection import get_session
from database.models.bank import Bank


class BankRepository:
    def __init__(self):
        self.session = get_session()

    def create(self, bank: 'Bank'):
        self.session.add(bank)
        self.session.commit()

    def find_by_name(self, name: str):
        return self.session.query(Bank).filter_by(name= name).first()
    
    def fetch_all(self):
        return self.session.query(Bank).all()
        