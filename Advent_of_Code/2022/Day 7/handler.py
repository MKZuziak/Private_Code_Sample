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
    
    def print_tree(self):
        current_dir= self
        for child_name in self.children:
            current_dir = current_dir.children[child_name]
            for file in self.files:
                print(r'-{}, size:{}'.format(file, self.files[file]))


root = Path_Tree('root', 'Root')

with open(r'Advent_of_Code\2022\Day 7\source.txt', 'r') as file:
    current_dir = root
    for line in file:
        if line[:4] == '$ cd':
            if line[5:7] == '..':
                # We want to update the size of all the parental folders at this point.
                par_dir = current_dir.parent
                cur_dir = current_dir
                while par_dir.parent != 'Root':
                    par_dir.size += current_dir.size
                    par_dir = par_dir.parent
                    cur_dir = par_dir
                current_dir = current_dir.parent
            else:
                name = cd_regex.search(line)
                name = str(name.group(1))
                child = Path_Tree(name, current_dir)
                current_dir.children[name] = child
                current_dir = current_dir.children[name]
        elif line[:3] == 'dir':
            name = dir_regex.search(line)
            name = str(name.group(1))
            child = Path_Tree(name, current_dir)
            current_dir.children[name] = child
        elif line[:2].isnumeric():
            size_and_name = file_regex.search(line)
            size = int(size_and_name.group(1))
            name = size_and_name.group(2)
            current_dir.size += size
            current_dir.files[name] = size
        else:
            pass

#print(root.children[r'/'].children[r'jtrbrcjl'].children)
print(root.children[r'/'].children[r'jtrbrcjl'].size)