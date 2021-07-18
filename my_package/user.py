from typing import Optional
import requests

import logging

logger = logging.getLogger('aplicacao.usuario')


class User:
    """
    Classe que representa um usuário da aplicação

    Attributes:
        name: nome do usuário
        token: token do usuário (se autenticado, se não None)
    """

    def __init__(self, name: str, token: Optional[str] = None):
        self.name = name
        self.token = token
        self.logger = True

    def login(self, password: str) -> bool:
        """
        Autentica o usuário no sistema

        Args:
            password: a senha com a qual o usuário será autenticado

        Returns:
            True em caso de sucesso ou False caso contrário

        Raises:
            ValueError no caso da senha ser uma string vazia
        """
        if not password:
            raise ValueError('A senha não pode ser vazia')

        response = requests.get('http://www.autenticausuario.com.br')

        if response.status_code == 200:
            self.logged = True
            return True

        return False

    def logout(self):
        """
        Desconecta o usuário da aplicação
        """
        self.logged = False
