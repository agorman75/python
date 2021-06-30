a = [3,7,42]
b = [3,7,42]
print(id(a), id(b))
a = b
print(a == b)
print(a is b)
print(id(a), id(b))

