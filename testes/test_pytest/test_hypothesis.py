from hypothesis import given, strategies as st
import pytest

CPF_REGEX = (
    r'([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|'
    r'([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})'
)


@pytest.mark.skip('Gera muito lixo no stdout')
@given(st.integers(min_value=0))
def test_float(integer: int):
    print('Integer:', integer)
    assert isinstance(integer, int)


@pytest.mark.skip('Gera muito lixo no stdout')
@given(st.from_regex(CPF_REGEX))
def test_cpfs(cpf: str):
    print('CPF:', cpf)
    assert isinstance(cpf, str)
