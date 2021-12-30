nDIas = int(input("Quantos dias voce trabalhou esse més? "))

if nDIas > 30:
    print(f"Não é possível Trabalhar {nDIas} em um més")
else: 
    print(f"salário = {(nDIas * 8) * 25}")
