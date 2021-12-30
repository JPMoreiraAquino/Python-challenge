salario = float(input("Qual o seu salário?: "))

add = (salario / 100) * 15
print(f"Seu aumento vai ser igual a R${(salario / 100) * 15:.2f}")

print(f"O seu novo salário vai ficar igual a R${salario + add:.2f}")