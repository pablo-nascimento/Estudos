# Curso Python - FIAP
# Manipulando informações dentro de um dicionário
# 23.04.2022 - 14h48

# Importando as funções do arquivo Funcoes_Dicionario
from Cap_04_Dicionarios.Funcoes_Dicionario import *

users = {}

escolha = opcaoUsuario()

while escolha == 'I' or escolha == 'P' or escolha == 'E' or escolha == 'L':
    if escolha == 'I':
        chave = input('Login: ')
        usuario = input('Nome do usuário: ')
        data_acesso = input('Último acesso (xx.xx.xxxx): ')
        estacao = input('Estação de trabalho: ')
        users[chave] = [usuario, data_acesso, estacao]
    escolha = opcaoUsuario()

