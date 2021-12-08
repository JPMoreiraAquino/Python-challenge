N = input("want numbers you will typer?: ")
N = int(N)
accumulator = 0
vet: [float] = [0 for x in range(N)]

for i in range(N):
    vet[i] = int(input("type one number: "))


print()
print("pair numbers".upper())
for i in range(N):
    if not vet[i] % 2 != 0:
        print(f"{vet[i]:.0f}", end="  ")
        accumulator += 1
print()
print(f"number pairs = {accumulator}")

