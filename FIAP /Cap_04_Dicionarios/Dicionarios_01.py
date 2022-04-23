# Curso Python - FIAP
# Criação de Dicionários
# 23.04.2022 - 14h27

# Declarando um dicionario
# Estrutura de dados que funciona com o conjunto chave e valor
# dicionario = {chave : valor - que pode ser uma lista, ou um outro valor}

usuarios = \
    {
        'user_01' : ['usuario_01', '23.12.2021', 'TI_01'],
        'user_02' : ['usuario_02', '27.12.2021', 'ADM_02']
    }
print(usuarios)

# Adicionando novos registros ao dicionario acima criado
# nome_dicionario[chave] = valor
usuarios['user_03'] = ['usuario_03', '01.01.2022', 'FIN_05']

print(usuarios)

# Pesquisando os valores do dicionário através de sua chave.
# Utilizar o método get.

pesquisa = input('Informe o login do usuario a ser pesquisado: ')
print(usuarios.get(pesquisa))

