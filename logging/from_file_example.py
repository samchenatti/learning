import yaml
import logging
from logging.config import dictConfig
# De modo geral, para permitir que o usuário de um pacote selecione quais logs
# são relevantes, faz-se uso extensivo da hierarquia dos loggers


def conecta_bd():
    bd_logger = logging.getLogger('my_app.bd')

    bd_logger.info('Conectado no BD')


def baixa_dados():
    data_logger = logging.getLogger('my_app.dados')

    data_logger.info('Baixando dados')


with open('log_config.yaml') as yaml_file:
    config = yaml.safe_load(yaml_file)

    dictConfig(config=config)

conecta_bd()
baixa_dados()
