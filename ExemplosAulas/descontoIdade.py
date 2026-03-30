# Desconto por idade
idade = int(input('Qual a sua idade? '))
if idade >= 0 and idade < 12:
    print('Desconto é de 100%')
elif idade >= 12 and idade < 26:
    print('Desconto é de 50%')
else:
    print('Sem desconto')

# Usando algo mais próximo da matemática
idade = int(input('Qual a sua idade? '))
if 0 <= idade < 12:
    print('Desconto é de 100%')
elif 12 <= idade < 26:
    print('Desconto é de 50%')
else:
    print('Sem desconto')
