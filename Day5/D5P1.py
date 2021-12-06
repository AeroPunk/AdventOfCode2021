from input import testinput, realInput
import numpy as np

input = realInput
input = input.splitlines()

# X     -   Format input into list of dictionaries -> [[x1: 1, y1: 2, x2: 3, y2: 4]]
# X     -   Filter out diagonal lines for P1
# X     -   Determine max size of the grid
# X     -   Build empty grid
# X     -   Find a way to get all coordinates between two points
# X     -   Fill all coordinates

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
    for x in range(gridSize[1]+1):
        grid.append(np.zeros(gridSize[0]+1, dtype=int))
    return grid

def getPositionsToUpdate(instruction):
    positions = []

    x1 = instruction.get("x1") 
    x2 = instruction.get("x2")
    y1 = instruction.get("y1")
    y2 = instruction.get("y2")

    highX = max(x1, x2)
    lowX = min(x1, x2)
    highY = max(y1, y2)
    lowY = min(y1, y2)

    # Vertical line (Y-direction)
    if ( x1 == x2 ):
        i = lowY
        while (i <= highY):
            positions.append([x1, i])
            i += 1
    # Horizontal line (X-direction)
    elif ( y1 == y2 ):
        i = lowX
        while (i <= highX):
            positions.append([i, y1])
            i += 1
    return positions

def updateGrid( positionsToUpdate ):
    for coordinate in positionsToUpdate:
        grid[coordinate[1]][coordinate[0]] += 1

def getAnswer(grid):
    counter = 0
    for line in grid:
        for position in line:
            if position > 1:
                counter += 1
    return counter

# Run the program

filtered = filterDiagonals(formatInput(input))
grid = buildGrid(determineGridSize(filtered))

for instruction in filtered:
    updateGrid( getPositionsToUpdate(instruction) )

print(getAnswer(grid))