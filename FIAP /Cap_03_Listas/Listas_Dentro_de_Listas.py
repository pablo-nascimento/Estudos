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
for elemento in inventario:
    for indice in elemento:
        print(indice)
    print('\t')

