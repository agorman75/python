f = open('D:\python\LL_python\inputfile.txt', 'r')

count = 0

for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)

f.close()