from hashlib import algorithms_guaranteed, new
import random, string

for i in range(5):
    print(random.random()*6)
    print(random.uniform(1,6))
    print(random.randint(1,6))
    print(random.randrange(1,6))

friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']

print(random.choice(friends_list))
print(random.sample(friends_list, 2))

random.shuffle(friends_list)
print(friends_list)


smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits
word = ''
for i in range(7):
    word += random.choice(letters_numbers)
word1 = ''.join(random.sample(letters_numbers,7))
word = random.choices(letters_numbers, k=7)
print(word)
print(word1)

new_l1 =  random.choice(smallcaps)
new_l2 = random.choice(largecaps)
new_l3 = random.choice(digits)
new10 = new_l1 + new_l2 + new_l3
print(new10, "this is new")

a = ''
for i in smallcaps, largecaps, digits:
    a += i
    b = ''.join(random.choices(a,k=len(a)))

print(b)