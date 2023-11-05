from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, start, visited):
        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start, visited):
        queue = []
        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node, end=' ')

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Take input for the graph
g = Graph()
n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
print("Enter edges as pairs (u v), one pair per line:")
for _ in range(m):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex for DFS and BFS: "))

visited_dfs = set()
visited_bfs = set()

print("\nDFS starting from vertex", start_vertex)
g.dfs(start_vertex, visited_dfs)

print("\nBFS starting from vertex", start_vertex)
g.bfs(start_vertex, visited_bfs)









The provided Python code is an implementation of graph traversal using Depth-First Search (DFS) and Breadth-First Search (BFS). It allows the user to input a graph, specify a starting vertex, and then visualize the traversal of the graph. Let's break down the code and explain the concepts in detail:

1. **`Graph` Class**:
   - This class is used to represent an undirected graph. It uses an adjacency list to store the graph's edges and vertices. The adjacency list is implemented using a `defaultdict` from the `collections` module, which is a dictionary with a default value of an empty list for each key.

   - **`__init__(self)`**: The constructor initializes an empty adjacency list to represent the graph.

   - **`add_edge(self, u, v)`**: This method adds an undirected edge between two vertices `u` and `v`. It does this by appending `v` to the list of neighbors of `u` and vice versa. This ensures that the graph is undirected.

   - **`dfs(self, start, visited)`**: This method performs Depth-First Search (DFS) starting from a specified vertex `start`. It uses a recursive approach to explore the graph. The `visited` parameter is a set that keeps track of visited vertices to avoid revisiting them.

   - **`bfs(self, start, visited)`**: This method performs Breadth-First Search (BFS) starting from a specified vertex `start`. It uses a queue to traverse the graph level by level, and the `visited` set keeps track of visited vertices.

2. **Graph Input**:
   - The code initializes an instance of the `Graph` class as `g`.

   - It takes user input for the number of vertices (`n`) and edges (`m`) in the graph.

   - The user is prompted to enter edges as pairs `(u, v)` one pair per line. For each pair, the `add_edge` method is called to add the undirected edge to the graph.

   - The user is then asked to specify the starting vertex for both DFS and BFS traversal.

3. **DFS (Depth-First Search)**:
   - DFS is a graph traversal algorithm that explores as far as possible along a branch before backtracking. The algorithm starts at the specified vertex and explores one branch as deeply as possible before backtracking.

   - The `dfs` method is called with the specified starting vertex. It recursively visits neighbors, marking them as visited in the `visited` set. The traversal path is printed to the console.

4. **BFS (Breadth-First Search)**:
   - BFS is a graph traversal algorithm that explores all the vertices at the current level before moving to the next level. It uses a queue to manage the order of vertex exploration.

   - The `bfs` method is called with the specified starting vertex. It uses a queue to manage the traversal order. The traversal path is printed to the console.

5. **User Interaction**:
   - The code provides a user-friendly menu where the user can choose to create a graph, specify a starting vertex, and perform both DFS and BFS traversals.

   - It checks for the existence of a graph object (`'g' in locals()`) before allowing traversal. If a graph hasn't been created, the user is prompted to create one first.

In summary, this code provides a practical implementation of graph traversal techniques (DFS and BFS) using an adjacency list representation. Users can input a graph, specify a starting vertex, and visualize the traversal process. It's a useful educational tool for understanding how these traversal algorithms work in practice.
