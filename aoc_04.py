input = []
tmpDict =  {}

with open('aoc_04_input.txt') as fd:
    for line in fd:
        if len(line.strip()) > 0:
            for field in line.strip().split(" "):
                keyVal = field.split(":")
                tmpDict[keyVal[0]] = keyVal[1]
        else:
            input.append(tmpDict)
            tmpDict =  {}
    if len(tmpDict) > 0:
        input.append(tmpDict)

iCounter = 0
for passport in input:
    if len(passport) == 8:
        iCounter += 1
    elif len(passport) == 7 and "cid" not in passport:
        iCounter += 1

print(iCounter)