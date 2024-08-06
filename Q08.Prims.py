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

def main():
    graph = {}
    for _ in range(int(input("Number of edges: "))):
        u, v, w = input("Edge (node1 node2 weight): ").split()
        w = int(w)
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))
    
    start = input("Starting node: ")
    if start in graph:
        mst = prims_algorithm(graph, start)
        for u, v, w in mst:
            print(f"{v} - {u} with weight {w}")
    else:
        print("Starting node not found.")

if __name__ == "__main__":
    main()
