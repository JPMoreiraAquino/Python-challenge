
base = input("rectangle Base: ")
height = input("rectangle height: ")

base = float(base)
height = float(height)

area = base * height

perimeter = (base * 2) + (height * 2)
diagonal = (base**2) + (height**2)
raiz = diagonal ** (1/2)

print(f"AREA = {area:.4f}")
print(f"PERIMETER = {perimeter:.4f}")
print(f"DIAGONAL = {raiz:.4f}")
