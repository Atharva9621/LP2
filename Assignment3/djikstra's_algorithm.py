from typing import List
from graph import Graph

def djikstras_algorithm(g: Graph, start: int=0)->dict:
    visited, unvisited = {start: 0}, {}
    current = start
    for i in range(g.n-1):
        neighbours = [i for i in range(g.n) if g.is_connected(current, i)]
        for neighbour in neighbours:
            if neighbour not in visited:
                if neighbour in unvisited:
                    unvisited[neighbour]=min(unvisited[neighbour], visited[current]+g[current][neighbour])
                else:
                    unvisited[neighbour]=visited[current]+g[current][neighbour]
        current = min(unvisited.items(), key=lambda x: x[1])[0]
        visited[current] = unvisited[current]
        unvisited.pop(current)

    return visited
    
if __name__=="__main__":
    #Test on GFG example  ==>   https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
    graph =  [
        [-1, 4, -1, -1, -1, -1, -1, 8, -1],
        [4, -1, 8, -1, -1, -1, -1, 11, -1],
        [-1, 8, -1, 7, -1, 4, -1, -1, 2],
        [-1, -1, 7, -1, 9, 14, -1, -1, -1],
        [-1, -1, -1, 9, -1, 10, -1, -1, -1],
        [-1, -1, 4, 14, 10, -1, 2, -1, -1],
        [-1, -1, -1, -1, -1, 2, -1, 1, 6],
        [8, 11, -1, -1, -1, -1, 1, -1, 7],
        [-1, -1, 2, -1, -1, -1, 6, 7, -1]
    ]
    g = Graph(graph=graph)
    g.display()
    min_paths = djikstras_algorithm(g)
    print("Distances : ", min_paths)