import regex as re

cd_regex = re.compile(r'(?:^\$ cd) (.*.)')
dir_regex = re.compile(r'dir (.*.)')
file_regex = re.compile(r'(\d+) (.*.)')

class Path_Tree:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = dict() # {Name of file: Path_Tree object}
        self.files = dict() # {Name of file: Size}
        self.size = 0
    
root = Path_Tree('root', 'Root')
with open(r'Advent_of_Code\2022\Day 7\source.txt', 'r') as file:
    current_dir = root
    for line in file:
        if line[:4] == '$ cd':
            if line[5:7] == '..':
                current_dir = current_dir.parent
            else:
                name = cd_regex.search(line)
                name = str(name.group(1))
                try:
                    current_dir = current_dir.children[name]
                except:
                    child = Path_Tree(name, current_dir)
                    current_dir.children[name] = child
                    current_dir = current_dir.children[name]
        elif line[:2].isnumeric():
            size_and_name = file_regex.search(line)
            size = int(size_and_name.group(1))
            name = size_and_name.group(2)
            current_dir.size += size
            current_dir.files[name] = size
            par_dir = current_dir.parent
            while par_dir.parent != 'Root':
                par_dir.size += size
                par_dir = par_dir.parent
        else:
            pass

below_10000 = []
space_needed = 30000000 - 24933642

def call_children(tree):
    print("{} that is of size {}".format(tree.name, tree.size))
    if tree.size <= 100000:
        below_10000.append(tree.size)
    
    if tree.children:
        for child in tree.children:
            call_children(tree.children[child])

fits = []
def find_smallets(tree):
    margin = space_needed - tree.size
    if margin < 0:
        fits.append(tree.size)
        print("New best fit founded: delete {} which will give a margin of {}".format(tree.name, margin))
    
    if tree.children:
        for child in tree.children:
            find_smallets(tree.children[child])
