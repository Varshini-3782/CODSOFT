import random

# Character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Welcome message
print("Welcome to Password Generator!")

# User input
password_length = int(input("Enter the desired length of the password:\n"))
num_symbols = int(input("How many symbols you want in your password?\n"))
num_numbers = int(input("How many numbers you want in your password?\n"))
num_letters = int(input("How many letters you want in your password?\n"))

# Generating password components
password_list = []

for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

for _ in range(num_numbers):
    password_list.append(random.choice(numbers))

for _ in range(num_letters):
    password_list.append(random.choice(letters))

# Shuffle the password list
random.shuffle(password_list)

# Convert list to string
password = ''.join(password_list)

# Output the password
print(f"Your generated password is: {password}")