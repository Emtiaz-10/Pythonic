def main():
    print("Welcome to the calculator!")
    n = float(input("Enter a number: "))
    square(n)

def square(x):
    return x+x

if __name__ == "__main__":
    main()