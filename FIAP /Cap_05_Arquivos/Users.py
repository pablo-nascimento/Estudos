# Curso Python - FIAP
# Uso de dicionarios somado a manipulação de arquivos (arquivo principal)
# 09.05.2022 - 20h11

from Cap_05_Arquivos.Funcoes_Users import *

# Dicionario vazio
users = {}

escolha = opcao()

while escolha == "I" or escolha == "P" or escolha == "E" or escolha == "L":
    if escolha == "I":
        inserir(users)
        escolha = opcao()
    if escolha == "P":
        pesquisar(users)
        escolha = opcao()
    if escolha == "E":
        excluir(users)
        escolha == opcao()
    if escolha == "L":
        listar(users)
        escolha == opcao()

