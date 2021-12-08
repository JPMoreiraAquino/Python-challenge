n = input("Quantas pessoa serão digitadas?: ")
n = int(n)
idadeL = []
alturaa = []
nomeL = []
alturasoma = 0
menos16 = 0
todasidades = 0


for i in range(n):
    print(f"dados da {i+1} pessoa: ")
    nome = input("Digite seu nome:")
    nome = str(nome)
    idade = input("Digite sua idade: ")
    idade = int(idade)
    altura = input("Digite sua altura: ")
    altura = float(altura)
    nomeL.append(nome)
    idadeL.append(idade)
    alturaa.append(altura)

for i in range(n):
    alturasoma += alturaa[i]
for i in range(n):
    if idadeL[i] < 16:
        menos16 += 1
    else:
        todasidades += 1

print(todasidades, menos16)
print(f"altura Média:{alturasoma / n}")
print(f"Pessoa com menos de 16 anos:{(menos16 /) * menos16}")





