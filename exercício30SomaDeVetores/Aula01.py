
n = input("want numbers you will type?: ")
n = int(n)

valores = []
sum = 0
for i in range(1, n+1, 1):
    num = input("type one number:")
    num = float(num)
    valores.append(num)

for i in range(n):
    sum += valores[i]
print()
print("values = ", end="")
for i in valores:
    print(i, end="  ")


print()
print(f"Sum = {sum}")
print(f"Media = { sum / n}")
