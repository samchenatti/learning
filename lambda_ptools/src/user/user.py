from pydantic import BaseModel


class User(BaseModel):
    """
    Representa um usuário
    """
    name: str
    age: int


def create_user(name: str, age: int) -> User:
    """
    Emula a criação de um novo usuário
    """
    return User(name=name, age=age)
