import numpy as np

def open_file():
    with open(r'source.txt', 'r') as file:
        ter_map = np.empty((99))
        for line in file:
            toarray = []
            for character in line:
                if character != '\n':
                    toarray.append(character)
            array = np.asarray(toarray, np.intc)
            ter_map = np.vstack((ter_map, array))
        ter_map = np.delete(ter_map, 0, 0)
        return ter_map

def scan(ter_map):
    visible_trees = 0
    registered_positions = list()
    for row_pos, row in enumerate(ter_map):
        highest_tree_right = -1
        highest_tree_left = -1
        
        for col_pos, tree in enumerate(row):
            if tree > highest_tree_left and (row_pos, col_pos) not in registered_positions:
                visible_trees += 1
                highest_tree_left = tree
                registered_positions.append((row_pos, col_pos))
            elif tree > highest_tree_left:
                highest_tree_left = tree

        for col_pos, tree in enumerate(reversed(row)):
            reversed_position = len(row) - 1 - col_pos
            if tree > highest_tree_right and (row_pos, reversed_position) not in registered_positions:
                visible_trees += 1
                highest_tree_right = tree
                registered_positions.append((row_pos, reversed_position))
            elif tree > highest_tree_right:
                highest_tree_right = tree

    
    
    for column in range(ter_map.shape[1]):
        highest_tree_up = -1
        highest_tree_down = -1

        for row_pos, tree in enumerate(ter_map[:, column]):
            if tree > highest_tree_up and (row_pos, column) not in registered_positions:
                visible_trees += 1
                highest_tree_up = tree
                registered_positions.append((row_pos, column))
            elif tree > highest_tree_up:
                highest_tree_up = tree

        for row_pos, tree in enumerate(reversed(ter_map[:, column])):
            reversed_position = len(ter_map[:, column]) - row_pos - 1
            if tree > highest_tree_down and (reversed_position, column) not in registered_positions:
                visible_trees += 1
                highest_tree_down = tree
                registered_positions.append((reversed_position, column))
            elif tree > highest_tree_down:
                highest_tree_down = tree

    print(visible_trees)
ter_map = open_file()
scan(ter_map=ter_map)         