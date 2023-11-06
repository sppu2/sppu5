#heuristic = heu

class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from the start node to this node
        self.h = h  # heuristic estimate to the goal
        self.f = g + h  # Total cost (g + h)


def astar(start, goal, heu):
    open_list = [Node(start, None, 0, heu(start, goal))]
    closed_list = set()


    while open_list:
        current = min(open_list, key=lambda node: node.f)
        if current.state == goal:
            return current


        open_list.remove(current)
        closed_list.add(current.state)


        for nei in get_neis(current.state):
            if nei in closed_list:
                continue


            g = current.g + 1
            h = heu(nei, goal)
            new_node = Node(nei, current, g, h)


            if any(node.state == nei and node.f > new_node.f for node in open_list):
                continue


            open_list.append(new_node)


    return None


def get_neis(state):
    # Return a list of all possible next states from the given state.
    return [(state[0] + 1, state[1]), (state[0] - 1, state[1]), (state[0], state[1] + 1), (state[0], state[1] - 1)]


def heu(state, goal):
    # Estimate the cost of reaching the goal state from the given state.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def main():
    start = (0, 0)
    goal = (5, 5)


    result = astar(start, goal, heu)
    if result is not None:
        path = []
        while result is not None:
            path.insert(0, result.state)
            result = result.parent
        print("Path found:", path)
    else:
        print("No path found.")


if __name__ == "__main__":
    main()




