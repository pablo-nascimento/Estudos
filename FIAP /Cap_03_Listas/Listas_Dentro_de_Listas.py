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



