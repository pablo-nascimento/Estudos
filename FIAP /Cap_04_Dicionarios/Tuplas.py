# Curso Python - FIAP
# Trabalhando com Tuplas.
# 04.05.2022 - 20h23


usuarios = {} # Dicionario de usuários
email = ['email@123email.com', 'email@321email.com'] # Lista de e-mails.

# Funcao enumerate - numerar cada item da lista email e gera uma tupla, para cada operacao.
# Funcao list - transformar cada tupla retornada pela funcao enumerate como, um item de uma lista.
# Código abaixo, gera uma lista de tuplas. 
t = list(enumerate(email))


print(t)