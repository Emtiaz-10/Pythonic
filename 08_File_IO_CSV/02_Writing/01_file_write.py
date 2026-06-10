
with open("D:/ML/Python/IO/names.txt","a") as file:
    while True:
        name = input("Whats Your Name? ")
        if not name:
            break
        file.write(f"{name.strip()}\n")
