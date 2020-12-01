year = 2020
input = []

with open('aoc_01_input.txt') as fd:
    for line in fd:
        input.append(int(line))

for i in range(len(input)):
    for j in range(len(input)):
        for k in range(len(input)):
            if i != j and i != k and j != k:
                if (input[i] + input[j] + input[k])==year:
                    print("a: {} b: {} c: {} ergebnis: {}".format(input[i],input[j],input[k],(input[i]*input[j]*input[k])))

