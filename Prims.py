def prims_algorithm(graph, start):
    """Prim's algorithm to find the Minimum Spanning Tree (MST)."""
    mst = []
    visited = set()
    min_edges = [(0, start, None)]  # Start with an arbitrary node

    while min_edges:
        weight, u, v = min(min_edges)
        min_edges.remove((weight, u, v))

        if u not in visited:
            visited.add(u)
            if v is not None:
                mst.append((v, u, weight))
            for neighbor, edge_weight in graph[u]:
                if neighbor not in visited:
                    min_edges.append((edge_weight, neighbor, u))

    return mst

def create_graph():
    """Create a graph from user input."""
    graph = {}
    n = int(input("Enter the number of nodes: "))
    nodes = input("Enter node names (space-separated): ").split()
    for node in nodes:
        graph[node] = []

    m = int(input("Enter the number of edges: "))
    for _ in range(m):
        u, v, weight = input("Enter edge (node1 node2 weight): ").split()
        weight = int(weight)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    return graph

# Example usage
graph = create_graph()
start_node = input("Enter the starting node: ")

if start_node not in graph:
    print("Starting node not found.")
else:
    mst = prims_algorithm(graph, start_node)
    print("Edges in the Minimum Spanning Tree:")
    for edge in mst:
        print("{} - {} with weight {}".format(edge[0], edge[1], edge[2]))
