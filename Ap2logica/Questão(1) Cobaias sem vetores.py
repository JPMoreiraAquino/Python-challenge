N = input("how many test cases will be entered?: ")
N = int(N)

lista1 = []
lista2 = []

total = 0
rabbit = 0
mouse = 0
frog = 0

for i in range(N):
    num = input("number of guinea pigs: ")
    num = int(num)
    tipo = input("type of guinea pig: ")
    tipo = str(tipo).upper()  #Coloquei o upper para caso a pessoa se esquecer de escrever a letra do animal maiúscula
    lista1.append(num)
    lista2.append(tipo)

    if not lista2[i] != "C":
        rabbit += lista1[i]
    elif not lista2[i] != "R":
        mouse += lista1[i]
    else:
        frog += lista1[i]
    total += lista1[i]

print("Final report:".upper())
print(f"Total: {total} guinea pigs ")
print(f"Total of rabbit: {rabbit}")
print(f"Total of mouse: {mouse}")
print(f"Total of frog: {frog}")
print(f"percentage of rabbit: {rabbit / total * 100:.2f}")
print(f"percentage of mouse: {mouse / total * 100:.2f}")
print(f"percentage of frog: {frog / total * 100:.2f}")