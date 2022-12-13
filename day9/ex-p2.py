from typing import Self
import math

class Coordinate:
    x = 0
    y = 0
    previous : Self
    next : Self
    def __init__(self,x,y,next : Self = False):
        self.x = x
        self.y = y
        self.previous = False
        self.next = next
    def __eq__(self, other : Self):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        hash = 17
        hash = hash * 11 + self.x
        hash = hash * 11 + self.y
        return hash
    def set_previous(self, other : Self):
        self.previous = other
    def set_next(self, other : Self):
        self.next = other
    def get_next(self) -> Self:
        return self.next
    def distance(self, other : Self):
        return math.sqrt(math.pow(self.x - other.x,2) + math.pow(self.y - other.y,2))
    def isDirectDiagonal(self, other : Self):
        return abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1
    def get_x(self) -> int:
        return self.x
    def get_y(self) -> int:
        return self.y
    def add(self, other : Self) -> Self:
        return Coordinate(self.x + other.x,self.y + other.y,self.next)
    def moveTo(self, direction : str) -> Self:
        if(direction == "U"):
            return self.add(Coordinate(0,1))
        elif(direction == "R"):
            return self.add(Coordinate(1,0))
        elif(direction == "D"):
            return self.add(Coordinate(0,-1))
        elif(direction == "L"):
            return self.add(Coordinate(-1,0))
    def moveToParent(self, parent : Self,direction : str) -> Self:
        distance = self.distance(parent)
        print(distance)
        if(distance == 2):
            if(parent.x > self.x):
                direction = "R"
            elif(parent.x < self.x):
                direction = "L"
            elif(parent.y > self.y):
                direction = "U"
            elif(parent.y < self.y):
                direction = "D"
            return self.moveTo(direction)
        elif(distance > 1 and not parent.isDirectDiagonal(self)):
            # check which diagonal it is, we DONT know one direction
            if(parent.x > self.x):
                direction = "R"
            elif(parent.x < self.x):
                direction = "L"
            elif(parent.y > self.y):
                direction = "U"
            elif(parent.y < self.y):
                direction = "D"



            if(direction == "U" or direction == "D"):
                if(parent.get_x() > self.get_x()):
                    return self.moveTo(direction).add(Coordinate(1,0))
                else:
                    return self.moveTo(direction).add(Coordinate(-1,0))
            else:
                if(parent.get_y() > self.get_y()):
                    return self.moveTo(direction).add(Coordinate(0,1))
                else:
                    return self.moveTo(direction).add(Coordinate(0,-1))
                    
        return self
    def __str__(self) -> str:
        return "({x},{y})".format(x=self.x,y=self.y)

def print_positions(visited_positions):
    minimum_x = min(visited_positions,key=lambda coordinate: coordinate.x )
    maximum_x = max(visited_positions,key=lambda coordinate: coordinate.x )
    minimum_y = min(visited_positions,key=lambda coordinate: coordinate.y )
    maximum_y = max(visited_positions,key=lambda coordinate: coordinate.y )

    for i in reversed(range(minimum_y.y,maximum_y.y)):
        for j in range(minimum_x.x,maximum_x.x):
            if Coordinate(j,i) in positions_visited:
                print("#",end="")
            else:
                print(".",end="")
        print("")

def print_snake(head, iteration = 0,direction = ""):
    positions = []
    cur = head
    while(cur.get_next()):
        positions.append(cur)
        cur = cur.get_next()

    minimum_y = -10
    maximum_y = 10
    minimum_x = -10
    maximum_x = 10

    print("-------", iteration, direction)
    
    for i in reversed(range(minimum_y,maximum_y)):
        for j in range(minimum_x,maximum_x):
            if i == 0 and j == 0:
                print("s",end="")
            elif Coordinate(j,i) in positions:
                print(positions.index(Coordinate(j,i)),end="")
            else:
                print(".",end="")
        print("")
    

directions : list[str] = []

positions_visited = set()
position_head = Coordinate(0,0)

cur = position_head
for x in range(0,9):
    knot = Coordinate(0,0)
    cur.set_next(knot)
    cur = knot


position_tail = Coordinate(0,0)


for (index,line) in enumerate(open("./day9/input","r")):
    line_chunks = line.strip().split(" ")

    # append letter direction to directions array for the amount after the letter
    [directions.append(line_chunks[0]) for x in range(0,int(line_chunks[1]))]


direction_changed_prev = ""

for direction in directions:
    position_head = position_head.moveTo(direction)
    cur = position_head
    cur_next = cur.get_next()

    # print("Direction",direction)
    # print(cur.x,cur.y)
    counter = 0
    while cur_next:
        counter += 1
        modified_knot = cur_next.moveToParent(cur,direction)
        # print(modified_knot.x,modified_knot.y)

        cur.set_next(modified_knot)
        modified_knot.set_next(cur_next.get_next())
    
        # print(str(cur))
        # print(str(cur_next))
        # print(str(modified_knot))
        # print_snake(position_head,counter,direction)

        cur = modified_knot
        cur_next = modified_knot.get_next()



    positions_visited.add(cur)

    # if(direction_changed_prev != direction):
    #     direction_changed_prev = direction
        
    #     print_positions(positions_visited)
    #     print("Direction:",direction)

    
    
    # if counter > 20:
    #    break
    # counter += 1

positions_visited.add(Coordinate(0,0))

print("End")
# print_positions(positions_visited)


print(len(positions_visited))
        




    



    