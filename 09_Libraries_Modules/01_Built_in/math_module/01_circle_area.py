import math
radius =float(input("Enter radius(cm):"))

circumference = 2 * math.pi * radius

area = math.pi * pow(radius,2)

print(round(circumference,2))
print(f"{round(area,2)}")