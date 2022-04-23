# Curso Python - FIAP
# Manipulando informações dentro de um dicionário
# 23.04.2022 - 14h48

users = {}

escolha = (
    input('Escolha uma das opções abaixo: ' +
          'I - Inserir um novo usuário: ' +
          'P - Pesquisar um usuário: ' +
          'E - Excluir um usuário: ' +
          'L - Listar um usuário: '
          ).upper()
)


while escolha == 'I' or escolha == 'P' or escolha == 'E' or escolha == 'L':
    if escolha == 'I':
        chave = input('Login: ')
        usuario = input('Nome do usuário: ')
        data_acesso = input('Último acesso (xx.xx.xxxx): ')
        estacao = input('Estação de trabalho: ')
        users[chave] = [usuario, data_acesso, estacao]
    escolha = (
        input('Escolha uma das opções abaixo: ' +
              'I - Inserir um novo usuário: ' +
              'P - Pesquisar um usuário: ' +
              'E - Excluir um usuário: ' +
              'L - Listar um usuário: '
              ).upper()
    )

