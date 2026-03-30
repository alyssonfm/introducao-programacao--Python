# Calculando o fatorial
num = int(input('Qual o valor para o cálculo do fatorial? '))
fatorial = 1
for i in range(1, num+1):
    fatorial = fatorial * i
print('O fatorial de', num, 'é', fatorial)
