N = input("how many test cases will be entered?: ")
N = int(N)

vet: [int] = [0 for x in range(N)]
vet2: [int] = [0 for x in range(N)]
total = 0
rabbit = 0
mouse = 0
frog = 0

for i in range(N):
    vet[i] = input("number of guinea pigs: ")
    vet[i] = int(vet[i])
    vet2[i] = input("type of guinea pig: ")
    vet2[i] = str(vet2[i]).upper()  #Coloquei o upper para caso a pessoa se esquecer de escrever a letra do animal maiúscula
    if not vet2[i] != "C":
        rabbit += vet[i]
    elif not vet2[i] != "R":
        mouse += vet[i]
    else:
        frog += vet[i]
    total += vet[i]

print("Final report:".upper())
print(f"Total: {total} guinea pigs ")
print(f"Total of rabbit: {rabbit}")
print(f"Total of mouse: {mouse}")
print(f"Total of frog: {frog}")
print(f"percentage of rabbit: {rabbit / total * 100:.2f}")
print(f"percentage of mouse: {mouse / total * 100:.2f}")
print(f"percentage of frog: {frog / total * 100:.2f}")