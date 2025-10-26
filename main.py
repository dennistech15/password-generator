import random
import string

print("Welcome to the Glorious Password Generator!")

length = int(input("Password length: "))

use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
use_digits = input("Include digits? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

characters = ""
if use_lower:
    characters += string.ascii_lowercase
if use_upper:
    characters += string.ascii_uppercase
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if not characters:
    print("You must select at least one character type!")
    exit()

password = ''.join(random.choice(characters) for _ in range(length))

print("\nYour generated password is:", password)
