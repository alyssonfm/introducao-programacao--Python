# Programa para calcular média e imprimir situação, com testes em sequência
nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
nota3 = float(input('Informe a nota 3: '))
media = (nota1 + nota2 + nota3)/3
print('A média é: {:.2f}'.format(media))
if media < 7:
    if media < 4:
        print("Ficou reprovado X(")
    else:
        print("Ficou para a prova final :-(")
else:
    print("Passou por média :)")

# Forma alternativa usando elif
nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
nota3 = float(input('Informe a nota 3: '))
media = (nota1 + nota2 + nota3)/3
print('A média é: {:.2f}'.format(media))
if media < 4:
    print("Ficou reprovado X(")
elif media < 7:
    print("Ficou para a prova final :-(")        
else:
    print("Passou por média :)")
