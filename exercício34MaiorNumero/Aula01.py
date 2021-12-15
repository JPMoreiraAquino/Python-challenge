N = input("want numbers you will typer?: ")
N = int(N)
greater_numbers = 0
posicao = 0


vet: [float] = [0 for x in range(N)]

for i in range(N):
    vet[i] = int(input("type one number: "))


print()
for i in range(N):
    if vet[i] > greater_numbers:
        greater_numbers = vet[i]
        posicao = i



print(f"greater numbers = {greater_numbers:.1f}")
print(f"HIGHEST VALUE POSITION = {posicao+1}")