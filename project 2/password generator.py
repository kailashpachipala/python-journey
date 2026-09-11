import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+"

print("Welcome to the Password Generator!")
no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like in your password?\n"))
no_of_numbers = int(input("How many numbers would you like in your password?\n"))

# easy method 

# password = " "
# for i in range (1, no_of_letters + 1):
#     password += random.choice(letters)

# for i in range (1, no_of_symbols + 1):
#     password += random.choice(symbols)

# for i in range (1, no_of_numbers + 1):
#     password += random.choice(numbers)

# print(f"Your generated password is: {password}")


# hard method

password_list = []
for i in range (1, no_of_letters + 1):
    char = random.choice(letters)
    password_list += char

for i in range (1, no_of_symbols + 1):
    char = random.choice(symbols)
    password_list += char

for i in range (1, no_of_numbers + 1):
    char = random.choice(numbers)
    password_list += char

random.shuffle(password_list)
password = " ".join(password_list)
print(f"Your generated password is: {password}")    
