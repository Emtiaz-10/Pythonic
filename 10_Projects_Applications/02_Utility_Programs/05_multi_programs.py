# typecasting = The process of converting a value of one data type to another.
#          (string, integer, float, boolean)
#            Explicit vs Implicit


name = "jarvis"
age = 25
gpa = 3.7
student = True

print(name,type(name))
print(age,type(age))
print(gpa,type(gpa))
print(student,type(student))
print("\n")

#name = int(name)    *********str can not be changed into float or int data type

age = bool(age)
gpa = str(gpa)
student = int(student)


print(name,type(name))
print(age,type(age))
print(gpa,type(gpa))
print(student,type(student))

print("\n")
name = bool(name)
age = float(age)
student = str(student)

print(name,type(name))
print(age,type(age))
print(student,type(student))
