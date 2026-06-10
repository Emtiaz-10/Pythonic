# conditional expression = a one line shortcut for the if-else statement(ternary operator)
#                          print or assign one of two values based on a condition
#                       X if condition else Y

num = float(input("Enter num: "))
print("Positive" if num>=0 else "Negative")
#print("\n")
a = float(input("Enter a: "))
b = float(input("Enter b: "))

result1 = "Even" if a%2 ==0 else "Odd"
result2 = "Even" if b%2 ==0 else "Odd"
print(result1 , result2)

max = a if a>b else b
min = a if a<b else b

print(f"max = {max} and min = {min}")

t = 20
print("Hot" if t>20 else "Normal")

role = "admin"
print("Full access" if role == "admin" else "Limited")

