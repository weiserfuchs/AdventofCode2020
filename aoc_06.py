input = []

with open('aoc_06_input.txt') as fd:
    for line in fd:
        input.append(line.strip())

iTotal = 0
answered = []
for k in input:
    
    if len(k) > 0:
        for c in k:
            if c not in answered:
                answered.append(c)

    else:
        iTotal += len(answered)
        answered = []
iTotal += len(answered)

print(iTotal)