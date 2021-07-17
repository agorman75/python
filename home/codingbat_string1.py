# def hello_name(name):
#     return "Hello " + name.title() + "!"

# print(hello_name('ho ho ho'))


# def make_tags(tag, word):
#     return "'<"+ tag + ">" + word + "</" + tag +">'"

# print(make_tags('i', 'Yay'))

# def make_out_word(out, word):
#     return out[:2] + word + out[2:]

# print(make_out_word('HHoo', 'Hello'))

# def extra_end(str):
#     if len(str) == 2:
#        return str * 3
#     if len(str) >= 3:
#         return str[-2:] * 3

# print(extra_end('code'))

# def first_two(str):
#     return str[:2]

# print(first_two('Hello'))

# def first_half(str):
#   a = len(str) / 2
#   return str[:a]

# first_half('WooHoo') 

# def without_end(str):
#   n = len(str)
#   return str[1:n - 1]

# without_end('Hello')


# def combo_string(a, b):
#     if len(a) > len(b):
#         return b + a + b
#     return a + b + a
    
# print(combo_string('Hello', 'hi'))# → 'hiHellohi'
# print(combo_string('hi', 'Hello'))# → 'hiHellohi'

# def non_start(a, b):
#     return a[1:] + b[1:]

# print(non_start('Hello', 'There'))# → 'ellohere'
# print(non_start('java', 'code'))# → 'avaode'
# print(non_start('shotl', 'java'))# → 'hotlava'

def left2(str):
    return str[2:] + str[:2]


print(left2('Hello'))# → 'lloHe'
print(left2('java'))# → 'vaja'
print(left2('Hi'))# → 'Hi'
print(left2('12345'))
print(left2('bricks'))
print(left2('Chocolate'))