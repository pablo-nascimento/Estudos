# Curso Python - FIAP
# Variaveis e Listas - Introducao
# 21.04.2022 - 19h57

# Declarando a lista
inventario = []

# Variavel do tipo string usada para controlar o laco.
resposta = 'S'
while resposta == 'S':

    # Metodo append usado para alimentar a lista.
    inventario.append(input('Equipamento: '))
    inventario.append(float(input('Valor: ')))
    inventario.append(int(input('Numero Serial: ')))
    inventario.append(input('Departamento: '))

    # Variavel de controle do laco
    resposta = input('Digite \"S\" para continuar:  ').upper()
