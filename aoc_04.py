import re

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
    if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
        bValid = True
        for field in passport:
            if bValid:
                if field == "byr":
                    bValid = (int(passport[field]) >= 1920 and int(passport[field]) <= 2002)
                elif field == "iyr":
                    bValid = (int(passport[field]) >= 2010 and int(passport[field]) <= 2020)
                elif field == "eyr":
                    bValid = (int(passport[field]) >= 2020 and int(passport[field]) <= 2030)
                elif field == "hgt":
                    tmp = passport[field]
                    if tmp[-2:] == "cm":
                        bValid = (len(tmp) == 5 and int(tmp[:3]) >= 150 and int(tmp[:3]) <= 193)
                    elif tmp[-2:] == "in":
                        bValid = (len(tmp) == 4 and int(tmp[:2]) >= 59 and int(tmp[:2]) <= 76)
                elif field == "hcl":
                    if not re.search("#[0-9a-f]{6}",passport[field]):
                        bValid = False
                elif field == "ecl":
                    bValid = (passport[field] in ["amb","blu","brn","gry","grn","hzl","oth"])
                elif field == "pid":
                    if not re.search("\d{9}",passport[field]):
                        bValid = False
                else:
                    pass
                    #print(passport[field])
        if bValid:
            if re.search("#[0-9a-f]{6}",passport["hcl"]):
                print(False)
            iCounter += 1


print(iCounter)