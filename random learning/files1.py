# Import os module to read directory
import os, sys

# Set the directory path
path = input("Provide path. \n")

# Read the content of the file
files = os.listdir(path)

# Print the content of the directory
def dirz():
    for file in files:
        if file.endswith(".txt"):
            new_folder = input("Name of new folder\n")
            new1 = path + "\\" + new_folder
            os.mkdir(new1)
            print(f"{new1}")

def dirz1():
    for file in files:
        if file.endswith(".zip"):
            ask = input("Do you want to continue?")
            if ask[0] != 'n':
                print("You continued")
            else:
                print("Time to exit")
                sys.exit()

dirz()
dirz1()