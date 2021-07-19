# Can accomplish the same thing with for loop, but with less coding

numbers = [1,2,3,4,5,6,7,8,9]

new_list = []

for num in numbers:
    new_list.append(num+num)
print(new_list)

new_list = [num*2 for num in numbers]
print(new_list)

# give me a list with num for each num in numbers if num is even 
new_list1 = [num for num in numbers if num % 2 == 0]
print(new_list1)

#lambda function
new_list2 = filter(lambda num: num % 2 == 0, numbers)
print(list(new_list2))

numbers2 = [1,2,3,4,5,6,7,8,9]

l2 = [num for num in numbers2 and numbers if num % 2 == 0]
print(l2)

# pos1 = [num for num in range(1,101)]
# print(pos1)

# pos2 = [num**2 % 5 for num in range(1, 101)]
# print(pos2)

# pos3 = [num**2 % 11 for num in range(1,101)]
# print(pos3)

movies = ["Star Wars", "Groundhod Day", "Good Will Hunting", "Bad Santa"]
movies2 = [movie for movie in movies if movie[0] == "G" or movie[0] == 'g']
print(movies2)

# Tuple list
move = [("Star Wars", 2001), ("Groundhod Day", 2020), ("Good Will Hunting", 1980), ("Bad Santa", 1999)]
mo = [title for (title, year) in move if year > 2000 and title[0] == "G"]
print(mo)

abc = [(letter, num) for letter in 'abcde' for num in range(4)]
print(abc)


A = [1,3,5,7]
B = [2,4,6,8]
c = [(a, b) for a in A for b in B]
print(c)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# newlist = [int(num) for num in numbers if num > 0]
# print(newlist)

def new1():
    return [int(num) for num in numbers if num > 0]
print(new1())

new_list = [(letter,num) for letter in'spam' for num in range(4)]
print(new_list)