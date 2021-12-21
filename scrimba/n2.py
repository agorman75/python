# name = input("What is your name? ").lower()
# if name == 'alice' or 'bob':
#     if name == 'alice':
#         print("Hello Alice!")
#     if name == 'bob':
#         print("Hello Bob!")
#     else:
#         print("You are not Alice or Bob.")

b = 0
n = int(input("Give me a number: "))
for i in range(n):
    if i % 3 == 0:
        print(i)
for i in range(n):
    b += i
    print(f"This does not mod 3: {b}")

# for i in range(1,n):
#     # if i % 5 or i % 3 == 0:
#     print()q