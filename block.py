import copy

class Block:

    def __init__(self, x, y, pos, parent, board, x1=None,y1=None):
        self.x      = x
        self.y      = y
        self.pos    = pos  
        self.parent = parent
        self.board  = copy.deepcopy(board)
        self.x1     = x1
        self.y1     = y1
    
    def __lt__(self, block):
        return True
    def __gt__(self, block):
        return True

    def moveUp(self):
        tempBlock = Block(self.x, self.y, self.pos, self, self.board)

        if self.pos == "Standing_POS":
            tempBlock.y -= 2 
            tempBlock.pos = "Vertical_POS"

        elif tempBlock.pos == "Horizontal_POS":
            tempBlock.y -= 1
        
        elif tempBlock.pos == "Vertical_POS":
            tempBlock.y -= 1
            tempBlock.pos = "Standing_POS"
        
        return tempBlock 

    def moveDown(self):
        tempBlock = Block(self.x, self.y, self.pos, self, self.board)

        if tempBlock.pos == "Standing_POS":
            tempBlock.y += 1
            tempBlock.pos = "Vertical_POS"

        elif tempBlock.pos == "Horizontal_POS":
            tempBlock.y += 1

        elif tempBlock.pos == "Vertical_POS":
            tempBlock.y += 2
            tempBlock.pos = "Standing_POS"
        return tempBlock 

    def moveRight(self):
        tempBlock = Block(self.x, self.y, self.pos, self, self.board)
    
        if tempBlock.pos == "Standing_POS":
            tempBlock.x += 1
            tempBlock.pos = "Horizontal_POS"

        elif tempBlock.pos == "Horizontal_POS":
            tempBlock.x += 2
            tempBlock.pos = "Standing_POS"

        elif tempBlock.pos == "Vertical_POS":
             tempBlock.x += 1
        return tempBlock

    def moveLeft(self):
        tempBlock = Block(self.x, self.y, self.pos, self, self.board)

        if tempBlock.pos == "Standing_POS":
            tempBlock.pos = "Horizontal_POS"
            tempBlock.x -= 2

        elif tempBlock.pos == "Horizontal_POS":
            tempBlock.x -= 1
            tempBlock.pos = "Standing_POS"

        elif tempBlock.pos == "Vertical_POS":
            tempBlock.x -= 1

        return tempBlock 

    def printBlockPos(self):
        print("Block Position:",self.pos, "[X,Y]: [",self.x, self.y,"]")
    
    def printBoard(self):
        
        # local definition
        x   = self.x
        y   = self.y
        # x1  = self.x1
        # y1  = self.y1
        pos = self.pos
        board = self.board

        # let's go
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