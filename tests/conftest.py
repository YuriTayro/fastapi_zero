import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


# Bloco de testes reutilizaveis
@pytest.fixture
def client():
    return TestClient(app)

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi_zero.models import table_registry

def session():
    #cria a conexão com o banco de dados em memória
    engine = create_engine('sqlite:///:memory:')
    #vai criar todas as tabelas no banco de dados em memória
    table_registry.metadata.create_all(engine)
    # abrir a sessão com o banco de dados em memória
    with Session(engine) as session:
        yield session
