input = []

with open('aoc_06_input.txt') as fd:
    for line in fd:
        input.append(line.strip())

iTotal = 0
answered = {}
iGrp = 0
for i in range(len(input)):
    
    if len(input[i]) > 0:
        iGrp += 1
        for c in input[i]:
            if c in answered:
                answered[c] += 1
            else:
                answered[c] = 1
        if i == (len(input)-1):
            for l in answered:
                if answered[l] == iGrp:
                    iTotal += 1
    else:
        for l in answered:
            if answered[l] == iGrp:
                iTotal += 1
        iGrp = 0
        answered = {}

print(iTotal)