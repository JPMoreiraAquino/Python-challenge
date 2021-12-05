age = input("how old are you: ")

if not age.isnumeric():
    print("you needs type only numbers ")
else:
    age = int(age)
    is_of_legal_age = (age >= 18)
    msg = 'permission granted' if is_of_legal_age else "you don't have access"

    print(msg)

