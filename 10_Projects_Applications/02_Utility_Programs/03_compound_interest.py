
principle = 0
time = 0
rate =0

while principle <=0:
    principle = float(input("Enter principle amount:"))
    if principle < 0:
      print("Not valid")

while time <=0:
    time = float(input("Enter time:"))
    if time < 0:
      print("Not valid")

while rate <=0:
    rate = float(input("Enter rate:"))
    if rate < 0:
      print("Not valid")            

total = principle*pow((1+rate/100),time)

print(f"Balance after {time} year/s : ${total:.2f}")