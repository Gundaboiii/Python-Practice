import random
import string

def encode():
    n = input("Enter a string for converting it to the secret language: ")
    if len(n) > 3:
        first_random_letters = ''.join(random.choices(string.ascii_letters, k=3))
        last_random_letters = ''.join(random.choices(string.ascii_letters, k=3))
        first_letter = n[0]
        new_string = first_random_letters + n[1:] + n[0] + last_random_letters
    else:
        new_string = n[::-1]
    print(new_string)

def decode():
    n = input("Enter a string to decode it from Secret Language to English: ")
    if len(n) > 3:
        new_string = n[-4] + n[3:-4]
    else:
        new_string = n[::-1]
    print(new_string)


print("Welcome to Secret Language conversion code")
option = int(input("Enter 1 to encode a string or 0 to decode a string: "))
if option == 1:
    encode()
elif option == 0:
    decode()
else:
    print("Invalid option entered")

    
