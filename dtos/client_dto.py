from typing import Optional
from pydantic import BaseModel


class CreateClientDTO(BaseModel):
    firstname: str
    lastname: str
    city: str
    salary: float
    initial_deposit: Optional[float] = 0