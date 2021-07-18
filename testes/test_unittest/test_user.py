import pathlib
from unittest import TestCase
from unittest.mock import patch, MagicMock

from my_package.user import User
from requests import Response
from pathlib import Path


class TestUser(TestCase):
    def setUp(self) -> None:
        """
        Método chamado antes da execução de cada teste
        """
        super().setUp()

        # Criamos uma instância da classe User *a cada teste*, de forma que as
        # modificações feitas no objeto não sejam levadas para os demais testes
        self.user = User(name='Samuel')

    def skip_test_login_without_mocking(self):
        """
        Testa o método de autenticação do usuário sem mocking do módulo
        requests

        É esperado que este teste falhe se não for skipado
        """
        self.assertTrue(
            self.user.login(password='12345'),
            "Deve retornar verdadeiro caso haja uma senha válida"
        )

    @patch('my_package.user.requests.get')
    def test_login_with_mocking(self, get_mock: MagicMock):
        """
        Testa o método de autenticação do usuário com mocking do módulo
        requests
        """
        mock_response = Response()
        mock_response.status_code = 200

        get_mock.return_value = mock_response

    def test_login_invalid_password(self):
        """
        Testa o método de autenticação do usuário com uma senha vazia
        """
        with self.assertRaises(ValueError):
            self.user.login(password='')

    @classmethod
    def setUpClass(cls):
        """
        Primeiro método chamado pela classe
        """
        # Geralmente utilizamos esse tipo de preparação para executar
        # procedimentos custosos (como IO) apenas uma vez
        Path('/tmp/test.txt').touch()

        with open('/tmp/test.txt') as test_file:
            # Os dados devem ser guardados em variáveis de classe, e acessados
            # como atributos do objeto usando self
            cls.test_file = test_file.read()

    @classmethod
    def tearDownClass(cls):
        """
        Último método chamado pela classe
        """
        # Aqui poderiamos fechar conexão com banco de dados ou limpar arquivos
        # que por ventura tenham sido criados durante os testes
        Path('/tmp/test.txt').unlink()
