def bellman_ford(graph, V, E, src):
    dist = [float('inf')] * V
    dist[src] = 0
    
    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return
            
    print("Vertex Distance from Source")
    for i in range(V):
        print(i, dist[i])

V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))
graph = []

for _ in range(E):
    u, v, w = map(int, input("Enter edge (u v w): ").split())
    graph.append((u, v, w))
src = int(input("Enter the source vertex: "))

bellman_ford(graph, V, E, src)






def bellman_ford(graph, V, src):
    dist = {vertex: float('inf') for vertex in graph}
    dist[src] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    print("Vertex Distance from Source")
    for vertex in dist:
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
            return None
        graph.append((u, v, w))
    
    return graph, V

# Example usage
graph, V = create_graph()
if graph:
    src = input("Enter source vertex: ")
    if src in dict(graph).keys():
        bellman_ford(graph, V, src)
    else:
        print("Source vertex not found.")

