# Curso Python - FIAP
# Estruturas de Repeticao - Repeticao FOR
# 21.04.2022 - 19h41

# FOR - diferentemente do While, é possivel determinar o inicio, o final da repeticao e seu incremento.

tabuada = int(input('Informe o valor da tabuada a ser exibida: '))
for valor in range(1, 11, 1):
    print(tabuada, ' X ', valor, ' = ', tabuada * valor)