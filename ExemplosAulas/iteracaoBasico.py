# Multiplicação como somas sucessivas
multiplicando = int(input('Informe o valor do multiplicando: '))
multiplicador = int(input('Informe o valor do multiplicador: '))
produto = 0
for i in range(multiplicador):
    produto = produto + multiplicando
print('O valor da multiplicação de',multiplicando, 'por', multiplicador, 'é:', produto)
