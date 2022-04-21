# Curso Python - FIAP
# Decisao Simples
# 21.04.2022 - 19h19

# Aprimorando a estrutura de decisao

# Variaveis
nome = input('Informe o nome: ')
idade = int(input('Informe a idade: '))
doenca = input('Suspeita de doenca contagiosa (SIM / NAO)').upper()

# Estrutura de decisao encadeada
if idade >= 65:
    print('O paciente ' + nome + ' possui atendimento prioritario.')
elif doenca == 'SIM':
    print('Direcionando o paciente ' + nome + ' para uma sala reservada.')
else:
    print('O paciente ' + nome + ' NAO possui atendimento prioritario.')
