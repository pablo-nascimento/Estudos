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

for chave in range(0, len(t)):
    print(t[chave])
print('\t')

# Percorrendo a lista t com o método range.
for chave in range(0, len(t)):
    print("Email.... ", t[chave][1]) # Acessando a cada item da lista, no caso, a tupla, indo até o segundo item.
    usuarios[t[chave]] = [input("Nome..... "), input("Nível de acesso...... ")]
    # Alimentando o dicionario usuarios
    # usando como chave, cada posicao da lista, neste caso, a tupla com o conjunto numero - email.
    # e como valor, o nome e o e-mail captados pelo input.
    print('\t')

print(usuarios) # Saída do dicionario usuarios.
print('\t')

# Percorrendo o dicionario usuarios, onde, na chave, estao os dados gerados pela funcao enumerate, logo acima
# e no valor, estao os valores informados pelo usuario.
# Por isso, tanto a chave, quanto o valor, possuem dois itens, que sao apontados manualmente, logo abaixo.
for chave, dado in usuarios.items():
    print("Usuario..... ", chave[0])
    print("Email..... ", chave[1])
    print("Nome.... ", dado[0])
    print("Nivel.... ", dado[1])
    print('\n')
