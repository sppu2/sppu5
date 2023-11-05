class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_safe(self, v, colour, c):
        for i in range(self.vertices):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graph_colouring_util(self, m, colour, v):
        if v == self.vertices:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, colour, c):
                colour[v] = c
                if self.graph_colouring_util(m, colour, v + 1):
                    return True
                colour[v] = 0

    def graph_colouring(self, m):
        colour = [0] * self.vertices
        if not self.graph_colouring_util(m, colour, 0):
            return False

        print("Solution exists: Following are the assigned colors:")
        for c in colour:
            print(c, end=" ")
        return True


def create_graph():
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    for i in range(vertices):
        for j in range(vertices):
            g.graph[i][j] = int(input(f"Is vertex {i} adjacent to vertex {j}? (1/0): "))

    return g


def main():
    while True:
        print("\nGraph Coloring Problem Menu:")
        print("1. Create a graph")
        print("2. Color the graph")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            g = create_graph()
        elif choice == 2:
            if 'g' in locals():
                m = int(input("Enter the number of colors: "))
                g.graph_colouring(m)
            else:
                print("Please create a graph first.")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
















The provided code is an implementation of the graph coloring problem using backtracking. The objective is to assign colors to vertices of a graph in such a way that no two adjacent vertices share the same color. Here's an explanation of the code:

1. `Graph` is a class that represents a graph and contains methods for graph coloring:

   - The `__init__` method initializes the graph with a given number of vertices, creating an adjacency matrix to represent the graph. The matrix is initialized with zeros, indicating no edges between vertices.

   - The `is_safe` method checks if it's safe to color a vertex `v` with color `c`. It examines adjacent vertices to ensure that no adjacent vertices have the same color.

   - The `graph_colouring_util` method is a recursive function used to find a valid coloring for the graph. It assigns colors to vertices one by one, backtracking when necessary to explore different color assignments.

   - The `graph_colouring` method is the entry point for solving the graph coloring problem. It initializes an array `colour` to store the assigned colors. If a valid coloring is found, it prints the result and returns `True`. If no valid coloring exists, it returns `False`.

2. `create_graph` is a function that prompts the user to input the number of vertices and the adjacency matrix of the graph. It creates an instance of the `Graph` class and returns it.

3. In the `main` function, there's a menu system that allows the user to create a graph, color the graph, or exit the program.

   - Option 1 (`Create a graph`) allows the user to input the graph's number of vertices and its adjacency matrix. The graph is created using the `create_graph` function.

   - Option 2 (`Color the graph`) allows the user to specify the number of colors and attempt to find a valid coloring for the graph using the `graph_colouring` method.

   - Option 3 (`Exit`) terminates the program.

4. The code checks for the existence of a graph object before allowing the user to color it. If a graph has not been created (`'g'` is not in local variables), it prompts the user to create a graph first.

5. The code executes the `main` function when run, and it provides a user-friendly menu for creating a graph, coloring the graph, or exiting the program.

This code demonstrates a basic implementation of graph coloring using a backtracking algorithm and allows users to interact with it through a simple menu system. Users can create graphs and find valid colorings for those graphs using a specified number of colors.