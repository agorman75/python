# print((4 <= 2 * 3) and (7 + 1 == 8))
# print(4 * 5 <= 21 - 1)

# x = 5
 
# if x <= 2:
#   print("This is printed")
# if x <= 4:
#   print("This is also printed")
# if x <= 6:
#   print("Is this printed?")
# if x <= 8:
#   print("This might be printed.")

# print((9 - 4) * 2 == 77 / 7 - 1)

# orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# orders2 = ["flower", "foot", "fake"]

# # for n in orders2:
# #     # orders.append(n)
# #     orders
# # orders.append(orders2)

# print(orders + [2]["help"])

def solution(number):
    add = 0
    for n in number:
        add = 0
        if n % 3 == 0 or n % 5 == 0:
            add += n
    return print(add)

number = 1