def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        return None

    solutions = []
    for row in board:
        solutions.append(["Q" if cell == 1 else "." for cell in row])

    return solutions

def print_solution(solution):
    if solution is None:
        print("No solution exists.")
    else:
        for row in solution:
            print(" ".join(row))

def main():
    while True:
        print("\nN-Queens Problem Menu:")
        print("1. Solve N-Queens")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter the board size (N): "))
            solution = solve_n_queens(n)
            print("\nSolution:")
            print_solution(solution)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


















The provided code is an implementation of the N-Queens problem using a backtracking algorithm. The N-Queens problem is a classic puzzle that asks you to place N chess queens on an NxN chessboard so that no two queens threaten each other. Here's an explanation of the code:

1. `is_safe(board, row, col, n)` is a function that checks whether it's safe to place a queen on a particular square of the chessboard.
   - It checks if there is a queen in the same row, in which case it returns `False`.
   - It checks if there is a queen in the diagonal from the current square to the top-left, returning `False` if found.
   - It checks if there is a queen in the diagonal from the current square to the bottom-left, returning `False` if found.
   - If no conflicts are found, it returns `True`, indicating it's safe to place a queen.

2. `solve_n_queens_util(board, col, n)` is a recursive function that solves the N-Queens problem.
   - If `col` is greater than or equal to `n`, it means all queens are placed successfully, and it returns `True`.
   - It iterates through rows and tries to place a queen in each row.
   - If it can place a queen safely, it recurs to place the next queen in the next column.
   - If a solution is found, it returns `True`. If not, it backtracks by changing the placement of queens.

3. `solve_n_queens(n)` is the main function that initializes the chessboard and calls `solve_n_queens_util` to find a solution.
   - It creates an empty chessboard of size `n` x `n`.
   - It calls `solve_n_queens_util` to find a solution. If a solution exists, it returns the board configuration; otherwise, it returns `None`.

4. `print_solution(solution)` is a function that prints the board configuration if a solution is found, or a message indicating that no solution exists.
   - It checks if the `solution` is `None`. If so, it prints "No solution exists."
   - If a solution exists, it iterates through the board and prints it in a human-readable format, using "Q" to represent queens and "." for empty squares.

5. In the `main` function, there's a simple menu system that allows the user to choose to solve the N-Queens problem (option 1) for a specified board size or exit the program (option 2).

6. The code executes the `main` function when run and allows the user to interact with the menu. The user can input the board size, and the program will attempt to find a solution and display it or report that no solution exists.

This code demonstrates a classic example of a backtracking algorithm used to solve a combinatorial problem, such as the N-Queens problem.