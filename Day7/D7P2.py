import sys
from input import testInput, realInput

input = realInput
bestFuel = 0
lastFuel = sys.maxsize

# for every possible position
for x in range(max(input)+1):     
    # Move every position to x
    usedFuel = 0
    for crab in input:
        diff = abs(crab - x)
        if ( diff > 0 ):
            usedFuel += (diff ** 2 + diff) / 2 
    if (usedFuel < lastFuel):
        bestFuel = usedFuel
    lastFuel = usedFuel

print(int(bestFuel))