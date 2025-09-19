from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_hello_world():
    """
    Esse teste tem três etapas (AAA):
    1. Arrange (preparar): configurar o ambiente e os dados necessários para
    o teste.
    2. Act (agir): executar a funcionalidade que está sendo testada.
    3. Assert (afirmar): verificar se o resultado obtido é o esperado.
    """
    client = TestClient(app)
    response = client.get('/') #captura a resposta da requisição
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'World'}
