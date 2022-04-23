# Curso Python - FIAP
# Listas dentro de Listas - estudando como montar, e sua aplicabilidade.
# 23.04.2022 - 10h33

inventario = []
#equipamento = []
resposta = 'S'

# Alimentando a lista equipamento com todas as informacoes. Em seguida, adicionando a lista inventario o que
# estiver na lista equipamento.
while resposta == 'S':
    equipamento = [
        input('Equipamento: '),
        float(input('Valor: ')),
        int(input('Serial: ')),
        input('Departamento: ')
    ]
    inventario.append(equipamento)
    resposta = input('Deseja adicionar mais algum equipamento? ').upper()
    print('\t')

# Testando a saida do que vai ficar salvo na lista inventario.
# Cada equipamento(nome, valor, serial, departamento, será uma unica lista, dentro da lista inventario.
# Pendencia - achar uma forma de incluir mais um laco por dentro, para percorrer cada item da lista interna.
#for indice in range(0, len(inventario)):
 #   print(inventario[indice])

# Pendencia acima listada, foi resolvida -
# Usei mais um laco para percorrer a variavel do laco externo.
# No exemplo usado no curso, a posicao da lista interna é apontada manualmente.
# Preferi usar um laco interno para treinar o uso de laco dentro de laco.
for elemento in inventario:
    for indice in elemento:
        print(indice)
    print('\t')

# Busca
pesquisa = input('Informe o nome do equipamento a ser pesquisado: ')
for elemento in inventario:
    for indice in elemento:
        if pesquisa == elemento[0]:
            print(indice)

depreciacao = input('Informe o nome do equipamento a ser depreciado: ')
for elemento in inventario:
    for indice in elemento:
        if depreciacao == elemento[0]:
            print('Equipamento: ', indice)
            print('Valor Atual: ', elemento[1]) # Apontando a posicao da lista onde fica armazenado o valor.
            elemento[1] = elemento[1] * 0.9
            print('Valor após depreciacao: ', elemento[1])