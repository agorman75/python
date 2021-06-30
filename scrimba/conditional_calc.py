print("what would you like to do?")
selection = input(("Select your operator: +, -, /, *, ?"))



if selection == "+":
    add1 = float(input("What would you like to add: "))
    add2 = float(input("and: "))
    print(add1 + add2)
elif selection == "-":
    sub1 = float(input("What would you like to subtract: "))
    sub2 = float(input("and: "))
    print(sub1 - sub2)
elif selection == "/":
    div1 = float(input("What would you like to divide: "))
    div2 = float(input("and: "))
    print(div1 / div2)
elif selection == "*":
    mul1 = float(input("What would you like to multiply: "))
    mul2 = float(input("and: "))
    print(mul1 * mul2)
elif selection == "?":
    cel1 = float(input("Convert C to F: "))
    temp = cel1 * 9 / 5 + 32
    print(temp)