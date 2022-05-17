# Curso Python - FIAP
# Leitura de Arquivos e transformação de dados em lista
# 16.05.2022 - 22h10

base_dados = [] # Lista Vazia

with open("iris.data", "r") as arquivo: # Abrindo o arquivo no modo leitura.
    for dado in arquivo.readlines(): # Percorrendo linha a linha dentro do arquivo.
        base_dados.append(dado.split(" ")) # Adicionando cada linha do arquivo a lista base_dados
        # Está sendo usado como separador, o espaço contido no final de cada linha.
        

print(base_dados)