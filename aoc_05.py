input = []

with open('aoc_05_input.txt') as fd:
    for line in fd:
        input.append(line.strip())
    
row = []
for k in range(128):
    row.append(k)
col = []
for k in range(8):
    col.append(k)

iTmp = 0
highestSeatID = 0
IDs = []
for boarding in input:
    tmpCol = []
    tmpRow = []
    for part in boarding:
        if part in ["B","F"]:
            if part == "B":
                if len(tmpRow) == 0:
                    iTmp = int((len(row)/2) * -1)
                    tmpRow = row[iTmp:]
                else:
                    iTmp = int((len(tmpRow)/2) * -1)
                    tmpRow = tmpRow[iTmp:]
            if part == "F":
                if len(tmpRow) == 0:
                    iTmp = int((len(row)/2))
                    tmpRow = row[:iTmp]
                else:
                    iTmp = int((len(tmpRow)/2))
                    tmpRow = tmpRow[:iTmp]
        elif part in ["L","R"]:
            if part == "L":
                if len(tmpCol) == 0:
                    iTmp = int((len(col)/2))
                    tmpCol = col[:iTmp]
                else:
                    iTmp = int((len(tmpCol)/2))
                    tmpCol = tmpCol[:iTmp]
            if part == "R":
                if len(tmpCol) == 0:
                    iTmp = int((len(col)/2) * -1)
                    tmpCol = col[iTmp:]
                else:
                    iTmp = int((len(tmpCol)/2) * -1)
                    tmpCol = tmpCol[iTmp:]
    seatID = int(tmpRow[0]) * 8 + int(tmpCol[0])
    IDs.append(seatID)

for id in IDs:
    if (not (id+1) in IDs and (id+2) in IDs) or ((id-1) not in IDs and (id-2) in IDs):
        print(id)