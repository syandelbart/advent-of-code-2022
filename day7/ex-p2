import re
from enum import Enum
from typing import Self

class Type(Enum):
    DIR = 1
    FILE = 2

class File:
    def __init__(self, name : str, size : int, parent : Self,type : Type = Type.DIR):
        self.name = name
        self.size = size
        self.parent = parent
        self.type = type
        self.simulated_size = None
        if(self.parent):
            self.parent.add_children(self)
        self.children = list()
    def get_name(self):
        return self.name
    def get_parent(self):
        return self.parent
    def get_children(self):
        return self.children
    def add_children(self, child):
        self.children.append(child)
    def get_size(self):
        return self.size
    def is_file(self):
        return self.type == Type.FILE
    def get_simulated_size(self):
        return self.simulated_size
    def set_simulated_size(self,value : int):
        self.simulated_size = value

max_file_size = 100000
size_total = 0

def print_structure(file : File,depth = 0):
    global size_total
    

    size = file.get_size()

    for child in file.get_children():
        size += print_structure(child,depth + 1)
    
    if not file.is_file():
        file.set_simulated_size(size)
        if size <= max_file_size:
            size_total += size


    print("|","F" if file.is_file() else "D" ,"-" * depth,file.name, file.get_simulated_size(),)

    return size

cur = File("/",0,None)
root = cur

for line in open("./day7/input","r"):
    line_formatted = line.strip()
    line_chunks = list(line)

    match = re.findall(r'\w+\.\w+|\w+|/|\.\.',line_formatted)

    arg1 = match[0]

    if arg1 == "ls":
        # print("ls",match)
        continue
    elif arg1 == "cd":
        # print("cd",match)
        arg2 = match[1]
        if arg2 == "..":
            cur = cur.get_parent()
        elif arg2 == "/":
            cur = root
        else:
            for child in cur.get_children():
                if child.name == arg2:
                    cur = child


    elif arg1 == "dir":
        # print("dir",match)
        dir = File(match[1],0,cur,type=Type.DIR)

    else:
        file = File(match[1],int(arg1),cur,type=Type.FILE)

# finding smallest that is large enough
total_space = 70000000
unused_req = 30000000
smallest_freeing_up_space = None
smallest_map = {}



print(print_structure(root))
print("Size:",size_total)

root_actual_size = root.get_simulated_size()
size_free = total_space - root_actual_size
space_to_free = max(0,unused_req - size_free)

print("Root Actual Size:", root_actual_size)
print("Size required:", size_free)
print("Space to free up:", space_to_free)

smallest : File = root

def get_smallest_dir(dir : File,depth = 0):
    global smallest

    if dir.is_file():
        return

    for child in dir.get_children():
        get_smallest_dir(child,depth + 1)

    dir_size = dir.get_simulated_size()
    
    if dir_size is not None and dir_size < smallest.get_simulated_size() and dir_size >= space_to_free:
        smallest = dir

lowest_file = get_smallest_dir(root)
print("Smallest directory size to remove:",smallest.get_simulated_size())
