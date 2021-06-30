import random

tries = 0
print("Guess a number between 1 and 10")
guess = input(f"Enter guess #{tries}: ")
random1 = random.randint(1,10)

while tries < 10 and guess != random1:
    guess = int(input("Guess a number between 1 and 5\n"))
    tries += 1
    if guess == random1:
        print(f"You win! The secret number is {random1}. You tried {tries} times!")
        break
    elif tries == 5:
        print(f"Sorry. The number was {random1}.")




# while tries < 5 and guess != random1:
#     guess = int(input("Guess a number between 1 and 5\n"))
#     tries += 1
#     if guess == random1:
#         print(f"You win! The secret number is {random1}. You tried {tries} times!")
#         break
#     elif tries == 5:
#         print(f"Sorry. The number was {random1}.")


# value = random.randint(1, 5)
# count = 0
# guess = 0
# while guess != value:
#     count += 1
#     guess = input('Guess a number between 1 and 5: ')
#     if guess.isnumeric():
#         guess = int(guess)
# else:
#     print(f'You guessed it in {count} tries!')