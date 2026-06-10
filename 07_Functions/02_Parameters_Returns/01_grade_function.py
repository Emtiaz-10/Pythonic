def main():

  x = float(input("enter a number: "))
  if x>=0 and x<=100:
      grade(x)
  else:
      print("Invalid number")

def grade(x):
    print("Grade: ", end="")
    if x<=100  and x>=90:
        print("A")
    elif x<90 and x>=80:
        print("B")
    elif x <80 and x>=70:
        print("C")
    elif x<70 and x>=60:
        print("D")
    else:
        print("F")
    
main()