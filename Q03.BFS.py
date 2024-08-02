def bfs(graph, start):
    # Initialize the visited set and the queue
    visited = set()
    queue = [start]
    
    # Mark the starting node as visited
    visited.add(start)
    
    while queue:
        # Dequeue a node and print it (or process it as needed)
        node = queue.pop(0)
        print(node)
        
        # Visit all unvisited neighbors and enqueue them
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Input for the graph
graph = {}
n = int(input("Enter the number of nodes: "))  # Number of nodes in the graph
for _ in range(n):
    node = input("Enter node: ")  # Node name
    # Input edges as space-separated values and split them into a list
    edges = input("Enter edges for node " + node + " (space-separated): ").split()
    # Add the node and its edges to the graph dictionary
    graph[node] = [edge for edge in edges]

# Input for the starting node
start_node = input("Enter the starting node for BFS: ")

# Perform BFS and print the traversal
print("BFS traversal:")
bfs(graph, start_node)
