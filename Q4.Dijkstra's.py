import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    
    for _ in range(num_vertices):
        data = input("Enter vertex and its edges (vertex weight vertex weight ...): ").split()
        vertex = data[0]
        edges = {}
        for i in range(1, len(data), 2):
            neighbor = data[i]
            weight = int(data[i + 1])
            edges[neighbor] = weight
        graph[vertex] = edges

    start_vertex = input("Enter the start vertex: ")
    distances = dijkstra(graph, start_vertex)
    
    for vertex, distance in distances.items():
        print(f"{vertex} {distance}")

if __name__ == "__main__":
    main()
