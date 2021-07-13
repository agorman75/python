# a = lambda x: (x*100) + 1
# print(a(1))

# num = lambda x: (x + 15)
# print(num(10))

# num1 = lambda y, z: y * z
# print(num1(10, 10))

def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Double the number of 15 =", result(15))
result = func_compute(3)
print("Triple the number of 15 =", result(15))
result = func_compute(4)
print("Quadruple the number of 15 =", result(15))
result = func_compute(5)
print("Quintuple the number 15 =", result(15))