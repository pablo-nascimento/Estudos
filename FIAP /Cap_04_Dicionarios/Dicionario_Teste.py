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
pesquisa = input('Informe o estado para pesquisa: ').upper()
for chave in estado.keys():
    if pesquisa == chave:
        print(estado.get(pesquisa))