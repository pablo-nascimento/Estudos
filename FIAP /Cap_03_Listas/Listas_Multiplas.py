# Curso Python - FIAP
# Listas Multiplas
# 21.04.2022 - 20h14

# Declarando as listas
equipamento = []
valor = []
serial = []
departamento = []
resposta = 'S'

# Estrutura usada para alimentar as listas
while resposta == 'S':
    equipamento.append(input('Informe o nome: '))
    valor.append(float(input('Informe o valor: ')))
    serial.append(int(input('Informe o serial: ')))
    departamento.append(input('Informe o departamento: '))
    resposta = input('Digite \"S"\ para continuar: ').upper()

# Utilizando o metodo FOR para percorrer e dar a saida do conteudo da lista.
for i in range(0, len(equipamento)):
    print('\nEquipamento: ', (i + 1))
    print('Nome: ', equipamento[i])
    print('Valor: ', valor[i])
    print('Serial: ', serial[i])
    print('Departamento: ', departamento[i])
    print('\n')