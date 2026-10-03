import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

letters_all = int(input("How many letters would you like in your password?\n"))
symbols_all = int(input("How many symbols would you like in your password?\n"))
number_all = int(input("How many numbers would you like in your password?\n"))


# EASY VERSION
# The easy version directly builds the password as a string by adding random characters one after another.

password = ""

for char in range(letters_all):
    password += random.choice(letters)

for char in range(symbols_all):
    password += random.choice(symbols)

for char in range(number_all):
    password += random.choice(numbers)

print(f"Easy version password: {password}")


# HARD VERSION
# The hard version first stores all characters in a list, shuffles them, and then joins them to create a random password.

password_list = []

for char in range(letters_all):
    password_list += random.choice(letters)

for char in range(symbols_all):
    password_list += random.choice(symbols)

for char in range(number_all):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Hard version password: {password}")
