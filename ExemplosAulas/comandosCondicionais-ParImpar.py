# Testando a paridade de um número
valor = 5
if valor % 2 == 0:
    print(valor, "é par!")
else:
    print(valor, "é ímpar!")


# paridade agora com entrada de dados
valor = int(input('Informe o valor para checar se é par ou ímpar: '))
if valor % 2 == 0:
    print(valor, "é par!")
else:
    print(valor, "é ímpar!")
