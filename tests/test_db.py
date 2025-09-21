from fastapi_zero.models import User


def test_create_user(session):
    # vamos passar os campos obrigatórios
    user = User(username='testuser', email='test@test', password='1234')

    session.add(user)
    # usa o commit para q as iinformações criadas na sessao seja trasnmitida
    # para o banco de dados
    session.commit()
    breakpoint()  # ponto de interrupção para depuração

    assert user.username == 'testuser'
