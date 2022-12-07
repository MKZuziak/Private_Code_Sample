source = r'Advent_of_Code\2022\Day 5\source.txt'

stockpile = {i: [] for i in range(1, 10)}
with open(source) as file:
    for line in file:
            i = 1
            for z in range(1, len(line), 4):
                stockpile[i].append(line[z])
                i += 1

print(stockpile)
        
    