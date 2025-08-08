from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from database.models.client import Client

class ClientNotFoundException(Exception):
    def __init__(self, client: 'Client') -> None:
        super().__init__(f"Le client '{client.firstname} {client.lastname}' ne fait pas partie de la banque")