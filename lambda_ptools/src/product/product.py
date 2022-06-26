from pydantic import BaseModel


class Product(BaseModel):
    """
    Representa um produto
    """
    name: str
    price: float


def create_product(name: str, price: float) -> Product:
    """
    Cria um novo produto
    """
    return Product(name=name, price=price)
