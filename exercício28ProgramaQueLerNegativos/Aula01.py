n = input("how many numbers will you type?:")
n = int(n)

negative_numbers = []
accumulator = 0
if n > 10:
    print('impossible to calculate'.upper())
else:
    for i in range(n):
        num = input("typer one number:")
        num = float(num)
        if num < 0:
            negative_numbers.append(num)
            accumulator += 1

    print('negative numbers'.upper())
    for i in range(accumulator):
        print(negative_numbers[i])



