# friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
# hello = []
# print('John' and 'Terry' in friends not in hello)
# print(len(friends[::1]))
# print(friends.index('Eric'))

# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# print(friends)
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# friends.reverse()
# print(friends)

# print(min(friends))
# print(max(friends))
# print(min(cars))
# print(max(cars))
# print(sum(cars))

# friends.append('Terry G')
# friends.insert(1, 'Terry G')
# print(friends)
# friends[1] = 'Harry G'
# print(friends)
# friends.extend(cars)
# print(friends)
# friends.remove('Terry')
# print(friends)
# friends.pop()
# print(friends)
# friends.pop(0)
# print(friends)
# del friends[:4]
# print(friends)
# friends.clear()
# print(friends)

# new_friends = friends[:]
# new_friends = friends.copy()
# new_friends = list(friends)
# print(new_friends)



week1 = [1,2,3,4,5,6,7]
week2 = [8,9,10,11,12,13,14]
new_week = []
profit = 1.5

extra = input("add another day: ")
week2.append(int(extra))

new_week = week1 + week2
print(new_week)

worst_day = min(new_week) * 1.5
best_day = max(new_week) * 1.5

print(f"Worst day profit:$ {worst_day}")
print(f"Best day profit:$ {best_day}")
print((f"Combined profit:$ {worst_day + best_day}"))
