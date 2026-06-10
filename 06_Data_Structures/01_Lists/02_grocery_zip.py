fruits =     ["apple","banana","coconut"]
vegetables = ["celery","carrots","potatoes"]
meats =      ["chicken","fish","turkey"]

grocery = [fruits,vegetables,meats]

categories = ["fruits", "vegetables", "meats"]

for item,index in zip(grocery,categories):
    print(index,":")
    for food in item:
        print(food,end=" ")

    print()
