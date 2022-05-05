# Curso Python - FIAP
# Criação e Manipulação de Arquivos.
# 04.05.2022 - 20h58

# Criação de arquivo - variavel = funcao open(caminho do arquivo, modo de abertura(read-leitura, write-escrita,
# append(r + w))
# x-exclusivo(somente quem abriu o arquivo, que pode ve-lo.
arquivo = open('arquivo_estudo.txt', 'w')

# Gravando dados no arquivo com a funcao write
arquivo.write("Gravando informacões no arquivo de estudo.")
arquivo.close() # Fechando o acesso ao arquivo.

# Utilizando o with - abaixo, ocorre a abertura do arquivo, junto com o modo de abertura,
# uso da funcao write com o seu parametro, e ao sair do bloco, já ocorre o fechamento do arquivo.
with open('arquivo_estudo.txt', 'a') as a:
    a.write("\nGravando mais dados...")