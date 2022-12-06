import os

def carry_e(source):
    elfes = []
    with open(source, 'r') as file:
        kcal = 0
        for line in file:
            if line == '\n':
                elfes.append(kcal)
                kcal = 0
            else:
                kcal += int(line)
        elfes = sorted(elfes)
        return elfes[-3:]

source = os.path.join(r'C:\Users\macie\OneDrive\Pulpit\Advent_of_Code\Day 1\source.txt')
result = carry_e(source)
print(result) # Answer to the first question
print(sum(result)) # Answer to the second question



