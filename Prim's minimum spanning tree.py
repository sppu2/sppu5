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
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

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

def print_mst(mst):
    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} - {v}: {w}")

def main():
    while True:
        print("\nMinimum Spanning Tree Menu:")
        print("1. Create Graph")
        print("2. Find MST (Kruskal's Algorithm)")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vertices = int(input("Enter the number of vertices: "))
            g = Graph(vertices)

            while True:
                edge_info = input("Enter an edge (u v w), or 'q' to finish: ")
                if edge_info == 'q':
                    break
                u, v, w = map(int, edge_info.split())
                g.add_edge(u, v, w)

        elif choice == "2":
            if 'g' in locals():
                mst = g.kruskal_mst()
                print_mst(mst)
            else:
                print("Please create a graph first.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


















or











# Prim's Algorithm in Python

INF = 9999999
# number of vertices in graph
N = 5
#creating graph by adjacency matrix method
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1














The provided Python code demonstrates how to find the Minimum Spanning Tree (MST) of a graph using Kruskal's algorithm. It includes a user interface to create a graph and find the MST. Let's break down the code and explain the concepts in detail:

1. **`Graph` Class**:
   - This class represents a graph and contains methods for adding edges, finding the MST using Kruskal's algorithm, and helper methods for union-find operations.

   - **`__init__(self, vertices)`**: The constructor initializes the graph with a given number of vertices (`self.V`). It maintains a list `self.graph` to store the edges as triples (source vertex, destination vertex, edge weight).

   - **`add_edge(self, u, v, w)`**: This method adds an edge to the graph, specifying the source vertex `u`, destination vertex `v`, and edge weight `w`. The edge is added as a triple to the `self.graph` list.

   - **`find(self, parent, i)`**: This helper method performs a find operation for the union-find data structure. It returns the root of the set to which the vertex `i` belongs.

   - **`union(self, parent, rank, x, y)`**: This helper method performs a union operation for the union-find data structure. It combines the sets to which vertices `x` and `y` belong. The `rank` list is used to keep track of the rank (depth) of trees in the forest.

   - **`kruskal_mst(self)`**: This method implements Kruskal's algorithm to find the MST. It sorts the edges in increasing order of their weights, initializes data structures for union-find, and iteratively selects edges that do not form cycles in the MST. It returns the MST as a list of edges.

2. **`print_mst` Function**:
   - This function takes the MST as input and prints the edges of the Minimum Spanning Tree.

3. **`main` Function**:
   - The main part of the code presents a menu-driven interface for user interaction.

   - When the user chooses option 1, they can create a graph by entering the number of vertices and adding edges with weights.

   - When the user chooses option 2, the code finds the MST using Kruskal's algorithm and prints the edges of the MST.

   - The program continues to loop until the user chooses to exit.

In summary, this code provides a user-friendly way to apply Kruskal's algorithm to find the Minimum Spanning Tree of a graph. Users can create a graph by adding edges with weights, find the MST, and visualize the results using a menu-driven interface. It's a practical implementation of a graph algorithm for solving MST problems.

The second part of the code (Prim's Algorithm) also finds the Minimum Spanning Tree of a graph using Prim's algorithm. It initializes a graph represented as an adjacency matrix, selects nodes, and finds the MST. The selected edges and their weights are printed.