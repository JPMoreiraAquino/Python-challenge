soma = 0
x = input("type one number: ")
x = int(x)

while x != 0:
    soma += x
    x = input("type others numbers: ")
    x = int(x)
print(f"SUM = {soma}")
