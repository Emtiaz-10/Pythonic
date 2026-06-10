foods = []
prices = []
total = 0

while True:
    food = input("Enter item u want to buy(q for quit):")

    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of {food}:$"))
        foods.append(food)
        prices.append(price)
for food in foods:
    print(food,end=" ")
for price in(prices):
    total += price
    print(price, end =" ")    
print()
print(f"total = ${total:.2f}")   