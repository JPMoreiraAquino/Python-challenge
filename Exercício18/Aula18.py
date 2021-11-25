y = input("register your password: ")
y = int(y)


print("type your passwoed")
x = input("")
x = int(x)


while x != y:
    print("invalid password, try again")
    x = input("")
    x = int(x)

print("allowed access")
