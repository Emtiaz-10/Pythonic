names = []

with open("D:/ML/Python/IO/names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names, reverse=True):
    print("Hello,",name.capitalize().strip())