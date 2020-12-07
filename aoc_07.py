input = []

with open('aoc_07_input.txt') as fd:
    for line in fd:
        input.append(line.strip())

bigBag = []

for rule in input:
    tmp = rule.split(' bags contain ')
    if "shiny gold bag" in tmp[1]:
        bigBag.append(tmp[0])
l = 0
counter = 0
while len(bigBag) != l:
    counter += 1
    l = len(bigBag)
    for rule in input:
        tmp = rule.split(' bags contain ')
        for k in bigBag:
            if k in tmp[1] and tmp[0] not in bigBag: 
                bigBag.append(tmp[0])
    
print(counter)
print(len(bigBag))