# Curso Python - FIAP
# Treino - Calculadora
# 06.06.2022 - 20h12

n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segundo número: "))
operacao = int(input("1 - Soma: \n" +
                     "2 - Subtração: \n" +
                     "3 - Multiplicaçao: \n" +
                     "4 - Divisão: "))

if operacao == 1:
    print("\nSoma: ", n1, " + ", n2, " = " ,(n1 + n2))
elif operacao == 2:
    if n1 > n2:
        print("\nSubtração: ", n1, " - ", n2, " = ", (n1 - n2))
    elif n2 > n1:
        print("\nSubtração: ", n2, " - ", n1, " = ", (n2 - n1))
elif operacao == 3:
    print("\nMultiplicação: ", n1, " * ", n2, " = ", (n1 * n2))
elif operacao == 4:
    if n1 > n2:
        print("\nDivisão: ", n1, " / ", n2, " = ", (n1 / n2))
    elif n2 > n1:
        print("\nDivisão: ", n1, " / ", n2, " = ", (n2 / n1))
    elif n1 == n2:
        print("\nOs dois números informados são iguais.")
print("\nCalculadora finalizada...")








