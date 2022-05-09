# Curso Python - FIAP
# Uso de dicionarios somado a manipulação de arquivos.
# 09.05.2022 - 20h00

def opcaoUsuario():
    escolha = (
        input('Escolha uma das opções abaixo: ' +
              'I - Inserir um novo usuário: ' +
              'P - Pesquisar um usuário: ' +
              'E - Excluir um usuário: ' +
              'L - Listar um usuário: '
              ).upper()
    )
    print("\n")
    return escolha

def inserir(dicionario):
    dicionario[input("Login:")] = [input('Nome do usuário: '),
                input('Data do último acesso: '),
                input('Estação de trabalho:') ]

def pesquisar(dicionario):
    login = input("Login: ")
    for chave in dicionario.keys():
        if chave == login:
            print("Login: ", login)
            print(dicionario.get(chave), '\t')

def excluir(dicionario, login):
    if dicionario.get(login) != None:
        del dicionario[login]
        print('Excluído.', '\t')
    else:
        print('Login não localizado.')

def listar(dicionario):
    for chave, valor in dicionario.items():
        print(chave + " - " + valor + "." + "\n")