import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w  # If the graph is undirected

    def dijkstra(self, src):
        visited = [False] * self.V
        distance = [sys.maxsize] * self.V
        distance[src] = 0

        for _ in range(self.V):
            u = self.min_distance(distance, visited)
            visited[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and visited[v] is False
                    and distance[v] > distance[u] + self.graph[u][v]
                ):
                    distance[v] = distance[u] + self.graph[u][v]

        self.print_solution(distance)

    def min_distance(self, distance, visited):
        min_dist = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if distance[v] < min_dist and not visited[v]:
                min_dist = distance[v]
                min_index = v

        return min_index

    def print_solution(self, distance):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t {distance[node]}")


def display_menu():
    print("\nMenu:")
    print("1. Add an Edge")
    print("2. Find Shortest Paths (Dijkstra's Algorithm)")
    print("3. Quit")

def add_edge(graph):
    u = int(input("Enter the source vertex: "))
    v = int(input("Enter the destination vertex: "))
    w = int(input("Enter the weight of the edge: "))
    graph.add_edge(u, v, w)
    print(f"Edge ({u}, {v}) with weight {w} added to the graph.")

def find_shortest_paths(graph):
    source = int(input("Enter the source vertex: "))
    graph.dijkstra(source)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_edge(g)
        elif choice == '2':
            find_shortest_paths(g)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    main()
    





The provided Python code implements Dijkstra's algorithm for finding the shortest path from a source vertex to all other vertices in a weighted graph. The code also includes a simple user interface to add edges to the graph and find the shortest paths using Dijkstra's algorithm. Let's break down the code and explain the concepts in detail:

1. **`Graph` Class**:
   - This class represents a weighted graph and contains methods for adding edges, performing Dijkstra's algorithm, and printing the results.

   - **`__init__(self, vertices)`**: The constructor initializes the graph with a given number of vertices (`self.V`). It creates an adjacency matrix to represent the graph, where `self.graph` is a 2D array of size `vertices x vertices`, and all elements are initially set to 0 (no edges).

   - **`add_edge(self, u, v, w)`**: This method adds a directed edge from vertex `u` to vertex `v` with a given weight `w`. It updates the adjacency matrix with the weight of the edge and sets the corresponding element to `w`. If the graph is undirected, it also updates the reverse direction with the same weight.

   - **`dijkstra(self, src)`**: This method performs Dijkstra's algorithm to find the shortest paths from the source vertex `src` to all other vertices. It initializes data structures for tracking visited vertices and the shortest distances. Then, it iteratively selects the vertex with the shortest distance and updates the distances to its neighbors if a shorter path is found. It prints the shortest distances when the algorithm completes.

   - **`min_distance(self, distance, visited)`**: This method finds the vertex with the minimum distance among unvisited vertices. It is used within the Dijkstra's algorithm.

   - **`print_solution(self, distance)`**: This method prints the shortest distances from the source vertex to all other vertices in a tabular format.

2. **`display_menu` Function**:
   - This function displays a user menu with options to add an edge to the graph, find the shortest paths using Dijkstra's algorithm, or quit the program.

3. **`add_edge` Function**:
   - This function allows the user to input source vertex, destination vertex, and edge weight to add an edge to the graph.

4. **`find_shortest_paths` Function**:
   - This function allows the user to specify a source vertex and then calls the `dijkstra` method of the `Graph` object to find and print the shortest paths from the source vertex to all other vertices.

5. **`main` Function**:
   - The main part of the code initializes an instance of the `Graph` class (`g`) with the specified number of vertices.

   - It presents a menu to the user for interaction. The user can add edges to the graph, find shortest paths, or exit the program.

   - The program continues to loop until the user chooses to exit.

In summary, this code provides a user-friendly way to apply Dijkstra's algorithm to find the shortest paths in a weighted graph. Users can add edges, specify a source vertex, and visualize the shortest paths using a simple menu-driven interface. It's a practical illustration of Dijkstra's algorithm for solving graph-related problems.
