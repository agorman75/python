import random


print("Password generator")
print("----------------------------------")
print()

# chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=;:',<.>/?]}"

# size = input("How many characters to the password would you like to generate? ")
# amount = input("How many passwords would you like? ")

# num_size = range(int(size))

# for num in range(int(amount)):
#     password = ""
#     for char in num_size:
#         password += random.choice(chars)
#     print("\nHere is your password:")
#     print(password)


def pw_gen(size, amount):
    for num in range(int(amount)):
        password = ""
        num_size = range(int(size))
        for char in num_size:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=;:',<.>/?]}"
            password += random.choice(chars)
        print("\nHere is your password:")
        print(password)

pw_gen(size = input("How many characters to the password would you like to generate? "), amount = input("How many passwords would you like? "))