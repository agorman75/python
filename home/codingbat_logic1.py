# def cigar_party(cigars, is_weekend):
#     if is_weekend == True and cigars > 40:
#         return True
#     if cigars in range(40,61):
#         return True
#     return False

# print(cigar_party(30, False))# → False
# print(cigar_party(50, False))# → True
# print(cigar_party(70, True))# True
# print(cigar_party(39, False))# False
# print(cigar_party(39, True))# False

# def date_fashion(you, date):
#     if you <= 2 or date <= 2:
#         return 0
#     if date >= 8 or you >= 8:
#         return 2
#     return 1
#     # elif you and date 

# print(date_fashion(5, 10))# → 2
# print(date_fashion(5, 2))# → 0
# print(date_fashion(5, 5))# → 1
# print(date_fashion(10, 5))# → 2


# def squirrel_play(temp, is_summer):
#     if is_summer == True and temp in range(90,101):
#         return True
#     if temp in range(60,91):
#         return True
#     return False

# print(squirrel_play(70, False))# → True
# print(squirrel_play(95, False))# → False
# print(squirrel_play(95, True))# → True

# def alarm_clock(day, vacation):
#     if day == 0 and vacation == False:
#         return '10:00'
#     if day == 6 and vacation == False:
#         return '10:00'
#     if day == 0 and vacation == True:
#         return 'off'
#     if day == 6 and vacation == True:
#         return 'off'
#     if day in range(1,6) and vacation == True:
#         return '10:00'
#     if day in range(1,6) and vacation == False:
#         return '7:00'

# print(alarm_clock(1, False))# → '7:00'
# print(alarm_clock(5, False))# → '7:00'
# print(alarm_clock(0, False))# → '10:00'
# print(alarm_clock(0, True))# off


# def love6(a, b):
#     if a == 6 or b == 6 or a + b == 6 or a - b == 6 or b - a == 6:
#         return True
#     return False

# print(love6(6, 4))# → True
# print(love6(4, 5))# → False
# print(love6(1, 5))# → True

# def in1to10(n, outside_mode):
#     if n == 9 and outside_mode == True:
#         return False
#     if n in range(1,11) or outside_mode == True:
#         return True
#     return False    

# print(in1to10(5, False))# → True
# print(in1to10(11, False))# → False
# print(in1to10(11, True))# → True


def near_ten(num):
    return num % 10



print(near_ten(12))# → True
print(near_ten(17))# → False
print(near_ten(19))# → True
print(near_ten(158))# → True
print(near_ten(8))# → True