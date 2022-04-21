# Curso Python - FIAP
# Estudo de Variaveis
# 21.04.2022 - 18h38

nome = input('Digite o nome de um funcionario: ')
empresa = input('Digite o nome da empresa: ')
qtde_funcionarios = int(input('Quantidade de funcionarios: '))
media_Mensalidade = float(input('Media da mensalidade: '))

print(nome + ' trabalha na empresa ' + empresa + '.')
print('Possui: ' + qtde_funcionarios + ' funcionarios.')
print('Valor medio da mensalidade: R$' + str(media_Mensalidade) + '.')
print('== Verificando o tipo de dado de cada variavel: ==')

print('Variavel nome: ' + type(nome))
print('Variavel empresa: ' + type(empresa))
print('Variavel qtde_funcionarios: ' + type(qtde_funcionarios))
print('Variavel media_Mensalidade: ' + type(media_Mensalidade))




