n = input("Quantas pessoa serão digitadas?: ")
n = int(n)

idadeL = []
alturaa = []
nomeL = []
alturasoma = 0
menos16 = 0
todasidades = 0

nomeMenor16 = []


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
        todasidades += 1
        nomeMenor16.append(nomeL[i])
    else:
        todasidades += 1




print(f"altura Média:{alturasoma / n}")
print(f"Pessoa com menos de 16 anos: {menos16 / todasidades * 100:.0f}%")

for i in range(n):
    try:
        print(nomeMenor16[i] or "nao existe nenhuma pessoa com menos de 16 :(")
    except:
        False










