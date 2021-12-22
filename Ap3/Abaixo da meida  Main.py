N = input("how many elements the vector have: ")
N = int(N)
"""
pt-br UTF-8 Colocamos uma variável "N" para saber quantos números sera divisível para calcular a média e para da range 
for 
"""

vet: [int] = [0 for x in range(N)]
vet2: [int] = [0 for x in range(N)]
Media = 0

for i in range(N):
    vet[i] = input("type one number: ")
    vet[i] = float(vet[i])
    Media += vet[i]
for i in range(N):
    if vet[i] < Media / N:
        vet2[i] += vet[i]
"""
Adicionamos o menor número um vetor 
"""
print(f'vector mean = {Media / N}')

print(f'ELEMENTS BELOW AVERAGE: ')
for i in vet2:
    if i == 0:
        None
    else:
        print(i)
"""
En seguida imprimimos na tela o vetor com os menores números  
"""










