# import random

# a = random.randint(1,20)
# count = 0

# def ran1():
#     global count
#     count += 1
#     if count < 6:
#         print("hello")
#     else:
#         print("NO")
        
        

# ran1()



#This is a guessing game
import random
print("Hello. What is your name?")
name = input()
secretnumber = random.randint(1,20)
print("Well, " + name + ", I am thinking of a number between 1 and 20.")

#Ask the player to guess 6 times
for guesstaken in range(1,7):
    print("Take your guess.")
    guess = int(input())
    if guess < secretnumber:
        print("Your guess is too low.")
    elif guess > secretnumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretnumber:
    print("Good job " + name + "! You guessed my number in the guessing game!")
else:
    print("Nope. The number I was thinking of was " +str(secretnumber))


# import random
# name = str(input("Hello. What is your name?"))
# while name != int():
#     print("Please provide a number")
#     if name == int():
#         continue
# secretnumber = random.randint(1,20)
# print(f"Well, {name}, I am thinking of a number between 1 and 20")

# for guesstaken in range(1,6):
#     guess = int(input("Take your guess."))
#     if guess < secretnumber:
#         print("Your guess is too low.")
#     elif guess > secretnumber:
#         print("Your guess is too high.")
#     else:
#         break

# if guess == secretnumber:
#     print(f"Good job {name}! You guessed my number in the guessing game!")
# else:
#     print("Nope. The number I was thinking of was " +str(secretnumber))