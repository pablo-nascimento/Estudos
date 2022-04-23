# Curso Python - FIAP
# Construçao e uso de funções no Python
# 23.04.2022 - 12h24

# Declaração de uma lista
# Palavra reservada def nome_lista(parametro de entrada):
#       bloco de código a ser executado.
#       palavra reservada return (caso seja necessário retornar algum valor).

def preenchendoInventario(lista):
    while resposta == 'S':
        equipamento = [
            input('Equipamento: '),
            float(input('Valor: ')),
            int(input('Serial: ')),
            input('Departamento: ')
        ]
        lista.append(equipamento)
        resposta = input('Deseja adicionar mais algum equipamento? ').upper()
        print('\t')

