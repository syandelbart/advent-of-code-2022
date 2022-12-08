
tree_map_horizontal  = list()
tree_map_vertical = list()
from enum import Enum
from typing import Self

class Direction(Enum):
    VERTICAL = 1
    HORIZONTAL = 2


for (index,line) in enumerate(open("./day8/input","r")):
    line_formatted = line.strip()
    line_chunks = list(map(int,list(line_formatted)))
    tree_map_horizontal.append(line_chunks)

    for (index_y,letter) in enumerate(line_chunks):
        if(index_y > len(tree_map_vertical) - 1):
            tree_map_vertical.append([])
        tree_map_vertical[index_y].append(letter)



class Tree :
    def __init__(self,x : int,y : int):
        self.x = x
        self.y = y
    def __eq__(self, other : Self):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        hash = 17
        hash = hash * 11 + self.x
        hash = hash * 11 + self.y
        return hash

        
trees_visible = list()

def get_visible_trees_line(tree_line : list, direction : Direction,reverse : bool = False,unknown : int = 0): 
    tree_list = set()
    max = 0
    tree_lines_enumerated = enumerate(reversed(tree_line)) if reverse else enumerate(tree_line)
    for (index, tree) in  tree_lines_enumerated:
        if tree > max or max == 0:
            if direction == Direction.HORIZONTAL:
                x = unknown
                y = index if not reverse else len(tree_line) - 1 - index
            else:
                y = unknown
                x = index if not reverse else len(tree_line) - 1 - index

            max = tree
            tree_list.add(Tree(x,y))
                
    return tree_list

print("horizontal")
print(tree_map_horizontal)
print("vert")
print(tree_map_vertical)


for (index,tree_line) in enumerate(tree_map_horizontal):
    print(tree_line)


print(tree_map_horizontal[0])
trees_hor = get_visible_trees_line(tree_map_horizontal[0],Direction.HORIZONTAL,True,unknown=index)
trees_rev = get_visible_trees_line(tree_map_horizontal[0],Direction.HORIZONTAL,False,unknown=index)
print("hor")
[print(tree.x,tree.y) for tree in trees_hor]
print("rev")
[print(tree.x,tree.y) for tree in trees_rev]
print("combined")
[print(tree.x,tree.y) for tree in trees_rev.union(trees_hor)]

highest_visible_trees = set()
for (index,horizontal_line) in enumerate(tree_map_horizontal):
    print("hor:",horizontal_line)
    highest_visible_trees = highest_visible_trees.union(get_visible_trees_line(horizontal_line,Direction.HORIZONTAL,True,unknown=index)).union(get_visible_trees_line(horizontal_line,Direction.HORIZONTAL,False,unknown=index))

for (index,vertical_line) in enumerate(tree_map_vertical):
    print("ver:",vertical_line)
    highest_visible_trees = highest_visible_trees.union(get_visible_trees_line(vertical_line,Direction.VERTICAL,True,unknown=index)).union(get_visible_trees_line(vertical_line,Direction.VERTICAL,False,unknown=index))

print(len(highest_visible_trees))