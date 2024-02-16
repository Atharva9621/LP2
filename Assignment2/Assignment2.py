from collections import namedtuple
from typing import List
from frozen_lake import FrozenLake
Point = namedtuple('Point', ['x', 'y'])

class Node:
    def __init__(self, x, y, gcost=100, parent=None) -> None:
        self.x = x
        self.y = y
        self.gcost = gcost
        self.parent = parent
    def __str__(self) -> str:
        return f'Node(x: {self.x}, y:{self.y})'
    # def __eq__(self, other) -> bool:
    def equals(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    def __gt__(self, other) -> bool:
        return self.gcost > other.gcost
    def __lt__(self, other) -> bool:
        return self.gcost < other.gcost
    
    def neighbours(self) -> List[str]:
        return [
            Node(self.x+1, self.y),
            Node(self.x-1, self.y),
            Node(self.x, self.y+1),
            Node(self.x, self.y-1)
        ]

def heuristic(a: Node, b: Node, type="manhattan") -> int:
    if type=="manhattan":
        x_offset = abs(a.x-b.x)
        y_offset = abs(a.y-b.y)
    return x_offset + y_offset

def a_star_search(grid: List[List[int]], start: Point, end: Point) -> int:
    openset = []
    closedset = []
    startNode = Node(start.x,start.y)
    endNode = Node(end.x, end.y)
    print("Init: ", startNode, endNode)
    startNode.gcost = 0
    openset.append(startNode)

    while(len(openset)!=0):
        openset.sort()
        currNode = openset.pop(0)
        closedset.append(currNode)
        # print(currNode)

        if currNode.equals(endNode):
            return currNode.gcost, currNode

        for neighbour in currNode.neighbours():
            if not grid[neighbour.x][neighbour.y] and neighbour not in closedset:
                cost = currNode.gcost + heuristic(currNode, neighbour)
                if cost<neighbour.gcost or neighbour not in openset:
                    neighbour.gcost = cost
                    neighbour.hcost = heuristic(neighbour, endNode)
                    neighbour.parent = currNode

                    if neighbour not in openset:
                        openset.append(neighbour)

    return -69, None


grid = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
        ]
start = Point(6, 2)
end = Point(6, 4)
min_distance, last = a_star_search(grid, start, end)
print(f"Optimal Distance : {min_distance}")

print("PATH: ")
while(not last==None):
    print(last)
    grid[last.x][last.y]=2
    last=last.parent

for row in grid:
    print(row)

lake = FrozenLake(grid, None)
lake.run()