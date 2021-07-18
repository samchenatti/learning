# Logging

O objetivo deste repositório é prover informações a cerca das melhores práticas no uso da biblioteca `logging` do Python

## Como a biblioteca funciona

A biblioteca logging é formada por três peças:
 - Handler: é a peça responsável por decidir o que será feito com o registro do logging. Devo envia-lo para o stdout? Para um sistema remoto através da Web?
 - Formatter: define como será feita a formatação do log; como a data deve ser exibida? qual a ordem das informações?
 - Logger: é a interface através da qual nós de fato registramos um log na aplicação

