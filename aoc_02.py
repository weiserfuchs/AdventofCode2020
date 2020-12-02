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
    cfir = int(tmp[0])-1
    csec = int(tmp[1])-1

    if bool(pwd[cfir] == char) != bool(pwd[csec] == char):
        iLegalPWD += 1
    
print(iLegalPWD)