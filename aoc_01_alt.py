
year = 2020
input = []
icounter = 0

with open('aoc_01_input.txt') as fd:
    for line in fd:
        input.append(int(line))

for i in range(len(input)):
    for j in range(len(input)):
        icounter += 1
        diff = year - (input[i] + input[j])
        if diff > 0:
            if diff in input:
                print("a: {} b: {} c: {} ergebnis: {}".format(input[i],input[j],diff,(input[i]*input[j]*diff)))
                break
    else:
        continue
    break
            

print(icounter)