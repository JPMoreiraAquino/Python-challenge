
para = 'n'

while True:
    if para == 's':
        break
    print("type two numbers: ")
    x = input()
    y = input()

    x = int(x)
    y = int(y)

    maior = x if x > y else y
    menor = y if y < x else x
    menor += 1
    soma = 0

    while menor < maior:
        if menor % 2 != 0:
            soma += menor
        menor += 1
    print(f"SUM OF THE ODDS = {soma}")
    para = input("Quer para (s)im / (n)ão: ")
