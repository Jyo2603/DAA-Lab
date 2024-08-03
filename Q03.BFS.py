def BFS(arr, start):
    visited = [False] * len(arr)
    queue = [start]
    visited[start] = True

    while queue:
        node = queue.pop(0)
        print(node)
        for neighbor in range(len(arr[node])):
            if arr[node][neighbor] and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

n = int(input("Enter number of vertices: "))
arr = [[0] * n for _ in range(n)]
for _ in range(int(input("Enter number of edges: "))):
    u, v = map(int, input("Enter edge (u, v): ").split())
    arr[u][v] = arr[v][u] = 1
print("Adjacency matrix:")
for row in arr: print(row)
start = int(input("Enter start node: "))
print("BFS traversal:")
BFS(arr, start)
