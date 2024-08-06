class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
    
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, u, v):
        self.parent[self.find(u)] = self.find(v)

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)
    mst = []
    
    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
    
    return mst

# Input handling
vertices = input("Vertices: ").split()
edges = [(*input("Edge (u v weight): ").split(), int(input())) for _ in range(int(input("Number of edges: ")))]
print("MST:", kruskal(vertices, edges))
