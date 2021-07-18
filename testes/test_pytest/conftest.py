import pytest
from pathlib import Path
# Todas as fixtures criadas aqui ficaram disponíveis para os testes presentes
# na pasta e em pastas em níveis inferiores


@pytest.fixture
def conftest_fixture() -> int:
    return 1


@pytest.fixture(autouse=True)
def create_empty_file():
    Path('/tmp/tmp_file.txt').touch()
