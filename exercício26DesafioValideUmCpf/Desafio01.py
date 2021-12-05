cpf = '16899535009'

new_cpf = cpf[:-2]
reserve = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(new_cpf[index]) * reserve

    reserve -= 1
    if reserve < 2:
        reserve = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        new_cpf += str(d)

if cpf == new_cpf:
    print("CPF Valid".upper())
else:
    print("CPF invalid".upper())