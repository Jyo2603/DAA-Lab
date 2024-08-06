def prims_algorithm(graph, start):
    mst, visited, edges = [], set(), [(0, start, None)]

    while edges:
        weight, u, v = min(edges)
        edges.remove((weight, u, v))

        if u not in visited:
            visited.add(u)
            if v is not None:
                mst.append((v, u, weight))
            edges.extend((w, v, u) for v, w in graph.get(u, []) if v not in visited)

    return mst

def create_graph():
    graph = {}
    for _ in range(int(input())):
        u, v, weight = input().split()
        graph.setdefault(u, []).append((v, int(weight)))
        graph.setdefault(v, []).append((u, int(weight)))
    return graph

graph = create_graph()
start_node = input()
if start_node in graph:
    mst = prims_algorithm(graph, start_node)
    for u, v, w in mst:
        print(f"{v} - {u} with weight {w}")
else:
    print("Starting node not found.")
