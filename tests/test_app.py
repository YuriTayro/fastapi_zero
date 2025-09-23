from http import HTTPStatus

from fastapi_zero.schemas import UserPublic


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
            'username': 'Test',
            'email': 'test@example.com',
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'Test',
        'email': 'test@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
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


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_update_integrity_error(client, user):
    # Criando um registro para "fausto"
    client.post(
        '/users',
        json={
            'username': 'fausto',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )

    # Alterando o user.username das fixture para fausto
    response = client.put(
        f'/users/{user.id}',
        json={
            'username': 'fausto',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username or Email already exist'}
