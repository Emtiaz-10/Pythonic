import random

low = 1
high = 100

num = random.randint(low,high)

while True:
    guess = int(input(f"Enter number between ({low}-{high}):"))

    if guess<num:
        print(f"{guess} is too low")
    elif guess>num:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is equal to num={num}")    
        break