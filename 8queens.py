board = []
size = 4

def danger(row, col):
    """ Return if there is a danger by placing queen in
        a given row, col
    """
    for (i, j) in board:
        if row == i: return True
        if col == j: return True
        if abs(row - i) == abs(col - j): return True

    return False
    
def placequeen(row):
    if row > size:
        print board
    else:
        for col in range(1, size + 1):
            if not danger(row, col):
                board.append((row, col))
                print ("1",row,col,board)
                placequeen(row + 1)
                print ("2",row,col,board)
                board.remove((row,col))
                print ("3",row,col,board)

if __name__ == "__main__":
    placequeen(1)
