"""
This is the main file of the application.
It contains the FastAPI application and the routes.
"""
from fastapi import FastAPI
from database.connection import get_session
from routes import bank_routes, client_routes, account_routes

api = FastAPI(
    title="Banking API",
    description="A simple API to manage banks, clients, and accounts.",
    version="1.0.0",
)

session = get_session()

api.include_router(bank_routes.router, prefix="/api")
api.include_router(client_routes.router, prefix="/api")
api.include_router(account_routes.router, prefix="/api")

@api.get("/")
def read_root():
    """
    Root endpoint of the API.
    """
    return {"message": "Welcome to the Banking API"}
