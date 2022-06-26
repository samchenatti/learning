from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver, content_types
from src.user.user import create_user
from src.product.product import create_product
from pydantic import ValidationError
from aws_lambda_powertools.event_handler.api_gateway import Response

app = APIGatewayRestResolver(strip_prefixes=['/api/v0'])


@app.post('/usuarios/')
def create_user_api():
    """
    Endpoint para criação de novos usuários
    """
    new_user = create_user(
        name=app.current_event.json_body.get('name'),
        age=app.current_event.json_body.get('age')
    )

    return new_user.json()


@app.get('/usuarios/<id_usuario>')
def get_user_api(id_usuario: int):
    """
    Endpoint para busca de usuario por id
    """

    return {'mensagem': f'Usuario com id {id_usuario} nao encontrado'}


@app.post('/produtos/')
def create_product_api():
    """
    Endpoint para criação de novos produtos
    """
    new_product = create_product(
        name=app.current_event.json_body.get('name'),
        price=app.current_event.json_body.get('price')
    )

    return new_product.json()


@app.exception_handler(ValidationError)
def handle_validation_error(error: ValidationError):
    """
    Trata exceções do tipo ValidationError e as retorna de uma forma
    compreensive para o usuário
    """
    return Response(
        status_code=500,
        content_type=content_types.APPLICATION_JSON,
        body=error.json()
    )


def lambda_handler(event: dict, context: dict) -> dict:
    """
    Exemplo de um AWS Lambda Handler utilizando o Event Handler do Lambda
    Power Tools

    Args:
        event: representa um evento de integração com a lambda, como os feitos
            através de um API Gateway ou SQS. Os campos podem variar de acordo
            com a fonte do evento
        context: carrega informações sobre o contexto/runtime da lambda

    Returns:
        A Lambda tem que retornar uma dicionário no formato esperado por quem
        originou o evento. O próprio Event Handler se encarrega de fazer isso.
    """
    return app(event=event, context=context)
