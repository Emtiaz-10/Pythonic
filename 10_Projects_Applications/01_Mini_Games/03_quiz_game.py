questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet in the solar system is the hottest?: ")

options = (
("A. 116", "B. 117", "C. 118", "D. 119"),
("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
("A. 206", "B. 207", "C. 208", "D. 209"),
("A. Mercury", "B. Venus", "C. Earth", "D. Mars") )

answers = ("C", "D", "A", "A", "B")

guesses = []

ques_num = 0
score = 0

for ques in questions:
    print(" - - - - - ")
    print (ques)
    for opt in options[ques_num]:
        print(opt)

    guess = input("Your choice: ").upper()
    guesses.append(guess)

    if guess == answers[ques_num]:
       score += 1
       print("Answer is correct")
    else:   
        print ("wrong answer")

    ques_num += 1

print(answers,end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
     print(guess,end=" ")

print(f"Total score = {score}")




