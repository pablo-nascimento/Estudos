# Curso Python - FIAP
# Trabalhando com a modularização e o uso de funções.
# 23.04.2022 - 15h02

# Definindo as opções de manipulação dos dicionarios.

# 'Menu de Escolha'
def opcaoUsuario():
    escolha = (
        input('Escolha uma das opções abaixo: ' +
              'I - Inserir um novo usuário: ' +
              'P - Pesquisar um usuário: ' +
              'E - Excluir um usuário: ' +
              'L - Listar um usuário: '
              ).upper()
    )
    return escolha

# Inserir usuarios no dicionario
# Está inserindo o login por último - Pendente.
def inserirUsuario(dicionario):
    dicionario[input('Login: ')] = \
        [
            input('Nome do usuário: '),
            input('Último acesso (xx.xx.xxxx): '),
            input('Estação de trabalho: ')
        ]
    print('\t')

# Funcao de pesquisa dentro do dicionario - funciona, mas necessita de aprimoramentos.
# Aprimoramentos realizados no dia 25.04.2022 - 19h57.
# Pesquisa funciona da seguinte forma:
# Recebe o login informado pelo usuario, e é percorrido o dicionario com o método keys
# Comparada a chave de cada valor do usuario, e sendo igual ao login informado, é dada a saída dos respectivos valores
# com o método get, tendo como parametro, o login informado.
def pesquisarUsuario(dicionario):
    login = input('Informe o login: ')
    for chave in dicionario.keys():
        if chave == login:
            print('Login: ', login, '.')
            print(dicionario.get(chave), '\t\t')
        else:
            print('Usuário não localizado.')

# Funcao de exclusao implementada conforme exemplo do curso.
def excluirUsuario(dicionario):
    login = input('Informe o login: ')
    if dicionario.get(login) != None:
        del dicionario[login]

# Função listarUsuario funcionando com o método items, que retorna tanto a chave, quanto o seu respectivo valor.
def listarUsuario(dicionario):
    for chave in dicionario.items():
        print(chave, '\t')
