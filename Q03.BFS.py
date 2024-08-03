def bfs_matrix(matrix, start):
    visited = set()
    queue = [start]  # Using a list as a queue
    
    while queue:
        node = queue.pop(0)  # Dequeue
        if node not in visited:
            visited.add(node)
            print(node)
            for i, adjacent in enumerate(matrix[node]):
                if adjacent and i not in visited:
                    queue.append(i)  # Enqueue

n = int(input("Enter the number of nodes: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

start_node = int(input("Enter the starting node for BFS: "))

print("BFS traversal:")
bfs_matrix(matrix, start_node)
