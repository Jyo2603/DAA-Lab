def prims_algorithm(graph, start):
    mst, visited, min_edges = [], set(), [(0, start, None)]

    while min_edges:
        weight, u, v = min(min_edges, key=lambda x: x[0])
        min_edges.remove((weight, u, v))

        if u not in visited:
            visited.add(u)
            if v is not None:
                mst.append((v, u, weight))
            min_edges.extend((edge_weight, neighbor, u) for neighbor, edge_weight in graph[u] if neighbor not in visited)

    return mst

def create_graph():
    graph = {}
    for _ in range(int(input("Enter the number of edges: "))):
        u, v, weight = input("Enter edge (node1 node2 weight): ").split()
        weight = int(weight)
        graph.setdefault(u, []).append((v, weight))
        graph.setdefault(v, []).append((u, weight))
    return graph

# Example usage
graph = create_graph()
start_node = input("Enter the starting node: ")

if start_node in graph:
    mst = prims_algorithm(graph, start_node)
    print("Edges in the Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]} with weight {edge[2]}")
else:
    print("Starting node not found.")
