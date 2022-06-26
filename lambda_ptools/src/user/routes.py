from aws_lambda_powertools.event_handler.api_gateway import Router
from src.user.user import create_user

router = Router()


@router.post('/usuarios/')
def create_user_api():
    """
    Endpoint para criação de novos usuários
    """
    new_user = create_user(
        name=router.current_event.json_body.get('name'),
        age=router.current_event.json_body.get('age')
    )

    return new_user.json()


@router.get('/usuarios/<id_usuario>')
def get_user_api(id_usuario: int):
    """
    Endpoint para busca de usuario por id
    """

    return {'mensagem': f'Usuario com id {id_usuario} nao encontrado'}
