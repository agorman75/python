def number_compare(a, b):
    if a == b:
        return "Numbers are equal"
    elif a > b:
        return "First is greater"
    return "Second is greater"

print(number_compare(a = input("A: "), b = input("B: ")))