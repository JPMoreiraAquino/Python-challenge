price = float(input("Qual o preço do produto: "))

desconto = (price / 100) * 5
print(f"Seu desconto vai ser igual a R${(price / 100) * 5:.2f}")

print(f"O produto vai ficar por R${price - desconto:.2f}")

