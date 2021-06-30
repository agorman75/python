# import os, sys
# # help(os)
# b = ()
# a = os.listdir()
# for files in a:
#     b = files
#     print(b)

passwordfile = open('secretpasswordfile.txt')
secretpassword = passwordfile.read()
print("Enter password.")
typedpassword = input()
if typedpassword == secretpassword:
    print("access granted")
    if typedpassword == '12345':
        print("that password is one")
else:
    print("denied")