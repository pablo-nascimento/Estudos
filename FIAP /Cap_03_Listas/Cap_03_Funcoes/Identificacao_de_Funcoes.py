# Curso Python - FIAP
# Construçao e uso de funções no Python
# 23.04.2022 - 12h24

# Declaração de uma lista
# Palavra reservada def nome_lista(parametro de entrada):
#       bloco de código a ser executado.
#       palavra reservada return (caso seja necessário retornar algum valor).

# Alimentando a lista.
def preencherInventario(lista):
    resposta = 'S'
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

# Mostrando o conteudo do que já está salvo nas listas.
def exibirInventario(lista):
    for elemento in lista:
        for indice in elemento:
            print(indice)
        print('\t')

# Fazendo a busca na lista.
def localizarLista(lista):
    pesquisa = input("Informe o equipamento a ser localizado: ")
    for elemento in lista:
        for indice in elemento:
            if pesquisa == elemento[0]:
                print(indice)

# Calculando a depreciaçao, onde, será alterado o valor da lista que já foi pre definido.
def calcularDepreciacao(lista, taxa):
    depreciacao = input("Informe o nome do equipamento a ser depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print('Equipamento: ', elemento[0])
            print("Valor atual: ", elemento[1])
            elemento[1] = elemento[1] * (1-(taxa / 100))

# Exclusão de itens.
def excluirInventario(lista):
    serial = int(input('Informe o serial do equipamento a ser excluído: '))
    for elemento in lista:
        if serial == elemento[2]:
            lista.remove(elemento)
    return 'Itens Excluídos.'

# Aplicando as funcoes matematicas aprendidas anteriormente.
def mostrarResumoValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    print('Valor mais caro: ', max(valores))
    print('Valor mais barato: ', min(valores))
    print('Soma dos valores: ', sum(valores))






