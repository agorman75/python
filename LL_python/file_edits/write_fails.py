f = open('D:\python\LL_python\inputfile.txt', 'r')
failFile = open('D:\python\LL_python\\failFile.txt', 'w')
passFile = open('D:\python\LL_python\passFile.txt', 'w')

for line in f:
    line_split = line.split()
    if line_split[-1] == "F":
        failFile.write(line)
    else:
        passFile.write(line)

f.close()
passFile.close()
failFile.close()

