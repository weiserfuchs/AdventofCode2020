
year = 2020
input = []
diff = 0

with open('aoc_01_input.txt') as fd:
    for line in fd:
        input.append(int(line))

for i in range(len(input)):
    if diff == 0:
        diff = year - input[i]
        used = [input[i]]
    else:
        diff -= input[i]
        used = 
        if diff in input:
            print("a: {} b: {} c: {} ergebnis: {}".format(input[i],input[j],input[k],(input[i]*input[j]*input[k])))
                    break
