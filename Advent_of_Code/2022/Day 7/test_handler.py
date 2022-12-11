import regex as re

cd_regex = re.compile(r'(?:^\$ cd) (.*.)')
dir_regex = re.compile(r'dir (.*.)')
file_regex = re.compile(r'(\d+) (.*.)')

class Path_Tree:
    def __init__(self, name, parent):
        self.name = name # String, name of the folder
        self.parent = parent # Path_Tree Object of the parental node
        self.children = dict() # {Name of file: Path_Tree object}
        self.files = dict() # {Name of file: Size}
        self.size = 0 # Size
    
    def __str__(self, level=1):
        #ret = '---'*level+repr(self.name)+'\n'
        center = 3 + level
        ret = (repr(self.name) + repr({self.size}) + '\n').rjust(center)
        for child in self.children:
            ret += self.children[child].__str__(level+3)
        return ret
    
    def __repr__(self):
        return '<tree node representation>'
    
root = Path_Tree('root', 'Root')
with open(r'Advent_of_Code\2022\Day 7\test.txt', 'r') as file:
    current_dir = root # Setting current_dir to dummy root
    for line in file:
        if line[:4] == '$ cd':
            if line[5:7] == '..':
                current_dir = current_dir.parent # If cd .. we are following pointer to parental Path_Tree object
            else:
                name = cd_regex.search(line)
                name = str(name.group(1)) # Exctraing folder name, e.g. cd a -> a
                try:
                    current_dir = current_dir.children[name] # If we already have this object in children
                except:
                    child = Path_Tree(name, current_dir) # Otherwise create a new Path_Tree Object
                    current_dir.children[name] = child
                    current_dir = current_dir.children[name]
        elif line[:2].isnumeric(): # If the input is of size '...'
            size_and_name = file_regex.search(line)
            size = int(size_and_name.group(1)) # Name
            name = size_and_name.group(2) # Size
            current_dir.size += size # We are adding the size of the file to the current folder
            current_dir.files[name] = size
            par_dir = current_dir.parent # Now we are backpropagating the size of the file to the parental folders
            while par_dir.parent != 'Root': # While the dummy root is not yet reached
                par_dir.size += size # We are adding size of the file to the parental folders
                par_dir = par_dir.parent # And we are moving to the next parent.
                # This way, if the file is in the folder abb that is a <- ab <- abb
                # All the parental folders (a and ab) will include this file. 
        else:
            pass # We are not interested in other commands.

# For the first task
below_10000 = []
def call_children(tree):
    print("{} that is of size {}".format(tree.name, tree.size))
    if tree.size <= 100000:
        below_10000.append(tree.size)
    
    if tree.children:
        for child in tree.children:
            call_children(tree.children[child])

# For the second task
fits = []
def find_smallets(tree):
    if tree.size >= space_needed:
        fits.append(tree.size)
        print("A new candidate found {} which will give a free space of {}".format(tree.name, tree.size))
    
    if tree.children:
        for child in tree.children:
            find_smallets(tree.children[child])
free_space = 70000000 - root.children['/'].size
space_needed = 30000000 - free_space
print(space_needed)
find_smallets(root)
print(sorted(fits))

str(root)
print(root)