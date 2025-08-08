"""
On veut gerer des banques
Une banque a un nom et une liste de clients
Un client a un nom prenom ville salaire comme attributs
Une banque peut ajouter un client, ce qui va creer automatiquement son compte
Un compte a un numero de 7 digits et un solde initial a 0, on peut retirer et deposer de l'argent sur le compte.
Une banque peut faire la demande d'une CB pour le compte d'un client
Une CB a un numero de 16 chiffres (XXXX XXXX XXXX XXXX) a un CVV de 3 chiffres (XXX) et une date d'expiration 5 ans apres la date de creation (MM/YY)
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from database.connection import get_session
from database.models.bank import Bank
from database.models.client import Client
from dtos.client_dto import CreateClientDTO
from routes import bank_routes

api = FastAPI()
session = get_session()

api.include_router(bank_routes.router)

@api.get('/')
async def root():
    return JSONResponse('Hello world', 201)

@api.post('/client/new/{bank_id}')
async def create_client(bank_id: int, data: CreateClientDTO):
    bank = session.query(Bank).filter_by(id= bank_id).first()
    if bank is None:
        return JSONResponse({"message": f"La banque avec l'ID '{bank_id}' n'existe pas"}, 404)
    client = Client(**data.model_dump())
    bank.register(client)
    session.add(client)
    session.commit()
    return JSONResponse({'id': client.id}, 201)

# Bank fait une requete de cb pour un client, l'api retourne les infos de la CB
@api.post('/bank/{bank_id}/request/{client_id}')
async def request_cb(bank_id: int, client_id: int):
    bank = session.query(Bank).filter_by(id= bank_id).first()
    if bank is None:
        return JSONResponse({"message": f"La banque avec l'ID '{bank_id}' n'existe pas"}, 404)
    client = session.query(Client).filter_by(id= client_id).first()
    if client is None:
        return JSONResponse({"message": f"Le client avec l'ID '{client_id}' n'existe pas"}, 404)
    
    cb = bank.request_cb(client)
    session.add(cb)
    session.commit()
    return JSONResponse({'cb': str(cb)}, 201)