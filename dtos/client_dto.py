from typing import Optional
from pydantic import BaseModel


class CreateClientDTO(BaseModel):
    firstname: str
    lastname: str
    city: str
    salary: float
    initial_deposit: Optional[float] = 0

class UpdateClientDTO(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    city: Optional[str] = None
    salary: Optional[float] = None