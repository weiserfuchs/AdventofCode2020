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
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        bValid = True
        for field in passport:
            if bValid:
                if field == "byr":
                    if not (int(passport[field]) >= 1920 and int(passport[field]) <= 2002):
                        bValid = False
                elif field == "iyr":
                    if not (int(passport[field]) >= 2010 and int(passport[field]) <= 2020):
                        bValid = False
                elif field == "eyr":
                    if not (int(passport[field]) >= 2020 and int(passport[field]) <= 2030):
                        bValid = False
                elif field == "hgt":
                    tmp = passport[field]
                    if tmp[-2:] == "cm":
                        if not (len(tmp) == 5 and int(tmp[:3]) >= 150 and int(tmp[:3]) <= 193):
                            bValid = False
                    elif tmp[-2:] == "in":
                        if not (len(tmp) == 4 and int(tmp[:2]) >= 59 and int(tmp[:2]) <= 76):
                            bValid = False
                    else:
                        bValid = False
                elif field == "hcl":
                    if not re.search("#[0-9a-f]{6}",passport[field]):
                        bValid = False
                elif field == "ecl":
                    if not (passport[field] in ["amb","blu","brn","gry","grn","hzl","oth"]):
                        bValid = False
                elif field == "pid":
                    if not re.search("^\d{9}$",passport[field]):
                        bValid = False
                else:
                    pass
        if bValid:
            iCounter += 1


print(iCounter)