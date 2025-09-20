from pydantic import BaseModel, EmailStr

# Schema é uma classe que herda de BaseModel do Pydantic.
# o Schema é uma representação dos dados que a API vai enviar ou receber.
# Ele define a estrutura e o formato dos dados, garantindo que eles estejam
# corretos e consistentes.
# É como se fosse o DTO (Data Transfer Object) em outras arquiteturas.


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
