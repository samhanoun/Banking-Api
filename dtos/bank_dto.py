from typing import TypedDict
from pydantic import BaseModel


class CreateBankDTO(BaseModel):
    name: str

class ResponseCreateBankDTO(TypedDict):
    data: dict[str, int]
    status_code: int