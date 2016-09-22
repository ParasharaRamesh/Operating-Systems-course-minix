import copy
def solve(n):
    #prepare a board
    board = [[0 for x in range(n)] for x in range(n)]
    
    #set initial positions
    solutions = place_queen(board, 0, 0, [])
    #solutions = place_queen_iterative(n)

    print solutions

def place_queen(board, row, column, solutions):
    """place a queen that satisfies all the conditions"""
    while True: # loop unconditionally
        if len(board) in (row, column): # out of bounds, so we'll backtrack
            if row == 0:   # base case, can't backtrack, so return solutions
                return solutions
            elif row == len(board): # found a solution, so add it to our list
                solutions.append(copy.deepcopy(board)) # copy, since we mutate board

            for c in range(len(board)): # do the backtracking
                if board[row-1][c] == 1:
                    #remove this queen
                    board[row-1][c] = 0
                    #go back to the previous row and start from the next column
                    return place_queen(board, row-1, c+1, solutions)

        if is_safe(board, row, column):
            #place a queen
            board[row][column] = 1
            #place the next queen with an updated board
            return place_queen(board, row+1, 0, solutions)

        column += 1

def place_queen_iterative(n):
    board = [[0 for x in range(n)] for x in range(n)]
    solutions = []
    row = column = 0

    while True: # loop unconditionally
        if len(board) in (row, column):
            if row == 0:
                return solutions
            elif row == len(board):
                solutions.append(copy.deepcopy(board))

            for c in range(len(board)):
                if board[row-1][c] == 1:
                    board[row-1][c] = 0

                    row -= 1     # directly change row and column, rather than recursing
                    column = c+1
                    break        # break out of the for loop (not the while)

        elif is_safe(board, row, column):   # need "elif" here
            board[row][column] = 1

            row += 1      # directly update row and column
            column = 0

        else:             # need "else" here
            column += 1   # directly increment column value

def is_safe(board, row, column):
    """ if no other queens threaten a queen at (row, queen) return True """
    queens = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 1:
                queen = (r,c)
                queens.append(queen)
    for queen in queens:
        qr, qc = queen
        #check if the pos is in the same column or row
        if row == qr or column == qc:
            return False
        #check diagonals
        if (row + column) == (qr+qc) or (column-row) == (qc-qr):
            return False
    return True

solve(4)
