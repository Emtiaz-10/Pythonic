x = float(input("enter a number: "))
y = float(input("enter a number: "))

z =  x + y

print(f"{x} + {y} = ",z)

"""round(z,2)  
   print(f"{z:2f})
"""

z = round(z)
print(z)
z= round(z,2)
print(f"{z:,}")