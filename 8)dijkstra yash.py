def dijkstra(graph, start):
    d, S, P = {v: float('inf') for v in graph}, {start}, {}
    d[start] = 0

    while S:
        v = min(S, key=d.get)
        S.discard(v)

        for u, w in graph[v].items():
            if d[v] + w < d[u]:
                d[u], P[u] = d[v] + w, v
                S.add(u)

    return d, P

# Example usage:
G = {
    'A': {'B': 2, 'D': 6},
    'B': {'A': 2, 'C': 3, 'D': 8, 'E': 5},
    'C': {'B': 3},
    'D': {'A': 6, 'B': 8, 'E': 9},
    'E': {'B': 5, 'D': 9}
}

start = 'A'
distances, parents = dijkstra(G, start)

for vertex, distance in distances.items():
    print(f'{start} -> {vertex}: {distance}')
