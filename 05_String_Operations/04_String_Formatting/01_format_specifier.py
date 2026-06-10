
# format specifiers = {value:flags} format a value based on what
#                      flags are inserted

# . (number)f = round to that many decimal places (fixed point)
# : (number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.98762
price2 =-4.789
price3 = 4000.895
price4 =-3456.239

print(f"${price1:.3f}")
print(f":(number) ${price1:10}")
print(f":(0number) ${price1:010}")
print(f":< =${price1:<10}")
print(f":> =${price1:>10}")
print(f":+ =${price1:+} ${price2:+} ")
print(f":^ =${price1:^10} ${price2:^10} ")
print(f":= =${price1:=} ${price2:=} ")
print(f":  =${price1: } ${price2: } ")

print(f":=,.2f =${price3:=,.2f} ${price4:=,.2f} ")
print(f": ,.2f =${price3: ,.2f} ${price4:= ,.2f} ")
print(f":+,.2f =${price3:+,.2f} ${price4:+,.2f} ")