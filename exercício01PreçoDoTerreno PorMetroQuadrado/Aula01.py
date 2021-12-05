S1 = input("Digite a largura do terrono: ")
S2 = input("Digite o comprimento do terreno: ")

squareMeterPrice = input("Digite o valor por metro quadrado: ")
S1 = float(S1)
S2 = float(S2)
squareMeterPrice = float(squareMeterPrice)

area = S1 * S2
price = area * squareMeterPrice

print(f"Area do terreno = {area:.2f}")
print(f"Preco do terreno = {price:.2f}")

