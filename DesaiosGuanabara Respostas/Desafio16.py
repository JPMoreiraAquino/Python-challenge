qtd_fumoPorDia = int(input("Quantos cigarros você consome por dia? "))
qtd_anos = float(input("Quantos anos você ficou fumando? "))

minutosPerdidos = qtd_fumoPorDia * 10
anos = 365 * qtd_anos
minutos_total = minutosPerdidos * anos
qtd_horas = minutos_total / 60
dias = qtd_horas / 24


print(f"você perdera {dias:.1f} dias de vida")
print(f'você perdera {int(qtd_horas)} horas de vida')
print(f"você perdera {int(minutos_total)} minutos de vida")
print(f"você perdera {int(minutos_total * 60)} segundos de vida")
