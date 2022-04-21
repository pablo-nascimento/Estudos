# Curso Python - FIAP
# Estruturas de Repeticao - Repeticao While
# 21.04.2022 - 19h31

# Variavel usada para controlar o laco
num = int(input('Informe um numero: '))

# Condicao para que o laco seja executado, ate um certo ponto.
while num < 100:
    print('\t', num)
    num = num + 1 # Incremento, usado para que a repeticao ocorra, ate que a condicao acima, seja satisfeita.
print('Repeticao finalizada.')