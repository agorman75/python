# def double_char(str):
#     result = ''
#     for char in str:
#         result += char * 2
#         print(result)


# print(double_char('The'))# → 'TThhee'
# print(double_char('AAbb'))# → 'AAAAbbbb'
# print(double_char('Hi-There'))# → 'HHii--TThheerree'

# def cat_dog(str):
#     if str.count("cat") == str.count("dog"):
#         return True
#     return False

# print(cat_dog('catdog'))# → True
# print(cat_dog('catcat'))# → False
# print(cat_dog('1cat1cadodog'))# → True

def count_code(str):
    c = ''
    for x in 'abcdefghijklmnopqrstuvwxyz':
        c += x
        return "co" + c + "e"

print(count_code('cozexxcope'))#