# Curso Python - FIAP
# Leitura de Arquivos.
# 04.05.2022 - 21h12

# Abrir o arquivo no modo de leitura.
with open("arquivo_estudo.txt", 'r') as arquivo:
    abrir = arquivo.read() # Atribuindo o conteudo do arquivo a variavel abrir
    print(abrir)

# Lendo somente a primeira linha - feito somente para teste.
with open("arquivo_estudo.txt", "r") as a:
    abrir = a.readline() # funcao readline, so acessa a primeira linha do arquivo.
    print(abrir)

# Lendo o arquivo linha a linha.
with open("arquivo_estudo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)