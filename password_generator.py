# ==============================
#      PASSWORD GENERATOR
# ==============================

import random
import string

print("===================================")
print("      WELCOME TO PASSWORD")
print("         GENERATOR APP")
print("===================================")

# Taking password length from user
length = int(input("Enter the desired password length: "))

# Defining character sets
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Combining all characters
all_characters = letters + numbers + symbols

# Generating password
password = ""

for i in range(length):
    random_character = random.choice(all_characters)
    password += random_character

# Displaying generated password
print("\n===================================")
print(" Your Generated Password Is:")
print(" ", password)
print("===================================")

# Checking password strength
if length <= 5:
    print("Password Strength: Weak")
elif length <= 10:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

print("\nThank You For Using Password Generator!")
