#key cannot be duplicated in a dictionary, but values can
python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print("He's not here!") #He\'s not here! < --- escape character

#Method 1: update
people = {}
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(people.items())

#Method 2: comprehension
people1 = {}
for groups in (python, holy_grail, life_of_brian) : people1.update(groups)
print(people1.items())

#Method 3: unpacking. Only works in 3.5 or later
people2 = {}
people2 = {**python, **holy_grail, **life_of_brian}
print(people2.items())
print(sorted(people2.items())) #if dictionaries becomes mixed, use the sorted() function among all to make print outs similar
