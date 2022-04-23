# Curso Python - FIAP
# Trabalhando com a modularização e o uso de funções.
# 23.04.2022 - 15h02

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
