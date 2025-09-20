import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


# Bloco de testes reutilizaveis
@pytest.fixture
def client():
    return TestClient(app)
