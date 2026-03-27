# Programa que calcula o tamanho do Universo em milimetros

segundos_min = 60
segundos_hora = 60 * segundos_min
segundos_dia = 24 * segundos_hora
segundos_em_1ano = 365 * segundos_dia
tamanho_anos_luz = 93000000000
velocidade_luz_mm = 299792458 * 1000
tamanho_universo_mm = tamanho_anos_luz * velocidade_luz_mm * segundos_em_1ano
print("O Universo tem aproximadamente", tamanho_universo_mm, "milímetros.")

print("O Universo tem aproximadamente", "{:,} milímetros.".format(tamanho_universo_mm))

# Programa que considera o ano com 365,25 dias
segundos_min = 60
segundos_hora = 60 * segundos_min
segundos_dia = 24 * segundos_hora
segundos_em_1ano = 365.25 * segundos_dia
tamanho_anos_luz = 93000000000
velocidade_luz_mm = 299792458 * 1000
tamanho_universo_mm = tamanho_anos_luz * velocidade_luz_mm * segundos_em_1ano
print("O Universo tem aproximadamente", tamanho_universo_mm, "milímetros.")
