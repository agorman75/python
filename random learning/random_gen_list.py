import random

the_list = ['John', 'Joe', 'Andrew', 'Ted']

# n = len(the_list) - 1
ran = random.randint(0,len(the_list) - 1)

print("Here is the list: " + str(tuple(the_list)),"\n" + str(the_list[ran]) + " was selected.")