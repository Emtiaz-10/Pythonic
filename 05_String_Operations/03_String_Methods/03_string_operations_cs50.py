print("hello, world!")
#ask user for name
name = input("What's your name?")
"""
then say hello to user
"""
print(f"hello {name}")
print("hello, " + name)

name = name.strip().capitalize()

print("hello,",name)
print("hello",name, sep=" ", end="\n")
print("hello, \"friend\"")

"""
remove whitespace and capitalize first letter of each word
"""
name = name.strip().title()
print("hello",name)

# split name into first and  last name
first, last = name.split(" ")
print("hello,", first)