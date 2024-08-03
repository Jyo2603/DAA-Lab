def bellman_ford(graph, vertices, src):
    dist = {vertex: float('inf') for vertex in vertices}
    dist[src] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    print("Vertex Distance from Source")
    for vertex in vertices:
        print("{}: {}".format(vertex, dist[vertex]))

def create_graph():
    graph = []
    V = int(input("Enter number of vertices: "))
    vertices = [input("Vertex {}: ".format(i + 1)) for i in range(V)]
    
    for _ in range(int(input("Enter number of edges: "))):
        u, v, w = input("Edge (u v w): ").split()
        w = int(w)
        if u not in vertices or v not in vertices:
            print("Invalid edge")
            return None, None
        graph.append((u, v, w))
    
    return graph, vertices

# Example usage
graph, vertices = create_graph()
if graph:
    src = input("Enter source vertex: ")
    if src in vertices:
        bellman_ford(graph, vertices, src)
    else:
        print("Source vertex not found.")
