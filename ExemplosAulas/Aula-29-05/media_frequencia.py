frequencia = int(input("Frequência: "))
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota1 + nota2 + nota3)/3
if media < 3.5 and frequencia < 75:
   print("Reprovado por faltas e media X(")
elif frequencia < 75:
   print("Reprovado por faltas X(")
else:
    if media >= 7.0:
        print("Aprovado :-)")
    elif 3.5 <= media < 7.0:
        print("Exame final")
    else:
        print("Reprovado :-(")
