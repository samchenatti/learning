from src.user.user import create_user
from src.product.product import create_product
import json
from pydantic import ValidationError
import logging

logger = logging.getLogger()


def lambda_handler(event: dict, context: dict) -> dict:
    """
    Exemplo clássico de um AWS Lambda Handler

    Args:
        event: representa um evento de integração com a lambda, como os feitos
            através de um API Gateway ou SQS. Os campos podem variar de acordo
            com a fonte do evento
        context: carrega informações sobre o contexto/runtime da lambda

    Returns:
        A Lambda tem que retornar uma dicionário no formato esperado por quem
        originou o evento
    """
    status_code = 500
    return_body = ''

    method = event['httpMethod']
    path = event['path']
    body = json.loads(event['body'])

    # Normalmente, quando estamos lidando com a integração de um API Gateway
    # nós temos que fazer um dispatch do evento manualmente; isto é, analisar
    # a rota e extrair os parâmetros para decidir como tratar o evento

    is_create_user = method == 'POST' and path == '/api/v0/usuarios/'
    is_create_product = method == 'POST' and path == '/api/v0/produtos/'

    try:
        if is_create_user:
            try:
                new_user = create_user(
                    name=body['name'],
                    age=body['age']
                )

                status_code = 200
                return_body = new_user.json()

            except ValidationError as err:
                status_code = 500
                return_body = err.json()

        if is_create_product:
            try:
                new_product = create_product(
                    name=body['name'],
                    price=body['price']
                )

                status_code = 200
                return_body = new_product.json()

            except ValidationError as err:
                status_code = 500
                return_body = err.json()

    except Exception as exception:
        logger.exception(msg='unknown error')

        status_code = 500
        return_body = 'Erro desconhecido:' + str(exception)

    # Obviamente haveriam formas de melhorar esse código criando estruturas
    # reaproveitaveis para lidar com o dispatching de eventos. Mas e se alguém
    # já tivesse feito esse trabalho por nós?

    return dict(
        statusCode=status_code,
        isBase64Encoded=False,
        body=return_body
    )
