# Curso Python - FIAP
# Estruturas de Repeticao - Repeticao FOR
# 21.04.2022 - 19h41

# FOR - diferentemente do While, é possivel determinar o inicio, o final da repeticao e seu incremento.

# Variaveis
tabuada = int(input('Informe o valor da tabuada a ser exibida: '))
limite = int(input('Ate onde deve ser calculada a tabuada? '))

# Estrutura FOR com a variavel valor
# metodo range usado juntamente com a estrutura FOR.
# range(inicio, fim, incremento)
for valor in range(1, limite + 1, 1):
    print(tabuada, ' X ', valor, ' = ', tabuada * valor)