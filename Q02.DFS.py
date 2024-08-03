def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

graph = {}
n = int(input("Enter the number of nodes: ")) 
for _ in range(n):
    node = input("Enter node: ")  
    edges = input("Enter edges for node " + node + " (space-separated): ").split()
    graph[node] = [edge for edge in edges]

start_node = input("Enter the starting node for DFS: ")

print("DFS traversal:")
dfs(graph, start_node)
