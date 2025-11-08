from database.models.bank import Bank
from dtos.bank_dto import CreateBankDTO, ResponseCreateBankDTO
from repositories.bank_repository import BankRepository

repository = BankRepository()

def create_new_bank(data: CreateBankDTO) -> ResponseCreateBankDTO:
    """
    Create a new bank.
    """
    existing_bank = repository.find_by_name(data.name)
    if existing_bank is not None:
        raise Exception(f"La banque '{data.name}' existe deja")
    bank = Bank(name= data.name)
    repository.create(bank)
    return {
        'data': {'id': bank.id},
        'status_code': 201
    }

def get_all_banks():
    """
    Get all banks.
    """
    banks = repository.fetch_all()
    return [str(bank) for bank in banks]