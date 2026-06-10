import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(char)
keys = chars.copy()
random.shuffle(keys)

#print(chars)

##_____________________________________________________Encryption__________________________________________


plain_text = input("Enter : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(plain_text)
print(cipher_text)



##_____________________________________________________Encryption__________________________________________

cipher_text = input("Enter : ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(cipher_text)
print(plain_text)

