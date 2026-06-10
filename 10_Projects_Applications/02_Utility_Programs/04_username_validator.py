username = input("enter username:")

if len(username) > 12:
    print("Username cannot be more than 12 charachters.")
elif username.find(" ") == 1:
    print("Username cannot contain spaces.")
elif not username.isalpha(): 
    print("Username can only contain alphabet.")
else:
    print(f"Welcome {username}")    
