variable = ["Talia", "João Pedro", "jp"]

start_with_j = False

for valor in variable:
    if valor.lower().startswith("j"):
        start_with_j = True

if start_with_j:
    print(f"there is a word that starts with J")
else:
    print(f"there is no word with J")