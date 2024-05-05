from typing import List
from graph import Graph
from dsu import DisjoinSet

def kruskals_algorithm(adjList: List[tuple[int]], n:int):
    adjList = sorted(adjList, key=lambda x: x[2])
    mst = []
    djs = DisjoinSet(n)
    for i, edge in enumerate(adjList):
        if not djs.findParent(edge[0]) == djs.findParent(edge[1]):
            mst.append(edge)
            djs.union(edge[0], edge[1])
        if len(mst) == n-1:
            return mst, sum([edge[2] for edge in mst])
        
if __name__ == "__main__":
    g = Graph([(0, 2, 3),
               (1, 3, 4), (1, 2, 10),
               (2, 3, 2), (2, 4, 6),
               (3, 4, 1)], n=5, directed=True)
    g.display()
    mst, cost = kruskals_algorithm([(0, 2, 3),
               (1, 3, 4), (1, 2, 10),
               (2, 3, 2), (2, 4, 6),
               (3, 4, 1)], 5)
    print(f"Cost: {cost}")
    print("MST: ", mst)