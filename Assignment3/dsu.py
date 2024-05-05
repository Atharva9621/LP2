class DisjoinSet:
    def __init__(self, n: int) -> None:
        self.size = [1 for i in range(n+1)]
        self.parent = [i for i in range(n+1)]

    def findParent(self, u):
        if self.parent[u]==u:
            return u
        else:
            self.parent[u] = self.findParent(self.parent[u]) #Path compression
            return self.parent[u]
        
    def __getitem__(self, key):
        return self.findParent(key)

    def union(self, u: int, v: int)->None:
        u_par, v_par = self.findParent(u), self.findParent(v)
        if u_par == v_par:
            return
        if self.size[u_par]>=self.size[v_par]:
            self.parent[v_par]=u_par
            self.size[u_par]+=self.size[v_par]
        else:
            self.parent[u_par]=v_par
            self.size[v_par]+=self.size[u_par]

    def display(self):
        print("DisjointSet : { ")
        print(' '*5, self.size)
        print(' '*5, self.parent)
        print("}")


if __name__ == "__main__":
    dj = DisjoinSet(8)
    dj.union(1,2)
    dj.display()
    dj.union(2,3)
    dj.display()
    dj.union(4,5)
    dj.display()
    dj.union(6,7)
    dj.display()
    dj.union(5,6)
    print(dj.findParent(4)==dj.findParent(7))
    dj.display()




