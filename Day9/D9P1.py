from typing import Iterable
from input import testinput, realinput

input = realinput

heightmap = input.splitlines()

def checkNeighbors(row, item):
    val = heightmap[row][item]
    isLowPoint = True
    if (row-1 >= 0):
        if ( heightmap[row-1][item] <= val ):
            isLowPoint = False
    else:
        pass    
    try:
        if ( heightmap[row+1][item] <= val ):
            isLowPoint = False
    except:
        pass    
    
    if (item-1 >= 0):
        if ( heightmap[row][item-1] <= val ):
            isLowPoint = False
    else:
        pass    

    try:
        if ( heightmap[row][item+1] <= val ):
            isLowPoint = False
    except:
        pass    
    
    if (isLowPoint):
        return int(val) + 1
    else: 
        return 0

score = 0

for rowIndex, row in enumerate(heightmap):
    for itemIndex, item in enumerate(row):
        score += checkNeighbors(rowIndex, itemIndex)

print(score)

    

