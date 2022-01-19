import itertools
import random
import copy


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # Because we are eliminating safe cells from the the statement, we are looking for statements
        # that would contain number of cells that is equal (or smaller) than number of mines.
        # Upon fulfilment of such condition, evaluated cells are known to be mines.
        if len(self.cells) <= self.count:
            return self.cells
        else:
            return None

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # There is only one case when the cells are known to be "safes" - when the number of count is 0.
        if self.count == 0:
            return self.cells
        else:
            return None

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # Marking mine implies two logical consequences:
        # a) the number of counts must decrease by one (n - 1);
        # b) the cell marked as mine must be discarded from the sentence (we keep track,
        # only of the cells that are still unknown to be mines or "safes".

        if cell in self.cells:
            self.cells.discard(cell)
            self.count -= 1
            if self.count < 0:  # this is a safeguard from any improper inference set forth.
                self.count = 0
        else:
            pass

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # Marking "safe" implies one logical consequence:
        # a) the cell marked as safe must be discarded from the sentence.
        if cell in self.cells:
            self.cells.discard(cell)
        else:
            pass


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # 1) mark the cell as a move that has been made.
        self.moves_made.add(cell)

        # 2) mark the cell as safe. By this we are also updating our internal knowledge base.
        self.mark_safe(cell)

        # 3) add a new sentence to the AI's knowledge base based on the value of `cell` and `count`
        sentence_prep = set()

        # Sentence must include all the adjacent tiles, but do not include:
        # a) the revealed cell itself;
        # b) the cells that are known to be mines;
        # c) the cell that are known to be safe.
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):  # Those two cover all the adjacent tiles.
                if (i, j) != cell:
                    if (i, j) not in self.moves_made and (i, j) not in self.mines and (i, j) not in self.safes:
                        if 0 <= i < self.height and 0 <= j < self.width:  # The cell must be within the game frame.
                            sentence_prep.add((i, j))
                    elif (i, j) in self.mines:
                        count -= 1

        new_knowledge = Sentence(sentence_prep, count)  # Adding newly formed knowledge to the KB.
        self.knowledge.append(new_knowledge)

        # 4) mark any additional cells as safe or as mines,
        #   if it can be concluded based on the AI's knowledge base
        # 5) add any new sentences to the AI's knowledge base
        #    if they can be inferred from existing knowledge.

        while True:  # iterating knowledge base in search for new conclusions on safes or mines.
            amended = False  # flag indicates that we have made changes to the knowledge, new run required.
            knowledge_copy = copy.deepcopy(self.knowledge)  # creating copy of the database.
            for sentence in knowledge_copy:  # cleaning empty sets from the database.
                if len(sentence.cells) == 0:
                    self.knowledge.remove(sentence)

            knowledge_copy = copy.deepcopy(self.knowledge)  # creating copy once again, without empty sets().
            for sentence in knowledge_copy:
                mines_check = sentence.known_mines()  # this should return: a set of mines that are known mines or None.
                safes_check = sentence.known_safes()  # this should return: a set of safes that are known safes or None
                if mines_check is not None:
                    for cell in mines_check:
                        self.mark_mine(cell)  # marking cell as a mine, and updating internal knowledge.
                        amended = True  # raising flag.
                if safes_check is not None:
                    for cell in safes_check:
                        self.mark_safe(cell)  # marking cell as a safe, and updating internal knowledge.
                        amended = True  # raising flag.

            # the algorithm should infer new knowledge,
            # basing on reasoning: (A.cells - B.cells) = (A.count - B.count), if
            # B is the subset of A.
            knowledge_copy = copy.deepcopy(self.knowledge)  # creating copy once again, updated checks.
            for sentence_one in knowledge_copy:
                for sentence_two in knowledge_copy:
                    if len(sentence_one.cells) != 0 and len(sentence_two.cells) != 0:  # In case of the empty set
                        if sentence_one.cells != sentence_two.cells:  # Comparing sentences (if not the same).
                            if sentence_one.cells.issubset(sentence_two.cells):  # If sentence one is subset of sen_two.
                                new_set = sentence_two.cells.difference(sentence_one.cells)
                                if len(new_set) != 0:  # if new set is not empty (in case of bug).
                                    new_counts = sentence_two.count - sentence_one.count
                                    if new_counts >= 0:  # if the counts are equal or bigger than 0 (in case of bug).
                                        new_sentence = Sentence(new_set, new_counts)
                                        if new_sentence not in self.knowledge:  # if the sentence is not already in
                                            # the KB.
                                            self.knowledge.append(new_sentence)
                                            amended = True  # raising flag.

            if not amended:
                break  # If the run resulted in no amendments, then we can not make any additional amendments,
                # to our KB.

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        for cell in self.safes:
            if cell not in self.moves_made:
                return cell

        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """

        for i in range(self.height):
            for j in range(self.width):
                cell = (i, j)
                if cell not in self.moves_made and cell not in self.mines:
                    return cell

        return None
