N = input("how many elements the vector have: ")
N = int(N)

vet: [int] = [0 for x in range(N)]

Media = 0
eadm = []


for i in range(N):
    vet[i] = input("type one number: ")
    vet[i] = float(vet[i])
    Media += vet[i]
for i in range(N):
    if vet[i] < Media / N:
        eadm.append(vet[i])

print(f'vector mean = {Media / N}')

print(f'ELEMENTS BELOW AVERAGE = ')
for i in eadm:
    print(i)










