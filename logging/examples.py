import logging
import sys

# Loggers são criados quando utilizamos `logging.getLogger`
logger = logging.getLogger('main')

# A principio eles não possuem nenhum handler
print('Handlers:', logger.handlers)

# Por default, todo logger é filho do root logger
print('Root logger:', logger.root, ', root handlers:', logger.root.handlers)

# Como não há nenhum handler registrado, ao tentarmos logar nada acontecerá
logger.info('Teste')

# Podemos registrar um handler
logger.addHandler(logging.StreamHandler(stream=sys.stdout))
logger.info('Teste')

# Perceba que mesmo assim nada acontece. Isso se dá pelo fato de que o nível do
# logger é maior do que info
print('Nível do logger:', logger.level, '== NOTSET')
logger.setLevel(logging.DEBUG)
logger.info('Teste!')

# Um logger pode ter mais de um Handler. A informação será enviada a todos os
# handlers
logger.addHandler(logging.FileHandler(filename='./log.log'))
logger.info('Teste com file handler')

# Um logger pode ter filhos
child_logger = logging.getLogger('main.child')
child_logger.setLevel(level=logging.DEBUG)
child_logger.info('Logging from child')

# Como o child_logger foi capaz de logar se ele não tem um handler?
print('Handlers do child_logger:', child_logger.handlers)

# A biblioteca logging propaga o log para o pai no caso de propagate ser True.
# Podemos desativar o comportamento de propagação
child_logger.propagate = False
child_logger.info('Agora nada deve aparecer na tela')

# E podemos adicionar um handler ao child logger para que ele possa atender o
# log
child_logger.addHandler(logging.StreamHandler(stream=sys.stdout))
child_logger.info('Agora o child logger é capaz de logar')

# Se habilitarmos o propagate, teremos um log duplicado! Ele é emitido tanto
# pelo filho quanto pelo pai
child_logger.propagate = True
child_logger.info('child logger continua logando')

# Qual a melhor saída então? Geralmente se seta o handler apenas para o root
# logger
for handler in child_logger.handlers:
    child_logger.removeHandler(handler)

for handler in logger.handlers:
    logger.removeHandler(handler)

child_logger.info('Child está mudo')
child_logger.info('Parent está mudo')

# Setamos o handler para o root logger
root_logger = logging.getLogger()
root_logger.addHandler(logging.StreamHandler(stream=sys.stdout))
child_logger.info('Agora o root recebe os logs do child')

# Há também os formatters. Eles permitem especificar a maneira como os logs vão
# ser formatados antes de serem emitidos pelos Handlers

root_logger.handlers[0].setFormatter(
    fmt=logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
)

child_logger.info('Agora eu estou formatadinho')
