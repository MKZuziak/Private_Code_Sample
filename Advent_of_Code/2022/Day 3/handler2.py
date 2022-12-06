import string
chars = string.ascii_lowercase + string.ascii_uppercase
scores = {chars[i]: (i+1) for i in range(len(chars))}
source = r'C:\Users\macie\OneDrive\Pulpit\Advent_of_Code\Day 3\source.txt'
Grand_Score = 0
with open(source, 'r') as file:
    elf_counter = 0
    group_items = []
    for elf in file:
        elf_items = set(elf.strip('\n')) # Cuting out \n
        group_items.append(elf_items)
        elf_counter += 1
        if elf_counter == 3:
            intersection = group_items[0] & group_items[1] & group_items[2]
            for item in intersection:
                Grand_Score += scores[item]
            elf_counter = 0
            group_items = list()
print(Grand_Score)