
times_tables = input("what number you want the multiplication table for what value: ")
IN = input("in: ")
IN = int(IN)

times_tables = int(times_tables)

for i in range(1, IN+1):
    print(f"{times_tables} X {i} = {times_tables * i}")

