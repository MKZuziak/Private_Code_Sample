import regex as re
import os
Superset_Score = 0
Intersection_Score = 0
finder = re.compile(r'\d+')
path = r'Day 4\source.txt'
with open(path, 'r') as file:
    for line in file:
        ranges = finder.findall(line)
        *elf1, = range(int(ranges[0]), (int(ranges[1] ) + 1))
        *elf2, = range(int(ranges[2]), (int(ranges[3] ) + 1))
        elf1_set = set(elf1)
        elf2_set = set(elf2)
        
        if elf1_set.issuperset(elf2_set):
            Superset_Score += 1
        elif elf2_set.issuperset(elf1_set):
            Superset_Score += 1
        
        if elf1_set.isdisjoint(elf2_set):
            Intersection_Score += 1
Intersection_Score = 1000 - Intersection_Score
print(Superset_Score)
print(Intersection_Score)