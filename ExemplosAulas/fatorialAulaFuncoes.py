n = int(input('Informe o número para o cálculo da fatorial: '))
fat = 1
for i in range(1, n+1):
    fat = fat * i
print('O fatorial de', n, 'é', fat)

# Criando uma função
def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat = fat * i
    return fat

n = int(input('Informe o número para o cálculo da fatorial: '))
print('O fatorial de', n, 'é', fatorial(n))
