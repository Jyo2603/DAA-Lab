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
