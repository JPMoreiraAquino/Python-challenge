name = input("enter your name: ")
value_hours = input("Enter the Hourly value: ")
hours = input("Enter the Hours worked: ")

value_hours = float(value_hours)
hours = int(hours)

should_be = value_hours * hours

print(f"O pagamento para {name} deve ser {should_be:.2f}")

# print(f"O pagamento para {name} deve ser {value_hours * hours:.2f}")
