input = []

with open('aoc_03_input.txt') as fd:
    for line in fd:
        input.append(line.strip())
#iRight,iColumn,
slopes = {"a":[1,0,0,1,1],"b":[3,0,0,1,1],"c":[5,0,0,1,1],"d":[7,0,0,1,1],"d":[7,0,0,1,1],"e":[1,0,0,2,2]}
iColumn = 0
bFirst = True
iRow = 0
for row in input:
    for slope in slopes:
        var = slopes[slope]
        #print("iRow: {} slope: {} nRow: {}".format(iRow,slope,var[3]))
        if var[3] == iRow:
            iRight = var[0]
            iColumn = var[1]
            iTreeCount = var[2]
            iColumn += iRight
            if iColumn >= len(row):
                iColumn = iColumn - len(row)
            if row[iColumn] == "#":
                iTreeCount += 1
            var[1] = iColumn
            var[2] = iTreeCount
            var[3] = iRow + var[4]
            #print(var)
            slopes[slope] = var
        else:
            pass
    iRow += 1
iScore = 1
for slope in slopes:
    print("slope: {} Tree: {}".format(slope, slopes[slope][2]))
    iScore *= slopes[slope][2]
print(iScore)
