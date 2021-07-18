import pytest
from my_package.user import User
from pytest_mock import MockerFixture


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

# Exemplo de fixture automática

# Exemplo de clean-up com fixtures


@pytest.fixture
def self_logout_user():
    user = User(name='Auto Delete User')
    yield user


# Exemplo de usuário mockando requets


def test_user_login_sucess(example_user: User):
    pass
