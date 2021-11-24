
try:
    price = input("price of the product: ")
    product_quantity = input("quantity of the product: ")
    money_received = input("received money: ")

    price = float(price)
    product_quantity = int(product_quantity)
    money_received = float(money_received)

    price_pay = price * product_quantity

    change_of_money = money_received - price_pay
    if change_of_money < 0:
        print(f"You owe = {change_of_money:.2f}")
    else:
        print(f'Change of money = {change_of_money:.2f}')
except:
    print("Enter only Numbers")

