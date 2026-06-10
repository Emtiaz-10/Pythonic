temp = float(input("Enter temperature: "))
unit = input("Is it in farenheit or celcius(F/C): ")

if unit == "c" or unit == "C":
    temp = round(9*temp/5+32,2)
    print(f"Temperature in farenheit is: {temp}°F")
elif unit == "f" or unit == "F":
    temp = round((temp-32)*5/9,2)
    print(f"Temperature in farenheit is: {temp}°C")  
else :
     print("Error")      