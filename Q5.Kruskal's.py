class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, u, v):
        self.parent[self.find(u)] = self.find(v)

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)
    mst = []
    
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
    
    return mst

# Example usage with user input
vertices = input("Vertices: ").split()
edges = []
num_edges = int(input("Number of edges: "))

for _ in range(num_edges):
    u, v, weight = input("Edge (u v weight): ").split()
    edges.append((u, v, int(weight)))

mst = kruskal(vertices, edges)
print("MST:", mst)

'''
ALGORITHM 
function Kruskal(graph):
    mst = []
    edges = sorted(graph.edges, key=lambda edge: edge.weight)
    ds = DisjointSet(graph.vertices)

    for edge in edges:
        u, v, weight = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append(edge)
    
    return mst
,,,
