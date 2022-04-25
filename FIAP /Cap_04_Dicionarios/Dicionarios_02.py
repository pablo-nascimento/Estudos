# Curso Python - FIAP
# Manipulando informações dentro de um dicionário
# 23.04.2022 - 14h48

# Importando as funções do arquivo Funcoes_Dicionario
from Cap_04_Dicionarios.Funcoes_Dicionario import *

users = {}

escolha = opcaoUsuario()

while escolha == 'I' or escolha == 'P' or escolha == 'E' or escolha == 'L':
    if escolha == 'I':
        inserirUsuario(users)
        escolha = opcaoUsuario()
    elif escolha == 'P':
        pesquisarUsuario(users)
        escolha = opcaoUsuario()
    elif escolha == 'E':
        excluirUsuario(users)
    elif escolha == 'L':
        listarUsuario(users)
        escolha = opcaoUsuario()

