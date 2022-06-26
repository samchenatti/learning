from aws_lambda_powertools.event_handler.api_gateway import Router
from src.product.product import create_product

router = Router()


@router.post('/produtos/')
def create_product_api():
    """
    Endpoint para criação de novos produtos
    """
    new_product = create_product(
        name=router.current_event.json_body.get('name'),
        price=router.current_event.json_body.get('price')
    )

    return new_product.json()
