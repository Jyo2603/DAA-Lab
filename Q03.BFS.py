def BFS(arr, start, labels):
    visited = [False] * len(arr)
    queue = [start]
    visited[start] = True
    
    while queue:
        node = queue.pop(0)  # Remove the first element
        print(labels[node])
        for neighbor, connected in enumerate(arr[node]):
            if connected and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

n = int(input("Enter number of vertices: "))
labels = [input(f"Enter label for vertex {i}: ") for i in range(n)]

arr = [[0] * n for _ in range(n)]
for _ in range(int(input("Enter number of edges: "))):
    u, v = input("Enter edge (u, v): ").split()
    u_index, v_index = labels.index(u), labels.index(v)
    arr[u_index][v_index] = arr[v_index][u_index] = 1

print("Adjacency matrix:")
for row in arr: print(row)

start_label = input("Enter start node: ")
start = labels.index(start_label)

print("BFS traversal:")
BFS(arr, start, labels)
