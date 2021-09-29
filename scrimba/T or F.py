a = [3,7,42]
b = [3,7,42]
print(id(a), id(b))
a = b
print(a == b)
print(a is b)
print(id(a), id(b))

# False = 0. True = 1 or higher
# a = 5
# print(a + True) = 6
# print(a + False) = 4
# ' ' = True. '' = False
# 