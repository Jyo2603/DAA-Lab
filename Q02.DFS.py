def DFS(arr, visited, node, labels):
    if visited[node]: return
    visited[node] = True
    print(labels[node])
    for neighbor, connected in enumerate(arr[node]):
        if connected and not visited[neighbor]:
            DFS(arr, visited, neighbor, labels)

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

print("DFS traversal:")
DFS(arr, [False] * n, start, labels)
