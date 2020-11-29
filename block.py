import copy
# import sys
import queue as Q

class Block:

    def __init__(self, x, y, rot, parent, board, x1=None,y1=None):
        self.x      = x
        self.y      = y
        self.rot    = rot  
        self.parent = parent
        self.board  = copy.deepcopy(board)
        self.x1     = x1
        self.y1     = y1
    
    def __lt__(self, block):
        return True
    def __gt__(self, block):
        return True

    def move_up(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board)

        if self.rot == "STANDING":
            newBlock.y -= 2 
            newBlock.rot = "LAYING_Y"

        elif newBlock.rot == "LAYING_X":
            newBlock.y -= 1
        
        elif newBlock.rot == "LAYING_Y":
            newBlock.y -= 1
            newBlock.rot = "STANDING"
        
        return newBlock 

    def move_down(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board)

        if newBlock.rot == "STANDING":
            newBlock.y += 1
            newBlock.rot = "LAYING_Y"

        elif newBlock.rot == "LAYING_X":
            newBlock.y += 1

        elif newBlock.rot == "LAYING_Y":
            newBlock.y += 2
            newBlock.rot = "STANDING"
        return newBlock 

    def move_right(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board)
    
        if newBlock.rot == "STANDING":
            newBlock.x += 1
            newBlock.rot = "LAYING_X"

        elif newBlock.rot == "LAYING_X":
            newBlock.x += 2
            newBlock.rot = "STANDING"

        elif newBlock.rot == "LAYING_Y":
             newBlock.x += 1
        return newBlock

    def move_left(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board)

        if newBlock.rot == "STANDING":
            newBlock.rot = "LAYING_X"
            newBlock.x -= 2

        elif newBlock.rot == "LAYING_X":
            newBlock.x -= 1
            newBlock.rot = "STANDING"

        elif newBlock.rot == "LAYING_Y":
            newBlock.x -= 1

        return newBlock 

    # FOR CASE SPLIT
    def split_move_up(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBlock.y -= 1
        return newBlock 

    def split_move_down(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBlock.y += 1
        return newBlock 


    def split_move_left(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBlock.x -= 1
        return newBlock 


    def split_move_right(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBlock.x += 1
        return newBlock 

    def split1_move_up(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBlock.y1 -= 1
        return newBlock 

    def split1_move_down(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBlock.y1 += 1
        return newBlock 

    def split1_move_left(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBlock.x1 -= 1
        return newBlock 

    def split1_move_right(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1)
        newBlock.x1 += 1
        return newBlock 

    def disPlayPosition(self):
        if self.rot != "SPLIT":
            print(self.rot, self.x, self.y)
        else:
            print(self.rot, self.x, self.y, self.x1, self.y1)
    
    def disPlayBoard(self):
        
        # local definition
        x   = self.x
        y   = self.y
        x1  = self.x1
        y1  = self.y1
        rot = self.rot
        board = self.board

        # let's go

        if rot != "SPLIT":
            
            for i in range(len(board)): # for ROW
                print("",end='  ')
                for j in range(len(board[i])): # for COL in a ROW

                    if (i==y and j==x and rot=="STANDING") or \
                            ((i==y and j==x) or (i==y and j==x+1) and rot=="LAYING_X") or \
                            ((i==y and j==x) or (i==y+1 and j==x) and rot=="LAYING_Y"):

                        print("x",end=' ')

                    elif(board[i][j]==0):
                        print(" ",end=' ')
                    else:
                        print(board[i][j], end=' ')
                print("")
        else: # CASE SPLIT
            for i in range(len(board)): # for ROW
                print("",end='  ')
                for j in range(len(board[i])): # for COL

                    if (i==y and j==x) or (i==y1 and j==x1):
                        print("x",end=' ')

                    elif(board[i][j]==0):
                        print(" ",end=' ')
                    else:
                        print(board[i][j], end=' ')
                print("")
