from http import HTTPStatus


def test_root_deve_retornar_hello_world(client):
    """
    Esse teste tem três etapas (AAA):
    1. Arrange (preparar): configurar o ambiente e os dados necessários para
    o teste.
    2. Act (agir): executar a funcionalidade que está sendo testada.
    3. Assert (afirmar): verificar se o resultado obtido é o esperado.
    Ex: arrange->client, act->response, assert->assert
    """

    response = client.get('/')  # captura a resposta da requisição
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'World'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Yuri',
            'email': 'yuri@example.com',
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'Yuri',
        'email': 'yuri@example.com',
    }


def teste_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'id': 1, 'username': 'Yuri', 'email': 'yuri@example.com'}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': '1234',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }
