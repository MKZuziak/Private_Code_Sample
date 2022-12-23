import numpy as np
import copy

def open_file():
    with open(r'Advent_of_Code\2022\Day 8\source.txt', 'r') as file:
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
    
    print("There are {} visible trees in the forest.".format(visible_trees))

def scenic_score(ter_map):
    scenic_scores = dict()
    scenic_scores_list = list()
    for row_number, row in enumerate(ter_map):
        for column_number, tree in enumerate(row):
            trees_cor = (row_number, column_number)
            panorama = list() # Trees visible: Up, down, left, right
        
            # Looking up
            if row_number == 0:
                panorama.append(1)
            else:
                trees_visible = 0
                row_search = copy.deepcopy(row_number)
                while row_search > 0:
                    trees_visible += 1
                    next_tree = ter_map[(row_search-1), column_number]
                    if tree > next_tree:
                        row_search -= 1
                    else:
                        break
                panorama.append(trees_visible)
            #print("Tree: {}, up: {}".format(trees_cor, trees_visible))

            # Looking down
            if row_number == (len(ter_map) - 1):
                panorama.append(1)
            else:
                trees_visible = 0
                row_search = copy.deepcopy(row_number)
                while row_search < (len(ter_map) - 1):
                    trees_visible += 1
                    next_tree = ter_map[(row_search+1), column_number]
                    if tree > next_tree:
                        row_search += 1
                    else:
                        break
                panorama.append(trees_visible)
            #print("Tree: {}, down: {}".format(trees_cor, trees_visible))
            
            # Looking left
            if column_number == 0:
                panorama.append(1)
            else:
                trees_visible = 0
                column_search = copy.deepcopy(column_number)
                while column_search > 0:
                    trees_visible += 1
                    next_tree = ter_map[row_number, (column_search - 1)]
                    if tree > next_tree:
                        column_search -= 1
                    else:
                        break
                panorama.append(trees_visible)
            #print("Tree: {}, left: {}".format(trees_cor, trees_visible))

            # Looking right
            if column_number == (len(row) - 1):
                panorama.append(1)
            else:
                trees_visible = 0
                column_search = copy.deepcopy(column_number)
                while column_search < (len(row) - 1):
                    trees_visible += 1
                    next_tree = ter_map[row_number, (column_search + 1)]
                    if tree > next_tree:
                        column_search += 1
                    else:
                        break
                panorama.append(trees_visible)
            #print("Tree: {}, right: {}".format(trees_cor, trees_visible))
            #print("\n")

            scenic_score = 1
            for i in panorama:
                scenic_score = scenic_score * i
            scenic_scores[trees_cor] = scenic_score
            scenic_scores_list.append(scenic_score)

    for cors in scenic_scores:
        print("Tree located at {} is scoring {}".format(cors, scenic_scores[cors]))
    scenic_scores_list.sort()
    print(scenic_scores_list)













def other_code():
            # Looking up
            trees_visible = 0
            if row_number == 0:
                trees_visible = 1
            else: 
                for row_search in range(row_number):
                    next_tree = ter_map[row_search, column_number]
                    if tree > next_tree:
                        trees_visible += 1
                    elif (row_search + 1) == 1:
                        pass
                    else:
                        trees_visible += 1
                        break
            panorama.append(trees_visible)
            print("Tree: {}, up: {}".format(trees_cor, trees_visible))
            
            # Looking down
            trees_visible = 0
            if row_number == (len(ter_map) - 1):
                trees_visible = 1
            else:
                for row_search, next_tree in enumerate(ter_map[(row_number+1):, column_number]):
                    if tree > next_tree:
                        trees_visible += 1
                    else:
                        trees_visible += 1
                        break
            panorama.append(trees_visible)
            print("Tree: {}, down: {}".format(trees_cor, trees_visible))
            print("\n")


ter_map = open_file()
scan(ter_map=ter_map)    
scenic_score(ter_map=ter_map)     