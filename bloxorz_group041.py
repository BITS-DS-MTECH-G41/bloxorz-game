#==================================================================================
# ACI Assignment 1 - Bloxorz Stage 1 Game by Uninformed (Depth First) search - DFS
#==================================================================================
# Contributors:
# -------------
#  Aditya Mehta (2019ad04031)
#  Ankit Gupta  (2019ad04026)
#  Hitesh Gupta (2019ad04027)
#==================================================================================

#Importing required libraries, project classes
import copy

# Below is the player block class specifying block properties and methods
class PlayerBlock:

    def __init__(self, x, y, pos, parent, board):
        self.x      = x
        self.y      = y
        self.pos    = pos  
        self.parent = parent
        self.board  = copy.deepcopy(board)

    def moveRight(self):
        tempBlock = PlayerBlock(self.x, self.y, self.pos, self, self.board)
    
        if tempBlock.pos == "Standing_POS":
            tempBlock.x = tempBlock.x + 1
            tempBlock.pos = "Horizontal_POS"
        elif tempBlock.pos == "Horizontal_POS":
            tempBlock.x = tempBlock.x + 2
            tempBlock.pos = "Standing_POS"
        elif tempBlock.pos == "Vertical_POS":
             tempBlock.x = tempBlock.x + 1
        return tempBlock

    def moveLeft(self):
        tempBlock = PlayerBlock(self.x, self.y, self.pos, self, self.board)

        if tempBlock.pos == "Standing_POS":
            tempBlock.pos = "Horizontal_POS"
            tempBlock.x = tempBlock.x - 2
        elif tempBlock.pos == "Horizontal_POS":
            tempBlock.x = tempBlock.x - 1
            tempBlock.pos = "Standing_POS"
        elif tempBlock.pos == "Vertical_POS":
            tempBlock.x = tempBlock.x - 1
        return tempBlock 

    def moveDown(self):
        tempBlock = PlayerBlock(self.x, self.y, self.pos, self, self.board)

        if tempBlock.pos == "Standing_POS":
            tempBlock.y = tempBlock.y + 1
            tempBlock.pos = "Vertical_POS"
        elif tempBlock.pos == "Horizontal_POS":
            tempBlock.y = tempBlock.y + 1
        elif tempBlock.pos == "Vertical_POS":
            tempBlock.y = tempBlock.y + 2
            tempBlock.pos = "Standing_POS"
        return tempBlock 

    def moveUp(self):
        tempBlock = PlayerBlock(self.x, self.y, self.pos, self, self.board)

        if self.pos == "Standing_POS":
            tempBlock.y = tempBlock.y - 2 
            tempBlock.pos = "Vertical_POS"
        elif tempBlock.pos == "Horizontal_POS":
            tempBlock.y = tempBlock.y - 1
        elif tempBlock.pos == "Vertical_POS":
            tempBlock.y = tempBlock.y - 1
            tempBlock.pos = "Standing_POS"        
        return tempBlock


    def printBoard(self):
        '''Prints the Board state'''        
        y   = self.y
        x   = self.x
        board = self.board
        pos = self.pos

        for i in range(len(board)): # for ROW
            print("",end='  ')
            for j in range(len(board[i])): # for COL in a ROW
                if (i==y and j==x and pos=="Standing_POS") or \
                        ((i==y and j==x) or (i==y and j==x+1) and pos=="Horizontal_POS") or \
                        ((i==y and j==x) or (i==y+1 and j==x) and pos=="Vertical_POS"):
                    print("x",end=' ')
                elif(board[i][j]==0):
                    print(" ",end=' ')
                else:
                    print(board[i][j], end=' ')
            print("")

    def printBlockPos(self):
        print("Block Position:",self.pos, "[X,Y]: [",self.x + 1, self.y + 1,"]")

# This method is to validate if the Block is in valid state 
def chkValidBlock(block):
    if chkFloor(block):           
        return True
    else:
        return False

# This method is to validate if the Block has reached GOAL state
def chkIfGoal(block):
    x = block.x
    y = block.y
    pos = block.pos
    board = block.board

    if pos == "Standing_POS" and  board[y][x] == 9:
        return True
    else:
        return False

# This method is to check if the position is already validated.
def chkVisited(block):
    for item in visitedStates:
        if item.x == block.x     and item.y == block.y and item.pos == block.pos and item.board == block.board:
            return True
    return False

def chkFloor(block):
    x = block.x
    y = block.y
    pos = block.pos
    board = block.board
    
    if x >= 0 and y >= 0 and y < MATRIX_X and x < MATRIX_Y and board[y][x] != 0:

        if pos == "Standing_POS":
            return True
        elif pos == "Vertical_POS":
            if y+1 < MATRIX_X and board[y+1][x] != 0 :
                return True
        elif pos == "Horizontal_POS":
            if x+1 < MATRIX_Y and board[y][x+1] != 0 :
                return True
    else:
        return False

# This method is to move and update the expandStack
def move(expandStack, block, flag):
    if chkValidBlock(block):
        if chkVisited(block):
            return None

        expandStack.append(block)
        visitedStates.append(block)
        return True 
    return False   

# This method is to print the success path
def printSuccessPath(block):
    
    print("\nHere is the final DFS Success path:")
    print("=====================================")
    
    successPath = [block]
    temp = block.parent
    
    while temp != None:
        newBlock = PlayerBlock(temp.x, temp.y, temp.pos, temp.parent, temp.board)
        successPath = [newBlock] + successPath
        
        temp = temp.parent
    
    step = 0
    for item in successPath:
        step += 1
        print("\nStep:", step, end=' ==> ')
        item.printBlockPos()
        print("========================================================")
        item.printBoard()

    print("\n")
    print("=======================================")
    print("Actual Steps Taken: ",step,"Steps...!!!")
    print("=======================================")
    
# Depth First Search algorithm implemented
def PlayStage1(block):

    expandStack = []
    visitedStates.append(block)

    expandStack.append(block)    
    generatedSteps = 0
    # print ("expandStack length is :", len(expandStack))
    while expandStack:
        currentBlockPos = expandStack.pop()
        if chkIfGoal(currentBlockPos):
            printSuccessPath(currentBlockPos)
            print("Total Steps generated:", generatedSteps, "steps")
            return True
        else:
            generatedSteps += 4

            move(expandStack, currentBlockPos.moveUp(), "up")
            move(expandStack, currentBlockPos.moveRight(), "right")
            move(expandStack, currentBlockPos.moveDown(), "down")
            move(expandStack, currentBlockPos.moveLeft(), "left")
    return False


if __name__ == "__main__":
    # Main code starts here...

    # Setting initial values of board and block position...
    visitedStates = []
    stage = '01'
    MATRIX_X = 6
    MATRIX_Y = 10
    xStart = 2
    yStart = 2
    sourceMap = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 1, 1, 9, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]
    boardState = []
    
    print("\nInitial Game MATRIX looks like this:")
    for item in sourceMap:
        print(item)
    print("\nStart at (",xStart, ",", yStart,")")
    print("======================================")
    block = PlayerBlock(xStart - 1, yStart - 1, "Standing_POS", None, sourceMap)

    PlayStage1(block)
    print("\n======== Completed successfully ==========")
