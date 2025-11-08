from pydantic import BaseModel
from datetime import datetime

class CreateTransactionDTO(BaseModel):
    amount: float
    type: str

from pydantic import ConfigDict

class TransactionDTO(BaseModel):
    id: int
    amount: float
    type: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
