from fastapi_zero.models import User


def test_create_user():
    # vamos passar os campos obrigatórios
    user = User(username='testuser', email='test@test', password='1234')

    assert user.username == 'testuser'
