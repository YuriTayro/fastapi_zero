from pydantic import BaseModel, ConfigDict, EmailStr

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
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]
