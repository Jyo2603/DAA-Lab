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
    for _ in range(int(input("Enter the number of vertices: "))):
        data = input("Enter vertex and its edges (vertex1 weight1 vertex2 weight2 ...): ").split()
        graph[data[0]] = {data[i]: int(data[i+1]) for i in range(1, len(data), 2)}

    start_vertex = input("Enter the start vertex: ")
    distances = dijkstra(graph, start_vertex)
    
    for vertex, distance in distances.items():
        print(vertex, distance)

if __name__ == "__main__":
    main()
  
*/Enter the number of vertices: 3
Enter vertex and its edges (vertex1 weight1 vertex2 weight2 ...): A B 1 C 4
Enter vertex and its edges (vertex1 weight1 vertex2 weight2 ...): B C 2
Enter vertex and its edges (vertex1 weight1 vertex2 weight2 ...): C A 3
Enter the start vertex: A
A 0
B 1
C 3/*
