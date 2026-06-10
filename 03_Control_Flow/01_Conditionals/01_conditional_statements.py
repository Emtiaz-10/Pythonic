# if-elif-else

#Python is an Indentation(proper spacing) based language. 4 spaces for if-elif-else statement.

"""
   if(condition):
       statement1
   elif(condition):
       statement2
   else:
       statementN
"""

light = input("light = ")

if light== "red":
    print("Stop")
elif light == 'yellow':
    print ("look")
elif light == 'green':
    print("Go")
else:
    print("Light is broken")
