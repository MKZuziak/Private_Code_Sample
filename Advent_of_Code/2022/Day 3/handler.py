import string
chars = string.ascii_lowercase + string.ascii_uppercase
scores = {chars[i]: (i+1) for i in range(len(chars))}
print(scores)

source = r'C:\Users\macie\OneDrive\Pulpit\Advent_of_Code\Day 3\source.txt'

Grand_Score = 0
with open(source, 'r') as file:
    for line in file:
        content = line.strip('\n') # Cuting out \n
        delimiter = int(len(content)/2)
        first_half = content[:delimiter]
        second_half = content[delimiter:]
        #print(len(first_half), '==', len(second_half), 'from', len(content))
        intersection = []
        for char in first_half:
            for char_b in second_half:
                if char == char_b:
                    intersection.append(char)
        intersection = set(intersection)
        for element in intersection:
            Grand_Score += scores[element]


print(Grand_Score)