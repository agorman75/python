# input_number = int(input("Please provide a number\n"))
# print(f"Your number is {input_number} ")

# if input_number > 0:
#     print(f"The number you provided {input_number} is larger than 0")
# else:
#     print(f"Te number you privded {input_number} is smaller than 0")


# i = 0
# while i != 100:
#     i = int(input("Please enter a number"))
#     if i == 30:
#         break

# Simple password checker
i = 0
pw = ''
while pw != 'pass':
    pw = str(input("Enter password \n"))
    i += 1
    if i == 3:
        print("access denied \n")
        break
    elif pw == 'pass':
        print("granted")
        break

# l = [1,3,4]
# for x in l:
#     print(x)