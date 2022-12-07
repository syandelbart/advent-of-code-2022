import re
from enum import Enum

class Type(Enum):
    DIR = 1
    FILE = 2

class File:
    def __init__(self, name : str, size : int, parent,type : Type = Type.DIR):
        self.name = name
        self.size = size
        self.parent = parent
        self.type = type
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

max_file_size = 100000
size_total = 0

def print_structure(file,depth = 0):
    global size_total
    print("|","F" if file.is_file() else "D" ,"-" * depth,file.name, file.get_size(),)

    size = file.get_size()

    for child in file.get_children():
        size += print_structure(child,depth + 1)
    
    if not file.is_file():
        if size <= max_file_size:
            size_total += size

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

print(print_structure(root))
print("Size:",size_total)


