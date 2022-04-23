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
def inserirUsuario(dicionario):
    dicionario[input('Login: ')] = \
        [
            input('Nome do usuário: '),
            input('Último acesso (xx.xx.xxxx): '),
            input('Estação de trabalho: ')
        ]
# Funcao de pesquisa dentro do dicionario - funciona, mas necessita de aprimoramentos.
def pesquisarUsuario(dicionario):
    login = input('Informe o login: ')
    for chave in dicionario.keys():
        if chave == login:
            print('Login: ', login, '.')
            for valor in dicionario.values():
                print(valor, '\t')

def excluirUsuario(dicionario):
    print(dicionario)



def listarUsuario(dicionario):
    print(dicionario)
