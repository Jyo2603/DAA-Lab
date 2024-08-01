def dfs(graph, start, visited=None):
    # Initialize the visited set if it's not provided
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(start)
    
    # Print the node (or process it as needed)
    print(start)

    # Recursively visit all the neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

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
start_node = input("Enter the starting node for DFS: ")

# Perform DFS and print the traversal
print("DFS traversal:")
dfs(graph, start_node)
