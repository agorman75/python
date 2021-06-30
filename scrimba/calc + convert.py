import sys

mode2 = input("Would you like to conert to C to F? ").lower()
if mode2[0] == "y":
    cel1 = float(input("Convert C to F: "))
    temp = (cel1 * 9 / 5) + 32
    print(temp)
    sys.exit()

print("Do your math:")
m1 = int(input())
mode = input()
m2 = int(input())

if mode == "+":
    print(f"{m1} + {m2} = {m1 + m2}")
elif mode == "-":
    print(f"{m1} - {m2} = {m1 - m2}")
elif mode == "*":
    print(f"{m1} x {m2} = {m1 * m2}")
elif mode == "/":
    print(f"{m1} / {m2} = {m1 / m2}")
else:
    print("Input error!")