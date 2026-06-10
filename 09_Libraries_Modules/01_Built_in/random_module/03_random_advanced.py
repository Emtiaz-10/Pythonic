from random import shuffle,randint,choice,sample

def main():
    nums= ['2','3','4','5','6','7','8','9','10']
    cards = ['J','Q','K','A']

    p,q=shuffle_deck(nums,cards)
    print("shuffled: ",p,q)

    x,y = pick(p,q)
    print("picked: ",x,y)




def shuffle_deck(x,y):
    shuffle(x)
    shuffle(y)
    return x,y

def pick(x,y):
    return choice(x),choice(y)

main()