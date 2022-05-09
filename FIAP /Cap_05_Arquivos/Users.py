# Curso Python - FIAP
# Uso de dicionarios somado a manipulação de arquivos (arquivo principal)
# 09.05.2022 - 20h11

from Cap_05_Arquivos.Funcoes_Users import *

# Dicionario vazio
users = {}

# Variavel que controla o laco abaixo.
escolha = opcao()

# Repeticao para manipular o dicionario.
while escolha == "I" or escolha == "P" or escolha == "E" or escolha == "L":
    if escolha == "I":
        inserir(users)
        escolha = opcao()
    elif escolha == "P":
        pesquisar(users)
        escolha = opcao()
    elif escolha == "E":
        excluir(users, input("Login: "))
        escolha = opcao()
    elif escolha == "L":
        listar(users)
        escolha = opcao()

