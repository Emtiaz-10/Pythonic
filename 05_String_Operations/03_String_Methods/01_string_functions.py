str1 = "I am learning Python. Python is interesting to learn."

# str.capitalize() capitalize 1st char of string only

print(str.capitalize(str1))
print(str1)

# str.count() count occurrences of sub string

print(str1.count("Python"))
print(str1.count(" "))

# str.replace(old,new) replace old with new

print(str1.replace("Python","ML"))
print(str1.replace(" ",""))
print("\n")
a = str1.replace("Python","ML")
print(a)
b=a.replace(" ","")
print(b)

# str.find() finds first index of first occurrence of sub string

print(str1.find("Python"))

# str.endswith()  returns True if the sting ends with sub string

print(str1.endswith("."))