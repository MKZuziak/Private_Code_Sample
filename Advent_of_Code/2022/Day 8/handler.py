import numpy as np
import copy
class Forest():
    def __init__(self, path, shape, verbose=0) -> None:
        self.tar_map = np.empty(shape)
        self.verbose = verbose
        with open(path, 'r') as file:
            for line in file:
                toarray = []
                for character in line:
                    if character != '\n':
                        toarray.append(character)
                array = np.asarray(toarray, np.intc)
                self.tar_map = np.vstack((self.tar_map, array))
            self.tar_map = np.delete(self.tar_map, 0, 0)
        if self.verbose == 1:
            print("Printing forest map of shape {}".format(self.tar_map.shape))
            print(self.tar_map)
    
    def scan(self):
        self.visible_trees = 0
        self.registered_positions = list()
        for row_pos, row in enumerate(self.tar_map):
            highest_tree_right = -1
            highest_tree_left = -1
            
            for col_pos, tree in enumerate(row):
                if tree > highest_tree_left and (row_pos, col_pos) not in self.registered_positions:
                    self.visible_trees += 1
                    highest_tree_left = tree
                    self.registered_positions.append((row_pos, col_pos))
                elif tree > highest_tree_left:
                    highest_tree_left = tree

            for col_pos, tree in enumerate(reversed(row)):
                reversed_position = len(row) - 1 - col_pos
                if tree > highest_tree_right and (row_pos, reversed_position) not in self.registered_positions:
                    self.visible_trees += 1
                    highest_tree_right = tree
                    self.registered_positions.append((row_pos, reversed_position))
                elif tree > highest_tree_right:
                    highest_tree_right = tree

        for column in range(self.tar_map.shape[1]):
            highest_tree_up = -1
            highest_tree_down = -1
            for row_pos, tree in enumerate(self.tar_map[:, column]):
                if tree > highest_tree_up and (row_pos, column) not in self.registered_positions:
                    self.visible_trees += 1
                    highest_tree_up = tree
                    self.registered_positions.append((row_pos, column))
                elif tree > highest_tree_up:
                    highest_tree_up = tree
            for row_pos, tree in enumerate(reversed(self.tar_map[:, column])):
                reversed_position = len(self.tar_map[:, column]) - row_pos - 1
                if tree > highest_tree_down and (reversed_position, column) not in self.registered_positions:
                    self.visible_trees += 1
                    highest_tree_down = tree
                    self.registered_positions.append((reversed_position, column))
                elif tree > highest_tree_down:
                    highest_tree_down = tree
    
        print("There are {} visible trees in the forest.".format(self.visible_trees))
        if self.verbose == 1:
            print("Printing visible tree positions")
            for position in self.registered_positions:
                print(position)

    def scenic_score(self):
        self.scenic_scores = dict()
        self.scenic_scores_list = list()
        for row_number, row in enumerate(self.tar_map):
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
                        next_tree = self.tar_map[(row_search-1), column_number]
                        if tree > next_tree:
                            row_search -= 1
                        else:
                            break
                    panorama.append(trees_visible)
                #print("Tree: {}, up: {}".format(trees_cor, trees_visible))

                # Looking down
                if row_number == (len(self.tar_map) - 1):
                    panorama.append(1)
                else:
                    trees_visible = 0
                    row_search = copy.deepcopy(row_number)
                    while row_search < (len(self.tar_map) - 1):
                        trees_visible += 1
                        next_tree = self.tar_map[(row_search+1), column_number]
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
                        next_tree = self.tar_map[row_number, (column_search - 1)]
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
                        next_tree = self.tar_map[row_number, (column_search + 1)]
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
                self.scenic_scores[trees_cor] = scenic_score
                self.scenic_scores_list.append(scenic_score)

        if self.verbose == 1:
            for cors in self.scenic_scores:
                print("Tree located at {} is scoring {}".format(cors, self.scenic_scores[cors]))
            self.scenic_scores_list.sort()
            print(self.scenic_scores_list)
        else:
            self.scenic_scores_list.sort()
            print("The highest scenic score is: {}".format(self.scenic_scores_list[-1]))

forest = Forest(path=r'Advent_of_Code\2022\Day 8\source.txt', shape=99, verbose=0)
forest.scan()
forest.scenic_score()