"""
Este script simula uma chamada de integração de um API Gateway REST
com uma Lambda

A sintaxe completa de integração com um REST APIG pode ser encontrada aqui:

https://github.com/awsdocs/aws-lambda-developer-guide/blob/main/sample-apps/nodejs-apig/event.json
"""
from classic_lambda_handler import lambda_handler
import json

if __name__ == '__main__':

    create_user_event = dict(
        httpMethod='POST',
        path="/api/v0/usuarios/",
        body=json.dumps(
            {
                "name": "Samuel",
                "age": 27
            }
        )
    )

    create_product_event = dict(
        httpMethod='POST',
        path="/api/v0/produtos/",
        body=json.dumps(
            {
                "name": "Detergente",
                "price": 10.99
            }
        )
    )

    get_user_event = dict(
        httpMethod='GET',
        path="/api/v0/usuarios/1",
        body=''
    )

    result = lambda_handler(
        event=create_product_event,
        context=None
    )

    print(result)
