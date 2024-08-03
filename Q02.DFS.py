def dfs(matrix, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)

    for i, adjacent in enumerate(matrix[node]):
        if adjacent and i not in visited:
            dfs_matrix(matrix, i, visited)
    
    return visited

n = int(input("Enter the number of nodes: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

start_node = int(input("Enter the starting node for DFS: "))

print("DFS traversal:")
dfs(matrix, start_node)
