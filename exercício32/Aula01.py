N = input("want numbers you will typer?: ")
N = int(N)

vet: [float] = [0 for x in range(N)]

for i in range(N):
    vet[i] = float(input("type one number: "))

print()

print("negative numbers".upper())
for i in range(N):
    if vet[i] < 0:
        print(f"{vet[i]:.1f}")
