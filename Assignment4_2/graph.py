from typing import List
from collections import deque

class Graph:
    def __init__(self, adj_list: List[tuple[int]] = None, graph:List[List[int]] = None, n: int = None,
                 directed: bool=False) -> None:
        self.directed = directed
        if adj_list:
            self.n = n
            self.graph = [[0 for i in range(n)] for j in range(n)]
            for pair in adj_list:
                weight = 1
                if len(pair)==3:
                    weight = pair[2]
                self.graph[pair[0]][pair[1]] = weight
                if self.directed:
                    self.graph[pair[1]][pair[0]] = weight
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
    def is_connected(self, i, j):
        return bool(self[i][j])
    
    def neighbours(self, i, weights = False)->List:
        neighbours =  [j for j in range(self.n) if self.is_connected(i, j)]
        if weights:
            neighbours = [(j, self.graph[i][j]) for j in neighbours]
        return neighbours
    
    def display(self, padding=3):
        print('-'*(2*padding*self.n))
        print(self)
        print('_'*(2*padding*self.n))
        print(' ', end=" | ")
        for i in range(self.n):
            print(f'{i:^{padding}}', end=" ")
        print()
        print('_'*(2*padding*self.n))
        for idx, i in enumerate(self.graph):
            print(idx, end=' | ')
            for j in i:
                print(f'{j:>{padding}}', end=" ")
            print()
        print('-'*(2*padding*self.n))

    def bfsTraversal(self, i=0):
        visited = [0 for nbr in range(self.n)]
        q = deque(maxlen=self.n)
        q.append(i)
        visited[i] = True
        while not len(q)==0:
            curr = q.popleft()
            print(curr, end=" ")

            for nbr in range(self.n):
                if self.is_connected(curr, nbr) and not visited[nbr]:
                    visited[nbr] = True
                    q.append(nbr)        

    def dfsTraversal(self, i=0):
        def dfs_traversal_recursive(visited, i):
            print(i, end=" ")
            visited[i] = 1
            for neighbour in range(self.n):
                if self.is_connected(i, neighbour) and not visited[neighbour]:
                    dfs_traversal_recursive(visited, neighbour)

        visited = [0 for i in range(self.n)]
        dfs_traversal_recursive(visited, i)
        print()


if __name__ == "__main__":
    g = Graph([(0, 1, 7), (0, 2, 6), (0, 3), (2, 4, 9), (4, 3)], n=5, directed=True)
    g.display()
    print("DFS Traversal")
    g.dfsTraversal()
    print('_'*10)
    print('BFS Traversal')
    g.bfsTraversal()