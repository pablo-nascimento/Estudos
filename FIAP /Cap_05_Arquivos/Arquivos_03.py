# Curso Python - FIAP
# Leitura de Arquivos e transformação de dados em lista
# 16.05.2022 - 22h10

base_dados = []

with open("iris.data", "r") as arquivo:
    for dado in arquivo.readlines():
        base_dados.append(dado.split(" "))

print(base_dados)