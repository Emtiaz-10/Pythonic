name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")    

age = float(input("Enter age:"))

while age <0:
    print("Enter valid age")
    age = float(input("Enter age:"))
print(f"Your age is {age}")    

food = input("Enter fav food(q for quit):")
while not food == "q" :
    print(f"{name}'s fav food is {food}")
    food = input("Enter fav food(q for quit):")
print("Thank u")   

num = float(input("enter num:"))

while num < 0 or num >100:
    print(f"{num} is invalid")
    num = float(input("enter num:"))
print(f"Num is {num}")    