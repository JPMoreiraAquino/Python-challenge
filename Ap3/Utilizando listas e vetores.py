N = input("how many elements the vector have: ")   #pt-br UTF-8 Colocamos uma variável "N" para saber quantos números sera divisível para calcular a média e para da range no for
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
"""
Adicionamos o menor número a uma lista
"""
print(f'vector mean = {Media / N}')

print(f'ELEMENTS BELOW AVERAGE: ')
for i in eadm:
    print(i)
"""
En seguida imprimimos na tela a lista com os menores números  
"""










