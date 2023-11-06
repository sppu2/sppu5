#SS
def ss(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Input from the user
n = input("Enter a list of numbers separated by spaces: ")
a = [int(x) for x in n.split()]

ss(a)

print("Sorted list: ", a)

#MST
def kruskal_mst(graph):
    graph.sort(key=lambda x: x[2])
    parent = list(range(max(max(edge[:2]) for edge in graph) + 1))
    mst = []

    def find_parent(node):
        return node if parent[node] == node else find_parent(parent[node])

    for edge in graph:
        src, dest, weight = edge
        src_parent, dest_parent = map(find_parent, (src, dest))
        if src_parent != dest_parent:
            mst.append(edge)
            parent[src_parent] = dest_parent

    return mst

# Example usage:
graph = [(0, 1, 2), (0, 2, 4), (1, 2, 3), (1, 3, 5), (2, 3, 1)]
minimum_spanning_tree = kruskal_mst(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)






