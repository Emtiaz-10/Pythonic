import random

option = ("rock", "paper", "scissor")

is_running = True

while  is_running:

    computer = random.choice(option)
    guess = input("Enter a choice(rock, paper, scissor): ")
    print(computer)

    if guess == computer:
        print("It is a tie!")
    elif guess =="rock" and computer =="scissor":
        print("You win.")
    elif guess =="paper" and computer =="rock":
        print("You win.")    
    elif guess =="scissor" and computer =="paper":
        print("You win.")    
    else:
        print("Lose!")
    
    jarvis = input("Do you want to play again?(y/n): ").lower()

    while jarvis  != "y" and jarvis != "n":
          print("Enter y or n.")
          jarvis = input("Do you want to play again?(y/n): ").lower()


    if jarvis == "n":
        is_running = False
        print("Thank you.")

