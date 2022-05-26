# Curso Python - FIAP
# Leitura de Arquivos JSON
# 25.05.2022 - 20h38

import json # Importando módulo JSON

# Leitura de Arquivo JSON
with open("db_users.json", "r") as arquivo_json: # Abrindo o arquivo JSON
    arquivo = json.load(arquivo_json)
    # Carregando o que está no arquivo JSON, para a variavel arquivo, com o método LOAD.
    for chave, valor in arquivo.items(): # Percorrendo o dicionario arquivo para ter o retorno de chave e valor.
        print(chave + " - " + str(valor)) # Saída das chaves e de seus valores.

# Salvando um dicionario em um arquivo JSON
dicionario = {"Outro_usuario_2" : ["Nome do outro usuario 2", "26.05.2022"]}
with open("db_users_2.json", "a") as json_file:
    json.dump(dicionario, json_file)
    # Método dump - converte um objeto Python em uma string JSON.