print("first person data:")
print('')
name = input("Type your name: ")
age = input("how old are you: ")
print("")
print("second person data:")
name2 = input("ender the second name: ")
age2 = input("what is your second age: ")

age = int(age)
age2 = int(age2)

print(f"A idade media de {name} e {name2} é de {(age + age2) / 2}")