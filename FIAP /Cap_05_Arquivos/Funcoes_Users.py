# Curso Python - FIAP
# Uso de dicionarios somado a manipulação de arquivos.
# 09.05.2022 - 20h00

def opcao():
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
    login = input("Login: ")
    dicionario[login] = [input('Nome do usuário: '),
                input('Data do último acesso: '),
                input('Estação de trabalho: ') ]
    salvar(dicionario)
    print('\n')

# Implementando a funcao de salvar o dicionario dentro do arquivo.
# Usando um laco para percorrer o dicionario e salvar a chave e seu respectivo valor.
def salvar(dicionario):
    with open("db_users.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write("\n" + chave + " - " + str(valor))

def pesquisar():
    login = input("Login: ")
    with open("db_users.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            linha.split(" - ")
            if linha == login:
                print("Encontrado!!")
    print("\n")

def excluir(dicionario, login):
    if dicionario.get(login) != None:
        del dicionario[login]
        print('Excluído.', '\t')
    else:
        print('Login não localizado.')

def listar(dicionario):
    for chave, valor in dicionario.items():
        print(chave, " - ", valor, ".", "\n")