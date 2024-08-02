import heapq

def prims_algorithm(graph, start):
    mst, visited, min_edges = [], set(), [(0, start, None)]

    while min_edges:
        weight, u, v = heapq.heappop(min_edges)
        if u not in visited:
            visited.add(u)
            if v is not None:
                mst.append((v, u, weight))
            for neighbor, edge_weight in graph[u]:
                if neighbor not in visited:
                    heapq.heappush(min_edges, (edge_weight, neighbor, u))

    return mst

def create_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    nodes = input("Enter node names (space-separated): ").split()
    for node in nodes:
        graph[node] = []

    for _ in range(int(input("Enter the number of edges: "))):
        u, v, weight = input("Enter edge (node1 node2 weight): ").split()
        weight = int(weight)
        graph[u].append((v, weight))
        graph[v].append((u, weight))

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
