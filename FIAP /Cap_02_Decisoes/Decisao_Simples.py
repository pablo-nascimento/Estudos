# Curso Python - FIAP
# Decisao Simples
# 21.04.2022 - 19h02

# Decisao simples - se, satisfeita a condicao, o fluxo do programa vai entrar no bloco e ira executar o que estiver dentro.

# Variaveis
nome = input('Informe o nome: ')
idade = int(input('Informe a idade: '))

# Estrutura de decisao simples
if idade >= 65:
    print('O paciente ' + nome + ' possui atendimento prioritario.')
else:
    print('O paciente ' + nome + ' NAO possui atendimento prioritario.')

# Estrutura de decisao completa, com o SE e SENAO.