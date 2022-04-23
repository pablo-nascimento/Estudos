# Curso Python - FIAP
# Listas Multiplas - Buscando informacoes em listas
# 23.04.2022 - 10h05

# Definindo as listas
equipamento = []
valor = []
serial = []
departamento = []
resposta = 'S'

# Alimentando as listas acima
while resposta == 'S':
    equipamento.append(input('Informe o equipamento: '))
    valor.append(input('Informe o valor: '))
    serial.append(input('Informe o serial: '))
    departamento.append(input('Informe o departamento: '))
    resposta = input('Deseja inserir mais algum equipamento? S/N: ').upper()
    print('\n')

# Pesquisa de dados dentro da lista #
# Variavel pesquisa - vai receber o conteudo a ser pesquisado.
pesquisa = input('Pesquisa de equipamento. Informe o nome do equipamento para pesquisa: ')

# Percorrendo a lista equipamento
for elemento in range(0, len(equipamento)):
    # Comparando o que foi digitado pelo usuario com o que está salvo em cada posicao da lista equipamento
    # Condicao abaixo sendo satisfeita, o bloco interno do IF é executado.
    if pesquisa == equipamento[elemento]:
        print('Equipamento número: ', elemento + 1)
        print('Equipamento: ', equipamento[elemento])
        print('Serial: ', serial[elemento])