menu = {"pizza": 3.00, 
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25} 

print("------------MENU---------------")
for key,value in menu.items():
    
    print(f"\t{key:10}:{value:.2f}")

cart = []
total=0 

while True:
      food = input("Enter food item(q for quit): ").lower()
      if food == "q":
           break
      elif menu.get(food) is not None:
            cart.append(food)
            
print("--------Your Order-----------")
print()
for food in cart:   
    total += menu.get(food)
   # print(food,end=" ")
    
    print(f"{food:10} : {menu.get(food):.2f}")

print()
print(f"Total = ${total:.2f}")