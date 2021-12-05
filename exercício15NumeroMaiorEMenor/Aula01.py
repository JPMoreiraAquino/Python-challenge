while True:
    print("typer two numbers: ")
    x = input()
    y = input()

    x = int(x)
    y = int(y)

    if y > x:
        print("growing".upper())
    elif x > y:
        print("decreasing".upper())
    else:
        print("waxed")
        break
