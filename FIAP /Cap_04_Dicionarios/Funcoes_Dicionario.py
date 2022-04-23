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

def pesquisarUsuario(dicionario, chave):
    print('Login: ', dicionario)
    print(dicionario.get(chave))

# def excluirUsuario(dicionario):


def listarUsuario(dicionario):
    print(dicionario)
