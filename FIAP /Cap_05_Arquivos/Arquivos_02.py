# Curso Python - FIAP
# Leitura de Arquivos.
# 04.05.2022 - 21h12

with open("arquivo_estudo.txt", 'r') as arquivo:
    abrir = arquivo.read()
    print(abrir)