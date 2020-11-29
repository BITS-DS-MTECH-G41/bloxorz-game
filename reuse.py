def readMatrix(MATRIX_X,MATRIX_Y,xStart,yStart,sourceMap, boardState,fileMap):
    with open(fileMap) as f:
        MATRIX_X, MATRIX_Y, xStart, yStart = [int(x) for x in next(f).split()] # read first line
        sourceMap = []
        countMapLine = 1
        for line in f: # read map
            countMapLine += 1
            sourceMap.append([int(x) for x in line.split()])
            if countMapLine > MATRIX_X: break

        # read managedBoard
        boardState = []
        for line in f: # read boardState
            # 2 2 4 4 4 5
            boardState.append([int(x) for x in line.split()])

    print("\nInitial Game MATRIX looks like this:")
    for item in sourceMap:
        print(item)
    print("\nStart at (",xStart, ",", yStart,")")
    # print("Board State:")
    # for item in boardState:
        # print(item)
    print("======================================")
    return sourceMap, boardState
