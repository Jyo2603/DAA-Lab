def bfs(graph, start):
    visited = set()
    queue = [start]
    
    visited.add(start)
    
    while queue:
        node = queue.pop(0)
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {}
n = int(input("Enter the number of nodes: "))  
for _ in range(n):
    node = input("Enter node: ")  
    edges = input("Enter edges for node " + node + " (space-separated): ").split()
    graph[node] = [edge for edge in edges]

start_node = input("Enter the starting node for BFS: ")

print("BFS traversal:")
bfs(graph, start_node)
