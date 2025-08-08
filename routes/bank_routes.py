from fastapi import APIRouter
from fastapi.responses import JSONResponse

from controllers.bank_controller import create_new_bank, get_all_banks
from dtos.bank_dto import CreateBankDTO

router = APIRouter()

@router.post('/bank/new') # Endpoint
async def create_bank(data: CreateBankDTO):
    try:
        response = create_new_bank(data)
        return JSONResponse(response['data'], response['status_code'])
    except Exception as msg:
        return JSONResponse(str(msg), 409)

@router.get('/bank')
async def fetch_all_banks():
    banks = get_all_banks()
    return JSONResponse({'banks': banks})