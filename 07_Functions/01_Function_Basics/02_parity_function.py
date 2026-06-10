def main():
    x = int(input("Enter an integer: "))
    if is_even(x):
        print("Even")
        print("Next odd number:", parity_maker(x))
    else:
        print("Odd")
        print("Next even number:", parity_maker(x))

def is_even(x):
   return  x%2==0
  
def parity_maker(x):
    return x+1
main()