
    # 1. Firstly we must create a grid in order to employ dynamic programming in this problem.
    # In backpack problem, grid will be consist of items (rows) and different backpacks maximal capacities.
    # Number of rows will correspond to the number of items that we can select.
    # Number of columns will depend on the weight of the smallest item and the bagpack maximal capacity.
    # Grid will be a pyth

class backpack_solver():
    def __init__(self, weights: dict, capacity: int | float) -> None:
        # 1. Firstly we must create a grid in order to employ dynamic programming in this problem.
        # In backpack problem, grid will be consist of items (rows) and different backpacks maximal capacities.
        # Number of rows will correspond to the number of items that we can select.
        # Number of columns will depend on the weight of the smallest item and the bagpack maximal capacity.
        # Grid will be a python lists of lists. Please note, that in real implementaiton you will likely
        # want to use a special library for linear algebra, as it already implements popular data structures
        # such as matrices (and optimise the operations on them). However, for an educational purposes
        # we can use a list of list that can be created using list comprehension.
        
        self.smallest_weight = min(min(weights[key] for key in weights))
        columns = int(capacity / self.smallest_weight) #conversion to int will truncate towards 0 -> we can not exceed the bagpack's capacity!
        self.weights = weights
        self.capacity = capacity
        self.grid = [[0] * columns for _ in range(len(weights))]

    def solve_problem(self):
        # 2. After defining the final grid layout, we can start solving our problem!
        # In fact, we have all the necessary information already in place,
        # now we can just apply the the dynamic programming to populate the grid.

        for row, item in enumerate(self.weights):
            for column in range(len(self.grid[0])):

                # First, we want to check if the item will fit in the backpack: 
                if self.weights[item][1] <= (column + 1) * self.smallest_weight:
                    
                    # If it fits, then we check if there is a row above:
                    if (row - 1) >= 0:
                        weight_left = (column + 1) - int((self.weights[item][1] / self.smallest_weight))
                        # If there is a still room left in the backpack:
                        if weight_left >= 1:
                            # Then we compare a choice above with the choice of the current item + free space left:
                            better_option = max(self.grid[row - 1][column], \
                                self.weights[item][0] + self.grid[row - 1][weight_left - 1])
                            # We assign the better option:
                            self.grid[row][column] = better_option
                        # If there is no room left in the backpack:
                        else:
                            # Then we must choose between this item and the item directly above.
                            better_option = max(self.grid[row - 1][column], self.weights[item][0])
                            self.grid[row][column] = better_option
                    # If it fits but there is no row above
                    else:
                        # Then the only choice is to select the item.
                        self.grid[row][column] = self.weights[item][0]
                # If the item does not fit into the bagpack
                else:
                    # We check whether there is a row above
                    if (row - 1) >= 0:
                        # If there is a row above, we assign use that value
                        self.grid[row][column] = self.grid[row-1][column]
                    else:
                        # Otherwise, the value will be equal to 0.
                        self.grid[row][column] = 0

        print(self.grid)
    
if __name__ == '__main__':
    # First problem:
    w = {'stereo':(3000, 4),
        'laptop': (2000, 3),
        'guitar': (1500, 1)
        }

    w2 = {
        'guitar': (1500, 1),
        'laptop': (2000, 3),
        'stereo': (3000, 4)
    }

    w3 = {
        'guitar': (1500, 1),
        'stereo': (3000, 4),
        'laptop': (2000, 3),
    }

    b = backpack_solver(weights=w3, capacity=4)
    b.solve_problem()

    # Second problem
    w1 = {
        "OW": (7, 0.5),
        "GT": (6, 0.5),
        "NG": (9, 1),
        "MB": (9, 2),
        "KP": (8, 0.5)
    }

    b = backpack_solver(weights=w1, capacity=2)
    b.solve_problem()

    # Third problem

    w1 = {
        "W": (10, 3),
        "B": (3, 1),
        "F": (3, 2),
        "K": (5, 2),
        "A": (6, 1)
    }

    b = backpack_solver(weights=w1, capacity=6)
    b.solve_problem()