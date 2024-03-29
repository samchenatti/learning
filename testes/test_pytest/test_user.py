import pytest
from my_package.user import User
from pytest_mock import MockerFixture
from requests import Response
from sys import platform
# Como não definimos escopo, essa fixture é chamada uma vez por cada teste


@pytest.fixture
def example_user() -> User:
    """
    Retorna um usuário de exemplo para os testes
    """

    return User(name='Samuel')


def test_user_login_fails(example_user: User):
    """
    Testa que o login do usuário falha se o password for vazio
    """
    with pytest.raises(ValueError):
        example_user.login(password='')

# Exemplo de fixture que chama outra fixture


@pytest.fixture
def loggedin_user(example_user: User) -> User:
    example_user.logged = True

    return example_user


def test_user_is_logged(loggedin_user: User):
    assert loggedin_user.logged, 'O usuário deve estar logado'

# Exemplo de multiplas fixtures sendo chamadas por um teste


@pytest.fixture
def other_user() -> User:
    return User(name='Rafael')


def test_two_users(loggedin_user: User, other_user: User):
    assert loggedin_user.name == 'Samuel'
    assert other_user.name == 'Rafael'

# Exemplo de clean-up com fixtures


@pytest.fixture
def self_logout_user() -> User:
    user = User(name='Self Logout User')
    user.logged = True
    yield user
    user.logged = False
    print('Usuário deslogado após o teste')


def test_self_logout_user(self_logout_user: User):
    assert self_logout_user.logged

# Exemplo de fixtures vindas da conftest.py


def test_conftest_fixture(conftest_fixture: int):
    assert conftest_fixture == 1

# Exemplo de parametrização de teste


@pytest.mark.parametrize(
    'a,b,expected',
    [
        [1, 1, 2],
        [2, 2, 4]
    ]
)
def test_auto_fixture(a: int, b: int, expected: int):
    # print('Number:', number)
    assert a + b == expected

# O PyTest também permite o uso de classes para organizar testes relacionados
# usefixtures permite que um teste utilize fixtures sem precisar receber
# parametros. Ao utiliza-lo em classes, todos os métodos chamarão a fixture


@pytest.mark.usefixtures('conftest_fixture')
class TestUser(object):

    def test_something(self, example_user: User):
        assert example_user.name == 'Samuel'

# Exemplo de usuário mockando requets (ver material de Mock no readme primeiro)


def test_user_login_sucess(example_user: User, mocker: MockerFixture):
    sucess_response = Response()
    sucess_response.status_code = 200

    mocked_get = mocker.patch('my_package.user.requests.get', autospec=True)
    mocked_get.return_value = sucess_response

    assert example_user.login(password='123'), 'Deve ser possível fazer login'

# À princípio o uso de mock pode parecer meio estranho, já que você está
# emulando o comportamento de algo. Mas lembre-se que este algo já foi testado
# e a interface dele está garantida

# Outros decorators da PyTest que são interessantes


@pytest.mark.xfail
def test_should_fail():
    """
    Testes marcados com xfail tem falha esperada
    """
    assert False


@pytest.mark.skip('Este teste deve ser skipado por que X, Y e Z')
def test_should_be_skipped():
    raise Exception


@pytest.mark.skipif(platform == 'linux', reason='Só roda em Windows')
def test_conditional_skip():
    raise Exception
