# Curso Python - FIAP
# Decisao Simples
# 21.04.2022 - 19h02

# Decisao simples - se, satisfeita a condicao, o fluxo do programa vai entrar no bloco e ira executar o que estiver dentro.


nome = input('Informe o nome: ')
idade = int(input('Informe a idade: '))

if idade >= 65:
    print('O paciente ' + nome + ' possui atendimento prioritario.')
