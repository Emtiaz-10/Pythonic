import random

low = 1
high = 6
cards = ["3","2","4","5","6","7","8","9","10","J","K","Q" ]
a = random.randint(1,6)
b = random.randint(low,high)

c = random.random()
random.shuffle(cards)
choice = random.choice(cards)
print(cards,choice)