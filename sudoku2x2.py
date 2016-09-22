import random
board = []

def initBoard():
    global board
    board=[[0 for i in range(4)] for j in range(4)]
    

def addRow(aList, rowIndex):
    j=0
    while j!=4:
        board[rowIndex][j] = aList[j]
        j+=1

def delRow(rowIndex):
    for j in range(0,4):
        board[rowIndex][j] = 0

def checkBoxesInRow(n):
    startRow = n*2
    for k in range (2):
        elemSet = set()
        startCol = k*2    
        for i in range(startRow, startRow+2):
            for j in range(startCol,startCol+2):
                elemSet.add(board[i][j])             
        if (len(elemSet) != 4):
            return False
    return True

def generateRow(i):
    
        candidate = [x for x in range(1,5)]
        random.shuffle(candidate)
        addRow(candidate, i)
        if not isRowCompatible(i):
            delRow(i)
            generateRow(i)
        
    
def createPuzzle():
    initBoard()
    for i in range(4):
        generateRow(i)
    removestuff() 
    for x in board:
        print (x)
        print ('\n')

def isRowCompatible(rowIndex):
    for i in range (rowIndex):
        for j in range (4):
            if (board[i][j] == board[rowIndex][j]):
                return False
    if (rowIndex == 1):
        return checkBoxesInRow(0)
    if (rowIndex == 3):
        return checkBoxesInRow(1)
    #if (rowIndex == 8):
     #   return checkBoxesInRow(2)
    return True
def removestuff():
    for i in range (9):
        (x,y)=(random.randint(0,3),random.randint(0,3))
        board[x][y]="_"

createPuzzle()

            
    
        
