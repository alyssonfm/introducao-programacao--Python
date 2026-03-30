nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
nota3 = float(input('Informe a nota 3: '))
media = (nota1 + nota2 + nota3)/3
print('A média é: {:.2f}'.format(media))
match media:
    case _ if media < 4:
        print("Ficou reprovado X(")
    case _ if media < 7:
        print("Ficou para a prova final :-(")
    case _:
        print("Passou por média :)")
