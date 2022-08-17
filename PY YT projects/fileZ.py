import os

# with open(r'D:\python\PY YT projects\test_stuff\test.txt','r') as o_file:
#     for each in o_file:
#         print(each)

folder = os.listdir('.')

# print("Curent directory:", os.getcwd(), "\nList of files: \n", str(folder))

print("")
print("Here are the retireved files:")

for file in folder:
    if file.endswith(".txt"):
        print("Reference file: ", file)
        with open(file, 'r')as file_2:
            new1 = file_2.readlines()
            count = 0
            while count <= len(new1):
                count += 1
                # new2 = str(count) + (".").join(new1)
                # new3 = list(new2)
                he1 = list(enumerate(new1))
                he2 = (".").join(he1)
                print(he1)