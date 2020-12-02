input = []

with open('aoc_02_input.txt') as fd:
    for line in fd:
        input.append(line.strip())

iLegalPWD = 0
for l in input:
    tmp = l.split(":")
    pwd = tmp[1].strip()
    tmp = tmp[0].split(" ")
    char = tmp[1]
    tmp = tmp[0].split("-")
    cmin = int(tmp[0])
    cmax = int(tmp[1])
    #print("pwd: {} char: {} min: {} max: {}".format(pwd,char,cmin,cmax))
    iCounter=0
    for c in pwd:
        if c == char:
            iCounter += 1

    if iCounter >= cmin and iCounter <= cmax:
        iLegalPWD += 1
    
print(iLegalPWD)