from datetime import datetime

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session):
    new_user = User(username='testuser', email='test@test', password='1234')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'testuser'))

    # Verifica se os dados fixos estão corretos
    assert user.id is not None
    assert user.username == 'testuser'

    # A verificação importante:
    # Apenas garante que um objeto datetime foi criado
    assert isinstance(user.created_at, datetime)
