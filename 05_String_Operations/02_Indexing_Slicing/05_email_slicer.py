email = input("Enter yur email: ")

index = email.find("@")              #find index of "@"
index_ = email.index("@")

username = email[ : index]

domain = email[index+1 : ]

print(f"{index} / {index_}")

print(f"Your username is {username} and domain is {domain}")