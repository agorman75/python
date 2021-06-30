import random
name = str(input("What is your name?"))
secretnumber = random.randint(1,20)
print(f"Well {name}, I am thinking of a number between 1 and 20.")

def guessestaken():
    guess = int(input("Take a guess."))
    for x in range(1,7):
        if guess < secretnumber:
            print("Your guess is too low")
        elif guess > secretnumber:
            print("Your guess is too high")
        else:
            break

guessestaken()



# import random
# name = str(input("What is your name?"))
# secretnumber = random.randint(1,20)
# print(f"Well {name}, I am thinking of a number between 1 and 20.")

# for guessestaken in range(1,7):
#     guess = int(input("Take a guess."))
#     if guess < secretnumber:
#         print("Your guess is too low")
#     elif guess > secretnumber:
#         print("Your guess is too high")
#     else:
#         break

# if guess == secretnumber:
#     print(f"Good job {name}! You guessed my number in {guessestaken}!")
# else:
#     print(f"Nope. THe number I was thinking about is {secretnumber}!")