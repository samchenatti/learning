# Testa o mecanismo de hierarquia do Conftest

def test_higher_conftest_fixture(conftest_fixture: int):
    """
    Testa a capacidade do PyTest de puxar fixtures a patir de conftests em
    níveis superiores
    """
    assert conftest_fixture == 1
