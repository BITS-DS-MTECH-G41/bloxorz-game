# -*- coding: utf-8 -*- 
# ACI Assignment 1 - Bloxorz Stage 1 Game by DFS search
# Author: Aditya Mehta, Ankit Gupta and Hitesh Gupta

import copy
import sys
import queue as Q
from reuse import readMatrix
from block import Block    


# chkValidBlock
def chkValidBlock(block):
    
    if chkFloor(block):           
        return True
    else:
        return False


def chkFloor(block):
    x = block.x
    y = block.y
    pos = block.pos
    board = block.board
    
    if x >= 0 and y >= 0 and \
            y < MATRIX_X and x < MATRIX_Y and \
            board[y][x] != 0:

        if pos == "STANDING":
            return True
        elif pos == "LAYING_Y":
            if y+1 < MATRIX_X and board[y+1][x] != 0 :
                return True
        elif pos == "LAYING_X":
            if x+1 < MATRIX_Y and board[y][x+1] != 0 :
                return True
    else:
        return False


def chkIfGoal(block):
    x = block.x
    y = block.y
    pos = block.pos
    board = block.board

    if pos == "STANDING" and  \
        board[y][x] == 9:
        return True
    else:
        return False


def chkVisited(block):
    for item in passState:
        if item.x == block.x     and item.y == block.y and \
            item.pos == block.pos and item.board == block.board:
            return True
    return False

def move(Stack, block, flag):
    if chkValidBlock(block):
        if chkVisited(block):
            return None

        Stack.append(block)
        passState.append(block)
        return True 
    return False   

def printSuccessPath(block):
    
    print("\nHere is the final DFS Success path:")
    print("==================================")
    
    successRoad = [block]
    temp = block.parent
    
    while temp != None:
        newBlock = Block(temp.x, temp.y, \
            temp.pos, temp.parent, temp.board)
        successRoad = [newBlock] + successRoad
        
        temp = temp.parent
    
    step = 0
    for item in successRoad:
        step += 1
        print("\nStep:", step, end=' ==> ')
        item.printBlockPos()
        print("=====================================================")
        item.printBoard()

    print("Actual Steps Taken: ",step,"Steps...!!!")
    
# DFS search algorithm
def DFS(block):

    # board = block.board
    Stack = []
    Stack.append(block)
    passState.append(block)
    
    virtualStep = 0
    print ("Stack length is :", len(Stack))
    while Stack:
        current = Stack.pop()
        # current.printBlockPos()
        # current.printBoard()
        if chkIfGoal(current):
            printSuccessPath(current)
            print("Steps Taken:", virtualStep, "Total Explored steps")
            print("Completed successfully")
            return True
        else:
            virtualStep += 4

            move(Stack,current.moveUp(), "up")
            move(Stack,current.moveRight(), "right")
            move(Stack,current.moveDown(), "down")
            move(Stack,current.moveLeft(), "left")

    return False


if __name__ == "__main__":
    # Main code starts here...

    #Setting initial values of board and block position...
    passState = []
    stage = '01'
    MATRIX_X = 6
    MATRIX_Y = 10
    xStart = 2
    yStart = 2
    sourceMap = []
    boardState = []

    sourceMap, boardState = readMatrix(MATRIX_X,MATRIX_Y,xStart,yStart,sourceMap, boardState, 'stage01.txt')
    block = Block(xStart, yStart, "STANDING", None, sourceMap)

    DFS(block)