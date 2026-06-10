import csv

students = []

with open("D:/ML/Python/IO/student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # students.append({"name":row['name'], "house":row['house'], "home":row['home']})
        students.append(row)

# Reading the CSV file and populating the students list
    # for line in file:
    #     name, house = line.rstrip().split(",")
    #     sd = {"name":name,"house":house}    # pair name and house
    #     students.append(sd)



#                   Function to get the name of a student from a dictionary
def get_name(student):
    return student["name"]

print()

#                                sorting based on name
for student in sorted(students , key = get_name):
    print(f"{student['name']} is in {student['house']} from {student['home']}.")   # single quote as double quote outside

print("\n\t------\t\t-------\t\t------\n")


#                       Using a lambda function sorting based house
for student in sorted(students , key = lambda student: student["house"]):
    print(f"{student['name']} is in {student['house']} from {student['home']}.")
print()