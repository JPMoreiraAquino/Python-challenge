N = input("How many values will each vector have: ")
N = int(N)

vectorA = []

vectorB = []


print("enter the values of the vector A:")
for A in range(N):
    vector = input()
    vector = int(vector)
    vectorA.append(vector)


print("enter the values of the vector B:")
for B in range(N):
    vector = input()
    vector = int(vector)
    vectorB.append(vector)

print("RESULTING VECTOR:")
for C in range(N):
    soma = vectorA[C] + vectorB[C]
    print(soma)


