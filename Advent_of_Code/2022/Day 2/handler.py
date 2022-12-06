scores = {'A':1, 'B':2, 'C':3, 'Lost': 0, 'Draw': 3, 'Win':6} # A for rock, B for paper, C for scissors
encoding = {'X': 'A', 'Y': 'B', 'Z': 'C'}
wheel_of_fortune = ['A', 'B', 'C']

source = r'C:\Users\macie\OneDrive\Pulpit\Advent_of_Code\Day 2\source.txt'
score = 0
with open(source, 'r') as file:
    for line in file:
        my_move = encoding[line[2]]
        my_move_i = wheel_of_fortune.index(encoding[line[2]])
        score += scores[my_move] # The points for a type of move are not dependant on the outcome.
        
        op_move = line[0]
        op_move_i = wheel_of_fortune.index(line[0])

        if my_move_i == op_move_i:
            score += scores['Draw']
        elif wheel_of_fortune[my_move_i - 1] == op_move:
            score += scores['Win']
        else:
            print('JANKEN JAANKEEN')


print(score)