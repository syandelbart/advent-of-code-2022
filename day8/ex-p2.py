
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

def get_visible_trees_line(tree_line : list, direction : Direction,reverse : bool = False,unknown : int = 0,max_allowed : int = 0): 
    tree_list = set()
    max = 0
    tree_lines_enumerated = enumerate(reversed(tree_line)) if reverse else enumerate(tree_line)
    for (index, tree) in  tree_lines_enumerated:
        print("Tree compare:",tree,max_allowed)
        if direction == Direction.HORIZONTAL:
            x = unknown
            y = index if not reverse else len(tree_line) - 1 - index
        else:
            y = unknown
            x = index if not reverse else len(tree_line) - 1 - index

        max = tree
        
        tree_list.add(Tree(x,y))
        if(tree >= max_allowed):
            break
        
                
    return tree_list

highest_visible_trees = set()

max_scenic = 0

def get_scenic_score(horizontal : int, vertical : int):
    tree_value = tree_map_vertical[horizontal][vertical]

    to_index_left = max(horizontal - 1,0) + 1
    to_index_right = min(horizontal + 1,len(tree_map_horizontal[0]) - 1)

    to_index_top = max(vertical - 1,0) + 1
    to_index_bottom = min(vertical + 1,len(tree_map_vertical[0]) - 1)

    scenic_left = get_visible_trees_line(tree_map_horizontal[vertical][0:to_index_left],Direction.HORIZONTAL,True,unknown=vertical,max_allowed=tree_value)
    scenic_right = get_visible_trees_line(tree_map_horizontal[vertical][to_index_right:len(tree_map_horizontal[vertical])],Direction.HORIZONTAL,False,unknown=vertical,max_allowed=tree_value)

    scenic_top = get_visible_trees_line(tree_map_vertical[horizontal][0:to_index_top],Direction.VERTICAL,True,unknown=vertical,max_allowed=tree_value)
    scenic_bottom = get_visible_trees_line(tree_map_vertical[horizontal][to_index_bottom:len(tree_map_vertical[horizontal])],Direction.VERTICAL,False,unknown=vertical,max_allowed=tree_value)

    return len(scenic_left) * len(scenic_right) * len(scenic_top) * len(scenic_bottom)


for horizontal in range(1,len(tree_map_horizontal[0])-1):
    for vertical in range(1,len(tree_map_vertical[0])-1):
        scenic_total = get_scenic_score(horizontal,vertical)

        if scenic_total > max_scenic:
            print(horizontal,vertical)
            max_scenic = scenic_total

print("Max Scenic:",max_scenic)

