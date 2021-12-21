# def string_bits(str):
#     for i in len


# print(string_bits('Hello'))# → 'Hlo'
# print(string_bits('Hi'))# → 'H'
# print(string_bits('Heeololeo'))# → 'Hello'

def string_bits(str):
    result = ''
    for i in range(0,len(str),2):
        result += str[i]
    return result

print(string_bits('Hello'))# → 'Hlo'
print(string_bits('Hi'))# → 'H'
print(string_bits('Heeololeo'))# → 'Hello'