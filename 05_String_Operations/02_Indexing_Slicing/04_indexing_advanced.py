# indexing = accessing elements of a sequence using [] (indexing operator) 
#                          [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:5])
print(credit_number[:5])       #indicating startig index at [starting address]
print(credit_number[5:9])
print(credit_number[5:])       #indicateing ending index at [end address]
print(credit_number[-1])       #******negative indexing means counting from the ending index****

print(credit_number[::])       #print whole str
print(credit_number[::2])      #print index after index[0]+2 eveytime before null

print(credit_number[ : : -1 ]) #reverse index

print(f"Your credit number is: XXXX-XXXX-XXXX-{credit_number[-4:]}")