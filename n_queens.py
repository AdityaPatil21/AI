#def solveNQueens(n: int) -> list[list[str]]:#(n: int) -> list[list[str]] indicates that the solveNQueens function expects an integer n as input and returns a list of solutions, where each solution is represented as a list of strings.
def solveNQueens(n):
    col = set() #to keep track of occupied columns and diagonals this 3 var
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)

    res = [] #to store the solutions
    board = [["."] * n for i in range(n)] #initializes a 2D list board to represent the chessboard.

    def backtrack(r):#backtrack function is defined within the solveNQueens function. It is a recursive function that explores all possible placements of queens on the chessboard.
        # Base case: If all queens are placed (reached beyond the last row),
        # add the current board configuration to the result.
        if r == n: #initially 1st r=0
            copy = ["".join(row) for row in board]#" ".join(row) for row in board is a list comprehension that joins the elements of each row in the board list into a single string with a space separator.
            res.append(copy)
            return

        # For each column in the current row, try to place a queen.
        for c in range(n):#The loop iterates over the columns c in the current row r
            # Check if there is a conflict with the current column or diagonals.
            if c in col or (r + c) in posDiag or (r - c) in negDiag:#If c is present in the col set (indicating a queen is already placed in that column), or
                continue

            # Mark the current position as occupied by a queen.updates the sets, and moves to the next row by calling itself recursively.
            col.add(c)#adds c to the col set, indicating that the column c is occupied by a queen.
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q" #set Q indicate presence of queen in that pos

            # Move to the next row.
            backtrack(r + 1)

            # Remove the queen from the current position (backtracking).to explore another position
            col.remove(c) 
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "." #indicate empty pos

    # Start the backtracking from the first row (row index 0).
    backtrack(0)

    return res


ans = solveNQueens(4)

# Print the solutions
for board in ans:
    for row in board:
        print(row)
    print("--------------------------------------------")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #with matrix check
    def solveNQueens(n):
    if n <= 0:
        return []  # Return an empty list for invalid matrix sizes
    
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)

    return res

# Test the function with different matrix sizes
matrix_sizes = [1, 2, 3, 4, 5]
for size in matrix_sizes:
    print(f"Matrix size: {size}")
    solutions = solveNQueens(size)
    if solutions:
        for board in solutions:
            for row in board:
                print(row)
            print("----")
    else:
        print("No solution found.")
    print()

    
