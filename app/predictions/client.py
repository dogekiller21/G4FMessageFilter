from g4f import AsyncClient
from g4f.Provider import Blackbox


def get_client() -> AsyncClient:
    return AsyncClient(provider=Blackbox)
