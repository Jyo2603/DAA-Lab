def bellman_ford(edges, vertices, src):
    dist = {v: float('inf') for v in vertices}
    dist[src] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    if any(dist[u] + w < dist[v] for u, v, w in edges):
        print("Graph contains negative weight cycle")
        return

    for v in vertices:
        print(v, ":", dist[v])

def create_graph():
    vertices = [input("Vertex: ") for _ in range(int(input("Number of vertices: ")))]
    edges = [tuple(input("Edge (u v w): ").split()) for _ in range(int(input("Number of edges: ")))]
    return edges, vertices

edges, vertices = create_graph()
src = input("Enter source vertex: ")
if src in vertices:
    bellman_ford(edges, vertices, src)
else:
    print("Source vertex not found.")
