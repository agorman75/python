# # from typing import no_type_check


# # words = ['one', 'two', 'three', 'four', 'five']
# # n = 0
# # # while n < 5:
# # #     print(words[n])
# # #     n += 1

# # def hello(math):
# #     print("today!")

# # print(hello)

# def a_bigger(a=1, b=2):
#   if a > b and (a - b) >= 2:
#     return True
#   else:
#     return False

# print(a_bigger(2))

# example = set()
# print(dir(example))

# example = set()
# example.add(32)
# example.add('Thello')
# print(len(example))
# print(example)

# print(0xa)

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["color"] = "red"
# print(dic(car))

# txt = " Hello World "
# x = txt.strip()
# print(x)


# txt = "Hello World"
# txt = txt.replace("e","J")
# a = txt.upper()
# print(a)

# fruits = ["apple", "banana"]
# if "apple" in fruits:
#     print("Yes, apple is a fruit!")

# def d(dd):
#     try:
#         return 42 / dd
#     except ZeroDivisionError:
#         print("going to skip")

# print(d(0))

#####                 Guess the number
import random
# print("Hello. What is your name?")
# name = input()
# secretnumber = random.randint(1,20)
# print("Well, " + name + ", I am thinking of a number between 1 and 20")

# #Ask the player to guess 6 times.
# for guessestaken in range(1,7):
#     print("Take a guess.")
#     guess = int(input())
#     if guess < secretnumber:
#         print("Your guess is too low")
#     elif guess > secretnumber:
#         print("Your guess is too high")
#     else:
#         break

# if guess == secretnumber:
#     print("Good job " + name + "! You guessed my number in " + str(guessestaken))
# else:
#     print("Nope. The number I was thinking about is " + str(secretnumber))



name = str(input("What is your name?"))
secretnumber = random.randint(1,20)
print(f"Well {name}, I am thinking of a number between 1 and 20.")

for guessestaken in range(1,7):
    guess = int(input("Take a guess."))
    if guess < secretnumber:
        print("Your guess is too low")
    elif guess > secretnumber:
        print("Your guess is too high")
    else:
        break

if guess == secretnumber:
    print(f"Good job {name}! You guessed my number in {guessestaken}!")
else:
    print(f"Nope. THe number I was thinking about is {secretnumber}!")