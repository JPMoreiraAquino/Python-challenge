nome = input("Nome do funcionário: ")
salario = input("Salário: ")

salario = float(salario)

if salario == type(float):
    print(f"O funcionário {nome} tem o salário de {salario} em junho")
else:
    salario = str(salario)
    print("seu salário não Apresente um valor")
    print(f"Salário = {salario}")
