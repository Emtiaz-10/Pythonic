import random

lowest_num=10
highest_num=20

num = random.randint(lowest_num,highest_num)

is_running=True
guesses = 0
print()
print("*******-----------Python Guess Game--------********")
print()
while is_running:
      guess = input("Enter your guess : ")

      if guess.isdigit():
            guess = int(guess)
            guesses += 1
            
            if guess < lowest_num or guess > highest_num:
                  print("Enter a valid value") 
                  print(f"Please enter a number between {lowest_num}-{highest_num} : ")

            elif guess>num:
                  print(f"{guess} is too high")

            elif guess <num:
                  print(f"{guess} is too low")

            else:
                  print()
                  print("Congratulations!")
                  print(f"{guess} is correct.")


                  is_running = False

      else:
            print("Invalid guess")
            print(f"Please enter a number between {lowest_num}-{highest_num} : ")

print()
print(f"Your required {guesses} attempts.")


