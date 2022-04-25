# Curso Python - FIAP
# Arquivo de teste e treino para aperfeiçoar o uso com dicionários
# 23.04.2022 - 16h02

# Declarando um dicionario.
estado = {'SP': ['Sao Paulo', 'Guarulhos, Campinas, Santos, Araçatuba, Sao José do Rio Preto'],
          'RJ': ['Rio de Janeiro', 'Nova Iguaçu, Petrópolis, Duque de Caxias, Angra dos Reis, Paraty'],
          'BA': ['Salvador', 'Feira de Santana, Camaçari, Caculé, Igaci, Teolandia'],
          'ES': ['Vitoria', 'Marataizes, Vargem Alta, Vila Velha, Serra, Linhares']
        }

estado['PR'] = ['Curitiba', 'Almirante Tamandare, Maringa, Londrina, Ponta Grossa, Paranagua']

# Percorrendo todo o dicionario
# Metodo items - retorna a chave e o seu valor.
for chave in estado.items():
    print(chave)
print('\t')

# Método keys - retorna somente as chaves, sem os valores.
for chave in estado.keys():
    print(chave)
print('\t')

# Método values - retornando somente os valores de cada chave.
for chave in estado.values():
    print(chave)
print('\t')


# Pesquisa de valores do dicionario, através de sua respectiva chave
# Variavel pesquisa recebe o que será pesquisado.
pesquisa = input('Informe o estado para pesquisa: ').upper()

# Laco for vai percorrer as chaves do dicionario
for chave in estado.keys():
    # Comparar o que estiver de chave com o conteudo da variavel pesquisa
    if pesquisa == chave:
        # Em caso de retorno positivo, dada a saída dos valores correspondentes a chave pesquisada.
        print(estado.get(pesquisa))
print('\t')

# Removendo itens do dicionario
# Abordada nova estratégia, como está no curso da FIAP.
# Verificada se o que estiver na variavel remover é diferente de vazio.
# Verdadeiro, é chamado o método del passando por parametro dicionario[chave]
remover = input('Informe o estado a ter os registros removidos: ').upper()
if estado.get(remover) != None:
    del estado[remover]
    print('\t')

for chave in estado.values():
    print(chave)