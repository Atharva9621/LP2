from typing import List
from graph import Graph

def prims_algorithm(g: Graph, start: int = 0) -> tuple[List[int], int]:
    mst, cost = [], 0
    visited = [start, ]
    while len(visited) < g.n:
        unvisited_edges = [(wt, i, j) for i in visited for j, wt in enumerate(g[i]) if g.is_connected(i, j) and j not in visited]
        optimal = min(unvisited_edges)
        cost+=optimal[0]
        visited.append(optimal[2])
        mst.append((optimal[1], optimal[2]))
    return mst, cost

if __name__ == "__main__":
    g = Graph([(0, 2, 3),
               (1, 3, 4), (1, 2, 10),
               (2, 3, 2), (2, 4, 6),
               (3, 4, 1)], n=5, directed=True)
    g.display()
    mst, cost = prims_algorithm(g, 1)
    print(f"Cost: {cost}")
    print("MST: ", mst)