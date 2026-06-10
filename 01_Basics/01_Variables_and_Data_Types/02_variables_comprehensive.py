# Variable = A container for a value (string, integer, float, boolean)
#A variable behaves as if it was the value it contains

#f-string
#To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quo-tation mark. Inside this string, you can write a Python expression between { and } characters that can refer
#to variables or literal values.

#String
name = str(input("Enter your Name:"))
food = str(input("Enter food Name:"))
email = str(input("Enter Email ID:"))

#Integers
age = int(input("Enter your age: "))
quantity = 3
num_of_students = 50

#float
price = int(input("Enter price: "))

#  *******infinite while loop controlling system at a specific point********

while True:
    gpa = float(input("Enter your GPA: "))
    if 0<=gpa<=4:
     break
    else:
     print(f"Error value of GPA!")
    
distance = 3.8

#Boolean
is_student = True
is_graduate = False
for_sell = True
is_online = True

if age >= 25 :
    is_graduate = True
    print(f"\n{name} is Graduated: {is_graduate} ")
else:
    print(f"\n{name} is Graduated: {is_graduate} ")   

if distance<=4 and quantity<4:
    print(f"\n{food} is available : {for_sell} ")
    print(f"price of {food} is : ${price:.2f}")
else:
    for_sell = False
    print(f"\n{food} is available : {for_sell} ")

if 3.7<=gpa<=4:
    is_online=False
    print(f"\n{name} is online : {is_online}")
    print(f"ID = {email} is offline ")
else:
    print(f"\n{name} is online : {is_online}")
    print(f"ID = {email} is online")







