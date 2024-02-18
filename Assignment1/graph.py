from typing import List
from collections import deque

class UnweightedGraph:
    def __init__(self, adj_list: List[tuple[int]] = None, graph:List[List[int]] = None, n: int = None, directed: bool="undirected") -> None:
        self.directed = directed
        if adj_list:
            self.n = n
            self.graph = [[0 for i in range(n)] for j in range(n)]
            for pair in adj_list:
                self.graph[pair[0]][pair[1]] = 1
                if self.directed:
                    self.graph[pair[1]][pair[0]] = 1
        else:
            self.graph = graph
        if n==None:
            self.n = len(graph)
        else:
            self.n = n
            
    def __getitem__(self, key):
        return self.graph[key]
    def __str__(self) -> str:
        return f'<graph : n: {self.n}, directed: {self.directed}>'
    def display(self):
        print(self)
        print(' ', end=" | ")
        for i in range(self.n):
            print(i, end=" ")
        print()
        print('-'*(2*self.n+4))
        for idx, i in enumerate(self.graph):
            print(idx, end=' | ')
            for j in i:
                print(j, end=" ")
            print()
        print('-'*(2*self.n+4))

    def bfsTraversal(self, i=0):
        visited = [0 for nbr in range(self.n)]
        q = deque(maxlen=self.n)
        q.append(i)
        visited[i] = True
        while not len(q)==0:
            curr = q.popleft()
            print(curr, end=" ")

            for nbr in range(self.n):
                if self[curr][nbr] and not visited[nbr]:
                    visited[nbr] = True
                    q.append(nbr)

    
    def dfs_traversal_recursive(self, visited, i):
        print(i, end=" ")
        visited[i] = 1
        for neighbour in range(self.n):
            if self[i][neighbour]==1 and not visited[neighbour]:
                self.dfs_traversal_recursive(visited, neighbour)
        

    def dfsTraversal(self, i=0):
        visited = [0 for i in range(self.n)]
        self.dfs_traversal_recursive(visited, i)
        print()


if __name__ == "__main__":
    g = UnweightedGraph([(0, 1), (0, 2), (0, 3), (2, 4), (4, 3)], n=5, directed=True)
    g.display()
    print("DFS Traversal")
    g.dfsTraversal()
    print('_'*10)
    print('BFS Traversal')
    g.bfsTraversal()