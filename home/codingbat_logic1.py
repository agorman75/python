def cigar_party(cigars, is_weekend):
    if is_weekend == True and cigars > 40:
        return True
    if cigars in range(40,61):
        return True
    return False


print(cigar_party(30, False))# → False
print(cigar_party(50, False))# → True
print(cigar_party(70, True))# True
print(cigar_party(39, False))# False
print(cigar_party(39, True))# False