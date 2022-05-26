# Curso Python - FIAP
# Leitura de Arquivos JSON
# 25.05.2022 - 20h38

import json # Importando módulo JSON

with open("db_users.json", "r") as arquivo_json: # Abrindo o arquivo JSON
    arquivo = json.load(arquivo_json) # Carregando o que está no arquivo JSON, para a variavel arquivo.
    for chave, valor in arquivo.items(): # Percorrendo o dicionario arquivo para ter o retorno de chave e valor.
        print(chave + " - " + str(valor)) # Saída das chaves e de seus valores.