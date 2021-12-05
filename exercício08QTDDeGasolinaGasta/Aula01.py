distance = input("enter the distance covered: ")
spent_fuel = input("type the spent fuel: ")

distance = int(distance)
spent_fuel = float(spent_fuel)

consumption = distance / spent_fuel

print(f"Average consumption = {consumption:.3f}")

