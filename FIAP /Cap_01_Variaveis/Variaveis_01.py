# Curso Python - FIAP
# Estudo de Variaveis
# 21.04.2022 - 18h38

# Armazenando na variavel nome, o conteudo digitado
nome = input('Digite o nome de um funcionario: ')

# Armazenando na variavel empresa, o que for digitado.
empresa = input('Digite o nome da empresa: ')

# Variavel qtde_funcionarios, vai receber o que for digitado, apos ter seu tipo de dado convertido para inteiro.
qtde_funcionarios = int(input('Quantidade de funcionarios: '))

# Variavel media_Mensalidade recebendo o que for digitado, apos ser convertido para float (ponto flutuante).
media_Mensalidade = float(input('Media da mensalidade: '))

# Funcao print, usada para saida de dados. Sinal de + usado na concatenacao de strings com dados do tipo string.
print(nome + ' trabalha na empresa ' + empresa + '.')

# Funcao str, usada para converter tipo de dados para string
print('Possui: ' + str(qtde_funcionarios) + ' funcionarios.')
print('Valor medio da mensalidade: R$' + str(media_Mensalidade) + '.')
print('== Verificando o tipo de dado de cada variavel: ==')
print('\n\n')

# Verificando os tipos de dados de cada variavel, atraves da funcao type.
print('Variavel nome: ' , type(nome))
print('Variavel empresa: ',  type(empresa))
print('Variavel qtde_funcionarios: ', type(qtde_funcionarios))
print('Variavel media_Mensalidade: ', type(media_Mensalidade))




