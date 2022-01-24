f = open('D:\python\LL_python\inputfile.txt', 'r')
passFile = open('D:\python\LL_python\PassFile.txt', 'w')

for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)

f.close()
passFile.close()