"""
<var> = <var1> if condition else <var2>

when if condition executes output will be var1(previous statement)
otherwise var2(lateral statement)

"""

food = input("food : ")

eat = "Yes!" if food == "cake" or food =="jalebi" else "No"
print(eat)

print("sweet") if food == "cake" or food == "jalebi" else print("Not sweet")