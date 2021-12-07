
s = ''

while s != 's':
    n = input("N:")
    n = int(n)
    Ntabuada = input("de qual numero é a tabuada que voce vai utilzar: ")
    Ntabuada = int(Ntabuada)
    for i, v in enumerate(range(n+1)):
        print(f"{v}|{i} X {Ntabuada} = { i * Ntabuada}")
    s = input("Deseja para (s)im ou (n)ão: ")

