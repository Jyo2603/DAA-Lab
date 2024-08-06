def BFS(arr, start, n):
    visited = [False] * n
    queue = [start]
    visited[start] = True
    
    while queue:
        node = queue.pop(0)  # Dequeue the first element
        print(node)
        for neighbor, connected in enumerate(arr[node]):
            if connected and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)  # Enqueue

n = int(input("Enter number of vertices: "))

arr = [[0] * n for _ in range(n)]
for _ in range(int(input("Enter number of edges: "))):
    u, v = map(int, input("Enter edge (u, v): ").split())
    arr[u][v] = arr[v][u] = 1

print("Adjacency matrix:")
for row in arr:
    print(row)

start = int(input("Enter start node: "))

print("BFS traversal:")
BFS(arr, start, n)
