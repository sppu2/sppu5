def prim(graph):
    mst = []
    visited = {list(graph.keys())[0]}

    while len(visited) < len(graph):
        min_edge = min((edge for node in visited for edge in graph[node] if edge[0] not in visited), key=lambda x: x[1])
        visited.add(min_edge[0])
        mst.append((min_edge[0], min_edge[1]))

    return mst

# Example usage:
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 5)],
    'C': [('A', 3), ('B', 4), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

min_spanning_tree = prim(graph)
print("Minimum Spanning Tree:")
for edge in min_spanning_tree:
    print(f'{edge[0]} - {edge[1]}')
