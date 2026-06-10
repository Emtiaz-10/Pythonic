name = input("Enter your full name:")
a = input("Enter which you want to find:")

r1 = len(name)
r2 = name.find(a)               #find first occurance 
r3 = name.rfind(a)               #find last occurance
r4 = name.capitalize()          #capitalize first letter
r5 = name.lower()               #lower whole str
r6 = name.upper()               #capitalize whole str
r7 = name.count("a")            #count occurance of a given str or char
r8 = name.isdigit()             #output(Boolean) "False" if the str contain any alphabet except number
r9 = name.isalpha()             #output(Boolean) "False" if the str contain any num or blank except alphabet

name1 = name.replace(" ","")
r10 = name1.isalpha()


print(r1 , r2 , r3 , r4 , r5 , r6 , r7 , r8 , r9 , name1 , r10)

