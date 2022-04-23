# Curso Python - FIAP
# Manipulando informações dentro de um dicionário
# 23.04.2022 - 14h48

# Importando as funções do arquivo Funcoes_Dicionario
from Cap_04_Dicionarios.Funcoes_Dicionario import *

users = {}

escolha = opcaoUsuario()

while escolha == 'I' or escolha == 'P' or escolha == 'E' or escolha == 'L':
    if escolha == 'I':
        users[input('Login: ')] = \
            [
            input('Nome do usuário: '),
            input('Último acesso (xx.xx.xxxx): '),
            input('Estação de trabalho: ')
            ]
    escolha = opcaoUsuario()

