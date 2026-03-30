#Somador até valor informado
num = int(input('Qual o número final? '))
soma = 0
i = 1
while i <= num:
    soma = soma + i
    i = i + 1
print('A soma de 1 até', num, '=', soma)


num = int(input('Qual o número final? '))
if num > 0:
    soma = 0
    i = 1
    while i <= num:
        soma = soma + i
        i = i + 1
    print('A soma de 1 até', num, '=', soma)
else:
    print('Use números não-negativos')
