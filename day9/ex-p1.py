from typing import Self
import math

class Coordinate:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other : Self):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        hash = 17
        hash = hash * 11 + self.x
        hash = hash * 11 + self.y
        return hash
    def distance(self, other : Self):
        return math.sqrt(math.pow(self.x - other.x,2) + math.pow(self.y - other.y,2))
    def isDirectDiagonal(self, other : Self):
        return abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1
    def get_x(self) -> int:
        return self.x
    def get_y(self) -> int:
        return self.y
    def add(self, other : Self):
        return Coordinate(self.x + other.x,self.y + other.y)
    def moveTo(self, direction : str):
        if(direction == "U"):
            return self.add(Coordinate(0,1))
        elif(direction == "R"):
            return self.add(Coordinate(1,0))
        elif(direction == "D"):
            return self.add(Coordinate(0,-1))
        elif(direction == "L"):
            return self.add(Coordinate(-1,0))

directions : list[str] = []

positions_visited = set()
position_head = Coordinate(0,0)
position_tail = Coordinate(0,0)


for (index,line) in enumerate(open("./day9/input","r")):
    line_chunks = line.strip().split(" ")

    # append letter direction to directions array for the amount after the letter
    [directions.append(line_chunks[0]) for x in range(0,int(line_chunks[1]))]

counter = 0

print("Initial")
print(position_head.x,position_head.y)
print(position_tail.x,position_tail.y)
    

for direction in directions:
    position_head = position_head.moveTo(direction)

    distance = position_head.distance(position_tail)

    if(distance == 2):
        position_tail = position_tail.moveTo(direction)
    elif(distance > 1 and not position_head.isDirectDiagonal(position_tail)):
        # check which diagonal it is, we know one direction
        if(direction == "U" or direction == "D"):
            if(position_head.get_x() > position_tail.get_x()):
                position_tail = position_tail.moveTo(direction).add(Coordinate(1,0))
            else:
                position_tail = position_tail.moveTo(direction).add(Coordinate(-1,0))
        else:
            if(position_head.get_y() > position_tail.get_y()):
                position_tail = position_tail.moveTo(direction).add(Coordinate(0,1))
            else:
                position_tail = position_tail.moveTo(direction).add(Coordinate(0,-1))

    positions_visited.add(position_tail)
    
    # if counter > 20:
    #    break
    # counter += 1

positions_visited.append(Coordinate(0,0))

print(len(positions_visited))
        




    



    