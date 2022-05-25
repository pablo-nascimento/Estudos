# Curso Python - FIAP
# Leitura de Arquivos e transformação de dados em lista
# 16.05.2022 - 22h10

base_dados = [] # Lista Vazia

with open("iris.data", "r") as arquivo: # Abrindo o arquivo no modo leitura.
    for dado in arquivo.readlines(): # Percorrendo linha a linha dentro do arquivo.
        base_dados.append(dado.split(",")) # Adicionando cada linha do arquivo a lista base_dados
        # Está sendo usado como separador, a virgula contida no final de cada linha.
        # Entao, cada numero, separado por virgula, vira uma posicao dentro da lista base_dados.
        # Cada linha representa um registro na base de dados, e sera usada como delimitador natural.

print(base_dados)
print(base_dados[0][2]) # Acessando a terceira posicao da lista interna. Primeira posicao da lista externa.

print(float(base_dados[0][0]) + float(base_dados[0][1]))
# Somando as duas primeiras posicoes da primeira lista
# Se fez necessario converter as posicoes para float, para fazer as operacoes de soma.