# Curso Python - FIAP
# Leitura de Arquivos JSON
# 25.05.2022 - 20h38

import json

with open("db_users.json", "r") as arquivo_json:
    arquivo = json.load(arquivo_json)
    for chave, valor in arquivo.items():
        print(chave + " - " + str(valor))