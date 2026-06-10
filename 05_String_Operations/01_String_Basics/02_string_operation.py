
str1 = "My"

'''
   My Room
   0123456
'''

str2 = "reading"

str3 = "room"

final = str1 + str2 +str3                          # concatenation = addition of 2 or more strings
print(final)

print(len(str1) , len(str2) , len(str3) )           #len() finds length of string
print(len(final))

final2 = str1+" "+str2+" "+str3
print(final2)
print(len(final2))

A , B = "2" , 3

C = "$"

# Numeric and string together operation

print(2*B*C,len(2*B*C))
print((A+C)*B,len((A+C)*B))