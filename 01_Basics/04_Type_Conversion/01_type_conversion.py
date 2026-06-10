a = 2

b = "5" #string

c = 7.92

d = a + c  # a int , c float
print("d = ",d,type(d))

e = int(d) #float to  int
print("e =", e)

'''
   int() can only covert valid numerical values into integer type from char or string type
   int(2) valid but int("go") will return ValueError
   
   str() can convert anything into string type
   str(2) , str(#) , str(+) all valid
   z = "python"
   y = int(z)           # y will return ValueError
'''

f = int(b) #converts from string to int type
g = a + f
print("g =", g)

s = str(c) # int type to string type
x = b + s  # concatenation = add of 2 strings
print("x =", x)



