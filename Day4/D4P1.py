from input import input, testinput
from itertools import groupby

testinput = testinput.split('\n\n')
input = input.split('\n\n')


numbersCalled = input[0].split(',')

# Turn the boards into nested lists
boards = []
for board in input[1:]:
    newBoard = []
    board = board.splitlines()
    for line in board:
        line = line.split()
        newBoard.append(line)
    boards.append(newBoard)

# Mark all occurances of the called number on the given board
def markCalledNumber(boardNr, calledNumber):
    for lineNr, line in enumerate(boards[boardNr]):
        for colNr, number in enumerate(line):
            if (number == str(calledNumber)):
                boards[boardNr][lineNr][colNr] = 'X'

# Check if a given board has a bingo
def checkBingo(board):
    #check lines
    for line in board:
        if (all_equal(line)):
            return board

    #check columns
    for column in range(5):
        if (board[0][column] == board[1][column] == board[2][column] == board[3][column] == board[4][column]):
            return board

    return False

# Calculate final score
def calculateScore(boardNr, lastCalled):
    boardTotal = 0
    for line in boards[boardNr]:
        for number in line:
            if (number != 'X'):
                boardTotal += int(number)
    
    print(f'Board score: {boardTotal}')
    print(f'Last called number: {lastCalled}')
    print(f'Total score: {boardTotal * int(lastCalled)}')


# Helper function for checking bingo on board rows
def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

# Run the bingo game
def playBingo():
    for indx, calledNumber in enumerate(numbersCalled):
        print(f'Calling number: {calledNumber}')
        for boardNr, board in enumerate(boards):
            markCalledNumber(boardNr, calledNumber)
            if (checkBingo(boards[boardNr]) != False):
                print("BINGO!")
                for line in boards[boardNr]:
                    print(line)
                calculateScore(boardNr, calledNumber)
                return

playBingo()
