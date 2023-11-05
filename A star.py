import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic estimated cost from current node to goal node
        self.f = 0  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    open_set = []
    closed_set = set()
    start_node = Node(None, start)
    goal_node = Node(None, end)

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        for next_move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Possible moves: left, right, up, down
            node_position = (current_node.position[0] + next_move[0], current_node.position[1] + next_move[1])

            if (
                node_position[0] < 0
                or node_position[0] >= len(maze)
                or node_position[1] < 0
                or node_position[1] >= len(maze[0])
            ):
                continue

            if maze[node_position[0]][node_position[1]] == 1:
                continue

            new_node = Node(current_node, node_position)

            if new_node.position in closed_set:
                continue

            new_node.g = current_node.g + 1
            new_node.h = abs(new_node.position[0] - goal_node.position[0]) + abs(new_node.position[1] - goal_node.position[1])
            new_node.f = new_node.g + new_node.h

            for open_node in open_set:
                if new_node.position == open_node.position and new_node.g >= open_node.g:
                    break
            else:
                heapq.heappush(open_set, new_node)

    return None

def display_menu():
    print("\nMenu:")
    print("1. Set Start Position")
    print("2. Set Goal Position")
    print("3. Find Path (A*)")
    print("4. Quit")

def print_map_with_path(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                print("X", end=" ")
            elif maze[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

def main():
    maze = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = None
    goal = None

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            x = int(input("Enter the row for the start position: "))
            y = int(input("Enter the column for the start position: "))
            if maze[x][y] == 0:
                start = (x, y)
            else:
                print("Invalid start position. It should be a valid empty cell.")

        elif choice == '2':
            x = int(input("Enter the row for the goal position: "))
            y = int(input("Enter the column for the goal position: "))
            if maze[x][y] == 0:
                goal = (x, y)
            else:
                print("Invalid goal position. It should be a valid empty cell.")

        elif choice == '3':
            if start is not None and goal is not None:
                path = astar(maze, start, goal)
                if path:
                    print("Path found:")
                    print_map_with_path(maze, path)
                else:
                    print("No path found.")
            else:
                print("Please set both start and goal positions before finding the path.")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()








The provided Python code is an implementation of the A* search algorithm for finding the shortest path between a start and a goal position in a 2D grid-based maze. The code also includes a simple user interface for setting the start and goal positions, finding the path, and displaying the results. Let's break down the code and explain the concepts in detail:

1. **`Node` Class**:
   - This class represents a node in the A* search algorithm. Each node has attributes:
     - `parent`: The parent node in the search tree.
     - `position`: The position of the node in the 2D grid.
     - `g`: The cost from the start node to the current node.
     - `h`: The heuristic estimated cost from the current node to the goal node.
     - `f`: The total cost, where `f = g + h`.

   - The `__lt__(self, other)` method is defined to compare nodes based on their `f` values. This is used for priority queue management.

2. **`astar(maze, start, end)` Function**:
   - This function performs the A* search algorithm to find the shortest path from the `start` position to the `end` position in the given `maze`.

   - The `open_set` is a priority queue (implemented as a heap) that contains nodes to be explored.

   - The `closed_set` is a set that keeps track of visited positions.

   - The A* search algorithm explores nodes in the `open_set` until it finds the goal node. It expands nodes, calculates costs, and adds nodes to the `open_set` based on their `f` values.

   - The function returns the path from the start to the goal if a path is found. If no path exists, it returns `None`.

3. **`display_menu` Function**:
   - This function displays a user menu with options to set the start position, set the goal position, find the path (using A* search), or quit the program.

4. **`print_map_with_path` Function**:
   - This function prints the maze, marking the path with 'X', obstacles with '#', and empty cells with '.'.

5. **`main` Function**:
   - The main part of the code initializes a 2D `maze`, where `0` represents empty cells and `1` represents obstacles.

   - The `start` and `goal` positions are initially set to `None`.

   - The main loop presents a menu to the user for interaction. The user can set the start and goal positions, find the path using A* search, or exit the program.

   - When setting positions, the code checks if they are valid (i.e., empty cells in the maze).

   - If a path is found, it prints the path with 'X' markers on the grid. If no path is found, it informs the user.

   - The program continues to loop until the user chooses to exit.

In summary, this code provides an interactive way to apply the A* search algorithm to find the shortest path in a maze. Users can set the start and goal positions and visualize the pathfinding process using a user-friendly menu. It's a practical illustration of A* search in a 2D grid-based environment.