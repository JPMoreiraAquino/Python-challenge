while True:
    print("type two number")
    x = input()
    y = input()

    x = int(x)
    y = int(y)

    high = 0
    smaller = 0
    sumodds = 0

    if x > y:
        high = x
    else:
        high = y

    if y < x:
        smaller = y
    else:
        smaller = x
    smaller += + 1

    while smaller < high:
        if smaller % 2 != 0:
            sumodds += smaller
        smaller += 1
    print(f"SOMA DOS IMPARES = {sumodds}")










