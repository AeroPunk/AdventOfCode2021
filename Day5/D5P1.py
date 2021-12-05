from input import testinput, realInput
from datetime import datetime
import numpy as np

input = testinput
input = input.splitlines()

# --------- v1 Solution
# X     -   Format input into list of dictionaries -> [[x1: 1, y1: 2, x2: 3, y2: 4]]
# X     -   Filter out diagonal lines for P1
# X     -   Determine max size of the grid
# X     -   Build empty grid
#       -   Find a way to get all coordinates between two points
#       -   Fill all coordinates

def formatInput(inputList):
    result = []
    for line in inputList:
        old, new = line.split(' -> ')
        x1, y1 = old.split(',')
        x2, y2 = new.split(',')
        coordsDict = {
            "x1": int(x1),
            "y1": int(y1),
            "x2": int(x2),
            "y2": int(y2)
        }
        result.append(coordsDict)
    return result

def filterDiagonals(formattedList):
    result = []
    for line in formattedList:
        if ( line.get("x1") == line.get("x2") ) or ( line.get("y1") == line.get("y2") ):
            result.append(line)
    return result

def determineGridSize(input):
    maxX = 0
    maxY = 0
    for line in input:
        maxX = max(maxX, line.get('x1'), line.get('x2'))
        maxY = max(maxY, line.get('y1'), line.get('y2'))
    return [maxX, maxY]

def buildGrid(gridSize):
    grid = []
    for x in range(gridSize[1]):
        grid.append(np.zeros(gridSize[0], dtype=int))
    return grid

def getPositionsToUpdate(instruction):
    positions = []
    # Vertical line (Y-direction)
    if ( instruction.get("x1") == instruction.get("x2") ):
        pass
    # Horizontal line (X-direction)
    elif ( instruction.get("y1") == instruction.get("y2") ):
        pass
    # Diagonal line
    else:
        pass
    return positions

def updateGrid(grid, PositionsToUpdate):
    pass

# Run the program

before = datetime.now()
print(before)

filtered = filterDiagonals(formatInput(input))
grid = buildGrid(determineGridSize(filtered))

after = datetime.now()
print(after)

