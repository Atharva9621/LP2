from typing import List
from graph import Graph

class ColorGraph(Graph):
    def color(self, k:int)->bool:
        self.colors = [0]*self.n
        def recursive_color(v: int):
            if v==self.n:
                return True
            for color in range(1, k+1):
                neighbour_colors = set([self.colors[neighbour] for neighbour in self.neighbours(v)])
                if color not in neighbour_colors:
                    self.colors[v]=color
                    if recursive_color(v+1):
                        return True
                    else:
                        self.colors[v]=0
            return False

        current = 0
        return recursive_color(current)
    
if __name__ == "__main__":
    g = ColorGraph([(0, 1, 7), (0, 2, 6), (1, 2, 6), (0, 3), (2, 4, 9), (4, 3)], n=5, directed=True)
    g.display()
    g.color(3)
    print(g.colors)
