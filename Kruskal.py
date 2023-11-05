class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result

def display_menu():
    print("\nMenu:")
    print("1. Add an Edge")
    print("2. Find Minimum Spanning Tree (Kruskal's Algorithm)")
    print("3. Quit")

def add_edge(graph):
    u = int(input("Enter the source vertex: "))
    v = int(input("Enter the destination vertex: "))
    w = int(input("Enter the weight of the edge: "))
    graph.add_edge(u, v, w)
    print(f"Edge ({u}, {v}) with weight {w} added to the graph.")

def find_minimum_spanning_tree(graph):
    minimum_spanning_tree = graph.kruskal_mst()
    print("\nEdges in Minimum Spanning Tree:")
    for edge in minimum_spanning_tree:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_edge(g)
        elif choice == '2':
            find_minimum_spanning_tree(g)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    main()







The provided Python code implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a given graph. It also includes a user interface to add edges to the graph and find the MST. Let's break down the code and explain the concepts in detail:

1. **`Graph` Class**:
   - This class represents a graph and contains methods for adding edges, finding the MST using Kruskal's algorithm, and helper methods for union-find operations.

   - **`__init__(self, vertices)`**: The constructor initializes the graph with a given number of vertices (`self.V`). It maintains a list `self.graph` to store the edges as triples (source vertex, destination vertex, edge weight).

   - **`add_edge(self, u, v, w)`**: This method adds an edge to the graph, specifying the source vertex `u`, destination vertex `v`, and edge weight `w`. The edge is added as a triple to the `self.graph` list.

   - **`find(self, parent, i)`**: This helper method performs a find operation for the union-find data structure. It returns the root of the set to which the vertex `i` belongs.

   - **`union(self, parent, rank, x, y)`**: This helper method performs a union operation for the union-find data structure. It combines the sets to which vertices `x` and `y` belong. The `rank` list is used to keep track of the rank (depth) of trees in the forest.

   - **`kruskal_mst(self)`**: This method implements Kruskal's algorithm to find the MST. It sorts the edges in increasing order of their weights, initializes data structures for union-find, and iteratively selects edges that do not form cycles in the MST. It returns the MST as a list of edges.

2. **`display_menu` Function**:
   - This function displays a user menu with options to add an edge to the graph, find the MST using Kruskal's algorithm, or quit the program.

3. **`add_edge` Function**:
   - This function allows the user to input source vertex, destination vertex, and edge weight to add an edge to the graph.

4. **`find_minimum_spanning_tree` Function**:
   - This function calls the `kruskal_mst` method of the `Graph` object to find the MST and then prints the edges of the MST.

5. **`main` Function**:
   - The main part of the code initializes an instance of the `Graph` class (`g`) with the specified number of vertices.

   - It presents a menu to the user for interaction. The user can add edges to the graph, find the MST using Kruskal's algorithm, or exit the program.

   - When the user chooses to add an edge, they are prompted to enter the source vertex, destination vertex, and edge weight, and the edge is added to the graph.

   - When the user chooses to find the MST, the `kruskal_mst` method is called, and the edges of the MST are printed.

   - The program continues to loop until the user chooses to exit.

In summary, this code provides a user-friendly way to apply Kruskal's algorithm to find the Minimum Spanning Tree of a graph. Users can add edges, find the MST, and visualize the results using a menu-driven interface. It's a practical implementation of a graph algorithm for solving MST problems.