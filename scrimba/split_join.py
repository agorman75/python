# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(msg.split())
# print(csv.split(','))
# print(str(friends_list))

# print(''.join(friends_list))

# print(''.join(msg.split()))
# print(msg.replace(' ', ''))

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

friends_list = csv

a = friends_list.replace(',', ' ')
b = a.replace(':', ' ')
c = b.replace(';', ' ')
l = []
l = c
print(l)