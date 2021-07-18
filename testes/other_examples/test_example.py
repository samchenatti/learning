# Exemplo de teste unitário
def soma(a: float, b: float) -> float:
    """
    Soma dois números de forma estúpida
    """
    resultado = 2 * ((a/2) + (b/2))

    return resultado


def test_soma():
    print('Testando soma')
    assert soma(2, 2) == 4, 'A soma de 2 e 2 deve ser 4'


if __name__ == '__main__':
    test_soma()
