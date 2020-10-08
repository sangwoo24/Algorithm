import itertools

def isIndexError(n,row,column):
    return True if row >= n or row < 0 or column >= n or column < 0 else False


def isValueExist(pyramid,row,column):
    return True if pyramid[row][column] != 0 else False

    
def solution(n):
    pyramid = [[0 for i in range(n)] for i in range(n)]
    pyramid[0][0] = 1
    cordinates = {1:[1,0], 2:[0,1], 3:[-1,-1]}
    dalPangE = 1
    
    direction = 1
    row = 1
    column = 0
    
    while True:
        while not isIndexError(n,row,column) and not isValueExist(pyramid,row,column):
            dalPangE += 1
            pyramid[row][column] = dalPangE      
            
            row = row + cordinates[direction][0]
            column = column + cordinates[direction][1]
    
        row -= cordinates[direction][0]
        column -= cordinates[direction][1]
        
        #direction 변경
        direction = 1 if direction == 3 else direction + 1
        
        row = row + cordinates[direction][0]
        column = column + cordinates[direction][1]
        if isIndexError(n,row,column) or isValueExist(pyramid,row,column):
            break

    for i in range(len(pyramid)):
        pyramid[i] = list(filter(lambda a: a != 0, pyramid[i]))
    return list(itertools.chain.from_iterable(pyramid))