names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
names.extend(names1)
# names += names1
count = 1

while count < 3:
    count += 1
    names.append(input("Add two names list: "))
for x in names:
    print(f"{x.capitalize()} ! You are invited to the party on Saturday.") 


# # The same as the above
# msg = 'You are invited to the party on saturday.'
# #names.extend(names1)
# names += names1
# for index in range(2):
#     names.append(input('Enter a new name: '))

# for name in names:
#     #msg1 = f'{name.title()}! {msg}'
#     msg1 = name.title() + '! ' + msg
#     print(msg1)