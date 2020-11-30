def readBoard(MATRIX_X,MATRIX_Y,xStart,yStart,sourceMap, boardState,stgFile):
    with open(stgFile) as f:
        sourceMap = []
        countMapLine = 1
        for line in f: 
            countMapLine += 1
            sourceMap.append([int(x) for x in line.split()])
            if countMapLine > MATRIX_X: break

        # read Board state
        boardState = []
        for line in f: # read boardState
            boardState.append([int(x) for x in line.split()])

    print("\nInitial Game MATRIX looks like this:")
    for item in sourceMap:
        print(item)
    print("\nStart at (",xStart, ",", yStart,")")
    print("======================================")
    return sourceMap, boardState
