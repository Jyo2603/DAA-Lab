def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_vertex = min((v for v in graph if v not in visited), key=lambda v: distances[v])
        visited.add(min_vertex)

        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited:
                distances[neighbor] = min(distances[neighbor], distances[min_vertex] + weight)
    
    return distances

def main():
    graph = {}
    for _ in range(int(input("Enter the number of edges: "))):
        u, v, w = input("Enter edge (u v weight): ").split()
        w = int(w)
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = w
        graph[v][u] = w  # Remove this line if the graph is directed
    
    start_vertex = input("Enter the start vertex: ")
    distances = dijkstra(graph, start_vertex)

    print("Shortest distances from vertex", start_vertex)
    for vertex, dist in distances.items():
        print(f"{vertex}: {dist}")

if __name__ == "__main__":
    main()
