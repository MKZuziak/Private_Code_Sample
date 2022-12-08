source = r'Advent_of_Code\2022\Day 5\stockpile.txt'
import regex as re

pattern = re.compile(r'\d+')

def load_stockpile(source):
    stockpile = {i: [] for i in range(1, 10)}
    with open(source) as file:
        for line in file:
            i = 1
            for z in range(1, len(line), 4):
                stockpile[i].append(line[z])
                i += 1
    for z in range(len(stockpile)):
        stockpile[(z + 1)].reverse()
        while True:
            try:
                stockpile[(z + 1)].remove(' ')
            except:
                break
    return stockpile

def carry_instructions(stockpile, source):
    with open(source, 'r') as file:
        for line in file:
            instructions = pattern.findall(line)
            number_of_crates = int(instructions[0])
            source = int(instructions[1])
            destination = int(instructions[2])
            bottom = len(stockpile[source]) - number_of_crates
            for i in range(bottom, len(stockpile[source])):
                stockpile[destination].append(stockpile[source][i])
            del stockpile[source][bottom:]

        

stock = load_stockpile(source)
carry_instructions(stockpile=stock, source=r'Advent_of_Code\2022\Day 5\source.txt')
for l in stock:
    print(stock[l][-1], end='')