# Somador até digitar 0
num = int(input('Qual o número final? (0 para terminar) '))
while num != 0:
    if num > 0:
        soma = 0
        i = 1
        while i <= num:
            soma = soma + i
            i = i + 1
        print('A soma de 1 até', num, '=', soma)
    else:
        print('Use números não-negativos')
    num = int(input('Qual o número final? (0 para terminar) '))
