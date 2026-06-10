import math
#Right angled triangle
A=float(input("Enter side a:"))
B=float(input("Enter side b:"))

C = math.sqrt(pow(A,2)+pow(B,2))

print(round(C,2))

area = .5*A*B
print(area)