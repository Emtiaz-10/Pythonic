a = int(input("a = "))
b = int(input("b (Can't be 0) = "))

#arithmatic operators +,-,*,/,%,**

print('\na + b =', a+b)
print('a - b =', a-b)
print('a*b = ', a*b)
print('a/b = ', a/b)
print('a%b =', a%b)    # remainder
print('a**b =', a**b)  # b is the power upon a here a^b

#comparison/relational operator <,>,==,!=,>=,<=

print('\na>=b ', a>=b)
print('a<=b ', a<=b)
print('a!=b ', a!=b)
print('a==b', a==b)

#assignment operator =,+=,-=,*=,/=,%=,**=
a=b
print('\na=b a= ', a, 'b = ' , b)
a+=b
print('a+=b a =', a, 'b =', b) #a=a+b
a-=b
print('a-=b a =', a, 'b =', b) #a=a-b

#logical operator  or,and ,not
print('\n')
a = 30
b= 20

print(not True)
print(not(a>b))

print("True and False", True and False)
print("True and True", True and True)

print("True or False", True or False)
print("True or False", False or True)
print("False or False", False or False)

print( (a==b) or (a>b) )
print((a==b) or (a>b))







