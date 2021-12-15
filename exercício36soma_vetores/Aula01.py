N = input("How many values will each vector have: ")
N = int(N)

vet: [int] = [0 for x in range(N)]
vet2: [int] = [0 for x in range(N)]

print("enter the values of the vector A:")
for A in range(N):
    vet[A] = input()
    vet[A] = int(vet[A])

print("enter the values of the vector B:")
for B in range(N):
    vet2[B] = input()
    vet2[B] = int(vet2[B])

print("RESULTING VECTOR:")
for C in range(N):
    print(vet[C] + vet2[C])