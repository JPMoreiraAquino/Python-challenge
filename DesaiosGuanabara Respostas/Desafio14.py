qtd_km = float(input("quantidade de quilômetros rodados?: "))
qtd_dias = int(input("Quantidade de Dias alugado?: "))

valor_dias = 90 * qtd_dias
valor_kmRodados = 0.20 * qtd_km

print(f"Valor total a pagar R${valor_dias + valor_kmRodados:.2f} ")
