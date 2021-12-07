from input import realInput, testInput
from Day import Day

input = realInput
initTimeList = [0,0,0,0,0,0,0,0,0]

for fish in input:
    initTimeList[fish] += 1

def runSimulation(amountOfDays, startingList):
    days = []
    days.append(Day(startingList))
    for i in range(amountOfDays):
        days.append(days[i].newDay())
    return days

# Part 1 answer
p1Days = runSimulation(80, initTimeList)
print(f'Part 1: {p1Days[-1].getTotal()}')

# Part 2 answer
p2Days = runSimulation(256, initTimeList)
print(f'Part 2: {p2Days[-1].getTotal()}')    