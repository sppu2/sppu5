MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def main():
    values = [3, 5, 6, 9, 1, 2, 0, -1]

    while True:
        print("Menu:")
        print("1. Find the optimal value")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))
        elif choice == 2:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

















The code you provided is an implementation of the minimax algorithm, which is commonly used in decision-making processes for two-player games, especially in scenarios with perfect information like chess, checkers, tic-tac-toe, etc. The goal of the minimax algorithm is to determine the best move for a player by considering the potential outcomes of each possible move.

Here's an explanation of the code:

1. `MAX` and `MIN` are constants defined with the values 1000 and -1000, respectively. These constants are used to represent positive and negative infinity, which are initial values for the best move of the maximizing and minimizing players, respectively.

2. `minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta)` is a recursive function that calculates the optimal value for a player given the current game state.

   - `depth` represents the current depth in the game tree, which limits the depth to which the algorithm will search.
   - `nodeIndex` is the index of the current node in the game tree.
   - `maximizingPlayer` is a boolean flag that indicates whether the current player is maximizing (True) or minimizing (False).
   - `values` is a list representing the values of the nodes in the game tree.
   - `alpha` and `beta` are parameters used for alpha-beta pruning, a technique to optimize the minimax algorithm by pruning branches of the tree that cannot affect the final result.

3. In the `minimax` function, if `depth` reaches 3 (which you can modify based on your game's complexity), the function returns the value of the current node, effectively terminating the recursion.

4. If the `maximizingPlayer` is True, the algorithm is trying to maximize the score. It initializes `best` to a very small value (`MIN`) and iterates through child nodes, calculating their values recursively. It updates the `best` value as the maximum of the current `best` and the value of the child node. Additionally, it keeps track of `alpha`, which represents the best value achievable by the maximizing player so far. If `beta` (the best value achievable by the minimizing player) becomes less than or equal to `alpha`, it breaks out of the loop.

5. If the `maximizingPlayer` is False, the algorithm is trying to minimize the score. It initializes `best` to a very large value (`MAX`) and follows a similar process, but this time it seeks to minimize the value.

6. In the `main` function, there is a simple menu system where you can choose to find the optimal value using the `minimax` function (option 1) or exit the program (option 2). The optimal value is calculated for a sample game tree with values provided in the `values` list.

7. The code executes the `main` function when run and allows the user to interact with the menu.

This code is a basic illustration of the minimax algorithm for decision-making in a simplified game scenario. In practice, you would adapt and extend it to suit the requirements of the specific game you're working on.