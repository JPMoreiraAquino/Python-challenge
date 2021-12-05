A = input("enter the measure of A: ")
B = input("enter the measure of B: ")
C = input("enter the measure of C: ")

A = float(A)
B = float(B)
C = float(C)

square_calculus = A * A
triangle_calculus = A * B / 2
trapeze_calculus = (A + B) * C / 2

print(f"Square area = {square_calculus:.4f}")
print(f"triangle area = {triangle_calculus:.4f}")
print(f"Trapeze area = {trapeze_calculus:.4f}")
