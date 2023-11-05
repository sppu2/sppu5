import heapq
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        distances = [float('inf')] * self.V
        distances[src] = 0

        min_heap = [(0, src)]

        while min_heap:
            dist_u, u = heapq.heappop(min_heap)

            if dist_u > distances[u]:
                continue

            for v, weight in self.graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(min_heap, (distances[v], v))

        return distances

def print_shortest_paths(distances, src):
    print("Shortest distances from source vertex", src)
    for i, dist in enumerate(distances):
        print(f"Vertex {i}: {dist}")

def main():
    while True:
        print("\nSingle-Source Shortest Path (Dijkstra's Algorithm) Menu:")
        print("1. Create Graph")
        print("2. Find Shortest Paths")
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
                src_vertex = int(input("Enter the source vertex: "))
                distances = g.dijkstra(src_vertex)
                print_shortest_paths(distances, src_vertex)
            else:
                print("Please create a graph first.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
















This Python code demonstrates the implementation of Dijkstra's algorithm for finding the single-source shortest paths in a weighted graph. It provides a user-friendly interface for creating a graph, finding the shortest paths from a specified source vertex, and displaying the results. Let's break down the code and explain the concepts in detail:

1. **`Graph` Class**:
   - The `Graph` class represents a weighted directed graph using an adjacency list.
   - It has the following key methods and attributes:
     - `__init__(self, vertices)`: Initializes the graph with the given number of vertices.
     - `add_edge(self, u, v, w)`: Adds an edge from vertex `u` to vertex `v` with weight `w`.
     - `dijkstra(self, src)`: Computes and returns the shortest distances from the source vertex `src` to all other vertices using Dijkstra's algorithm.

2. **`print_shortest_paths` Function**:
   - This function takes the calculated distances array and the source vertex as input and prints the shortest distances from the source vertex to all other vertices.

3. **`main` Function**:
   - The main part of the code presents a menu-driven interface for user interaction.
   - When the user chooses option 1, they can create a graph by specifying the number of vertices and entering edge information.
   - When the user chooses option 2, they can find the shortest paths from a specified source vertex. The code then calls the `dijkstra` method and prints the shortest distances.
   - The program continues to loop until the user chooses to exit.

In summary, this code provides a user-friendly way to work with Dijkstra's algorithm and visualize the shortest paths from a specified source vertex to all other vertices in a weighted graph. Users can create a graph, find shortest paths, and view the results using a menu-driven interface.

The code is well-structured and easy to understand, making it accessible for users to perform graph operations and observe the shortest path computations.