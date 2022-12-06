scores = {'A':1, 'B':2, 'C':3} # A for rock, B for paper, C for scissors
projected_outcome = {'X': 0, 'Y': 3, 'Z': 6} # X to loose, Y to draw, Z to win
wheel_of_fortune = ['A', 'B', 'C']

source = r'C:\Users\macie\OneDrive\Pulpit\Advent_of_Code\Day 2\source.txt'
score = 0
with open(source, 'r') as file:
    for line in file:
        score += projected_outcome[line[2]] # Outcome is predetermined by the encoding.
        
        op_move = line[0]
        op_move_i = wheel_of_fortune.index(line[0])


        # Now we must figure out the shape.
        if projected_outcome[line[2]] == 0: # If we have to loose
            move = wheel_of_fortune[op_move_i - 1] # We have to choose move on the right on the wheel of fortune.
            score += scores[move]
        
        elif projected_outcome[line[2]] == 3: # If we have to draw
            move = wheel_of_fortune[op_move_i] # We have to choose the same exact move.
            score += scores[move]
        
        else: # Otherwise we have to win.
            if op_move_i == 2: # To avoid indexing issues.
                move = wheel_of_fortune[0]
                score += scores[move]
            else:
                move = wheel_of_fortune[op_move_i + 1]
                score += scores[move]

print(score)