cpf = '16899535009'

new_cpf = cpf[:-2]
reverse = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(new_cpf[index]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        new_cpf += str(d)

if cpf == new_cpf:
    print("CPF Valid".upper())
else:
    print("CPF invalid".upper())