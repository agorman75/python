# strings are immutable - cannot change them. Need to save them in new variable or override the existing variable

# msg='Welcome to Python 101: Strings'
# print(msg.find('Python'))
# print(msg.replace('Python','Java'))
# print("Python" in msg)
# print("Python" not in msg)


name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color + '!'
msg1 = f'[{name.title()}] loves the color {color.lower()}!'
print(msg)
print(msg1)