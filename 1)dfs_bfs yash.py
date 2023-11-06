# Depth first search (DFS) algorithm
def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)

    for nei in graph[node]:
        dfs(graph, nei, visited)

# Breadth first search (BFS) algorithm
def bfs(graph, node, visited):
    queue = []

    queue.append(node)
    visited.add(node)

    while queue:
        current = queue.pop(0)

        for nei in graph[current]:
            if nei not in visited:
                queue.append(nei)
                visited.add(nei)

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

visited = set()

# DFS
dfs(graph, 0, visited)
print("DFS:", visited)

# BFS
visited = set()
bfs(graph, 0, visited)
print("BFS:", visited)
