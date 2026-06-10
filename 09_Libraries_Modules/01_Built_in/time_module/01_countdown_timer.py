import time
t = int(input("Enter seconds:"))

for y in range(t,0,-1):
         seconds = y % 60
         mins = int (y / 60) % 60
         hours = int (y / 3600) % 24
         print(f"{hours:02}:{mins:02}:{seconds:02}")
         time.sleep(1)