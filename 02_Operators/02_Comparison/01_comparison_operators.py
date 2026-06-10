print(0.1+0.2 == 0.3)  # converts to binary so timny error happens

import math
print(math.isclose(.1+.2,.3))

#------------------------------

x = "apple"
if x == "apple" or "orange":
    print("found")

if x in ["apple","orange"]:             #cleaner code
    print("found")