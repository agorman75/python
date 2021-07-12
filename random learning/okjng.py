import os

# list_of_files = ''

path = "C:\\Users\dijef279\\OneDrive - Dentsply Sirona\\Desktop\\VS code\\Python\\junk\\"
files = os.listdir(path)

def enter_file_name():
    list_of_files = input("Provide one or more ticket number")
    for i in list_of_files:
        print(i)

enter_file_name(files)