# Frameworks de teste unitário em Python

Este repositório contém código de estudo acerca de dois dos principais frameworks para testes unitários em Python: PyUnit (Unittest) e PyTest.

O pacote `my_package` contém código dummy que será utilizado para testes. As pastas `test_pytest` e `test_unittest` implementam testes para `my_package` utilizando os frameworks PyTest e Unittest, respectivamente.

O que segue nesse Readme são as explicações e resultados de pesquisa acerca do assunto.

## Objetivos

O objetivo deste repositório é me orientar durante uma passagem de conhecimento sobre o framework PyTest do Python. O intuito é apresentar a ferramenta em si, e não perder muito tempo revisando a teoria de testes unitários.

### Mas o que são testes unitários?

Testes unitários são testes automatizados que verificam o funcionamento de uma pequena unidade de código, como funções e métodos de classes. O objetivo é garantir que o contrato de uma dada unidade não seja alterado durante refatorações.

Um exemplo bem simples de uma função desnecessariamente complexa:

```Python
def soma(a: float, b: float) -> float:
   """ Realiza uma soma de uma forma complicada """
   resultado = 2 * (a/2 + b/2)

   return soma
```

Para testa-la, precisamos apenas garantir o seu contrato:

```Python
a = 2
b = 2
assert soma(a, b) == 4, 'O resultado da soma de 2 e 2 deve ser 4'
```

Podemos alterar o corpo da função e o teste deve continuar funcionando:

```Python
def soma(a: float, b: float) -> float:
   """ Realize uma soma de uma forma mais direta """
   return a + b
```

De forma geral, os testes unitários sempre seguem os seguintes passos:
 - Preparação da entrada do teste
 - Execução da unidade
 - _Assert_ do resultado
 - Limpeza dos dados criados para o teste

Obviamente as situações do dia a dia acabam sendo um pouco mais complicadas e requerem um pouco mais de criatividade e ferramentas para serem testadas. É aí que entram os frameworks.

## Frameworks

Existem diversos frameworks de testes unitários em Python, mas dois dos principais são:
 - Unittest (PyUnit)
    - Framework built-in de testes unitários do Python
    - É bem semelhante ao JUnit, fazendo forte uso de princípios de orientação a objetos para implementações dos testes **(class based)**
    - Possui métodos específicos para assertion
 - PyTest
    - Mesmo não sendo built-in, parece ser o mais utilizado e querido da comunidade.
    - A sintaxe é muito mais limpa e permissiva em relação ao Unittest **(function based)**.
    - Baseado no uso direto do `assert` do Python

É importante ressaltar que o PyTest é capaz de executar testes do Unittest sem qualquer tipo de problema. Sendo assim, ambos frameworks se encaixam bem nas nossas esteiras.

### Comparação

Um teste em PyTest é tão simples quanto:

```Python
def test_sum():
   """ Testa a soma de dois números """
   assert soma(2, 2) == 4, 'O resultado da soma deve ser 4'
```

Enquanto que no Unittest é sempre necessário escrever uma classe herdando `TestCase` e utilizar os asserts disponibilizados pelo framework:

```Python
from unittest import TestCase

class TestSum(TestCase):
   def test_sum_integers(self):
      """ Testa a soma de dois números """
      # Perceba que o Unittest faz uso de camelCase, enquanto o padrão do Python
      # é o snake_case; herança do Java!
      self.assertEqual(
         soma(2, 2),
         4,
         'O resultado da soma deve ser 4'
      )
```

O PyTest também possibilita (mas não obriga) o uso de classes para agrupamento de testes.

A grande diferença é a maneira como a preparação dos testes são feitos. O Unittest funciona utilizando métodos especiais que são chamados antes de cada teste ou antes de todos os testes de uma classe: `setUp(self)` e `setUpClass(cls)`.

Enquanto isso, o PyTest utiliza um sistema de **Fixtures**, que são funções de preparação que podem ser utilizadas de forma global por todos os testes unitários presentes no pacote. Elas são extremamente módulares e facilitam o desenvolvimento de plugins para o PyTest.

Como parece existir um viés maior pelo uso do PyTest dentro da empresa (algumas esteiras chamam o PyTest por default), seguiremos utilizando ele para demonstrar o funcionamento de outras ferramentas de testes unitários.

## PyTest

### Fixtures

Fixtures são uma forma de preparar os dados e objetos que serão utilizados durante os testes. Eles são funções anotadas pelo PyTest e retornam o objeto criado

```Python
def valida_payload(payload: dict) -> bool:
   if payload['status'] != 200:
      raise Exception()

@pytest.fixture
def payload() -> dict:
   return {
      'status': 404
   }

# O simples fato de colocarmos o nome da fixture na assinatura da função fará
# com que o PyTest injete o retorno da fixture aqui
def test_request(payload: dict):
   print('Recebi a fixture:', valid_payload)

   with pytest.raises(Exception):
      assert valida_payload(payload)
```

## Ferramentas interessantes

### Mocking

Mocking, como o nome sugere, é o ato de mimicar o comportamento de algo. No nosso caso, queremos mimicar o comportamento de bibliotecas e funções que não podem ser chamadas em tempo de testes, como requests, acesso à banco de dados e etc.

A principal classe quando estamos falando sobre Mocks em Python é a `MagicMock`. Um objeto do tipo MagicMock pode assumir o papel de qualquer outra biblioteca ou função. Isso por que, quando tentamos chamar qualquer tipo de atributo ou método em um objeto do tipo MagicMock ele não falhará, mas registrará a chamada para que possamos realizar asserting posteriormente:

```Python
from unittest.mock import MagicMock

mock = MagicMock()

# O retorno de um método de um mock é outro mock
mock.sum(1, 2)

# Podemos ver que o objeto de fato registra as chamadas
mock.sum.call_args

# Podemos utilizar os parametros guardados pela chamada para fazer assertion
mock.sum.assert_called_with(1, 3) # Falha
mock.sum.assert_called_with(1, 2) # Passa

# Podemos resetar o mock para que ele volte ao seu estado original
mock.reset_mock
mock.sum.assert_called_with(1, 2) # Falha (não foi chamado ainda)

# Podemos emular o comportamento da função que queremos mockar
mock.sum.return_value = 4
moc.sum(2, 2)

# Ou, ainda, podemos adicionar um side-effect ao mock para testar um cenário de rise
mock.sum.side_effect = Exception
mock.sum(2, 2)

# Em alguns casos queremos garantir um stub; isto é, queremos mimicar diretamente a interface de uma classe
class Papagaio:
   def fala(self, frase: str):
      print(frase)

papagaio_mock = MagicMock(spec=Papagaio)

```
