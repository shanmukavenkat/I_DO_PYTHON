def solve_n_queens(N):
    def is_safe(board, row, col):
        return all(board[i] not in (row, row + col - i, row - col + i) for i in range(col))

    def backtrack(board, col):
        if col >= N:
            return True
        for row in range(N):
            if is_safe(board, row, col):
                board[col] = row
                if backtrack(board, col + 1):
                    return True
        return False

    board = [-1] * N
    if not backtrack(board, 0):
        print("No solution exists.")
        return

    print("Solution exists and is as follows:")
    for row in board:
        print(" ".join("Q" if r == row else "*" for r in range(N)))

# Example usage
N = 4
solve_n_queens(N)
