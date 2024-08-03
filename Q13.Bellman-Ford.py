def bellman_ford(graph, vertices, src):
    dist = {v: float('inf') for v in vertices}
    dist[src] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    if any(dist[u] != float('inf') and dist[u] + w < dist[v] for u, v, w in graph):
        print("Graph contains negative weight cycle")
        return

    print("Vertex Distance from Source")
    for vertex in vertices:
        print("{}: {}".format(vertex, dist[vertex]))

def create_graph():
    vertices = [input("Vertex {}: ".format(i + 1)) for i in range(int(input("Enter number of vertices: ")))]
    graph = []
    for _ in range(int(input("Enter number of edges: "))):
        u, v, w = input("Edge (u v w): ").split()
        graph.append((u, v, int(w)))
    return graph, vertices

# Example usage
graph, vertices = create_graph()
src = input("Enter source vertex: ")
if src in vertices:
    bellman_ford(graph, vertices, src)
else:
    print("Source vertex not found.")
