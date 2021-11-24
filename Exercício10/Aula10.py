secund = input("enter the duration on secund: ")
secund = int(secund)

number_of_seconds = [3600, 60, 1]
result = []

for target in number_of_seconds:
    qtd = int(secund / target)
    result.append(str(qtd))
    secund -= qtd * target

print(":".join(result))


