segundos_min = 60
segundos_hora = 60 * segundos_min
segundos_dia = 24 * segundos_hora
segundos_em_1ano = 365 * segundos_dia
idade_anos = 14000000000
tempo_segundos = idade_anos * segundos_em_1ano
print("O Universo tem aproximadamente", "{:,} segundos de vida.".format(tempo_segundos))
