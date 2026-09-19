# simple bill calculator

price = float(input("enter the price of one item: "))
quantity = int(input("enter the quantity: "))

total = price * quantity
print(f"{quantity} items at {price: .2f} each ={total: .2f}")
