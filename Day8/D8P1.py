from input import realinput, testinput
import operator

input = realinput

input = input.splitlines()
input = list(map(operator.methodcaller("split", "|"), input))

counter = 0

for line in input:
    outputValues = line[1].split(' ')
    for val in outputValues:
        if (len(val) == 2) or (len(val) == 3) or (len(val) == 4) or (len(val) == 7):
            counter += 1

print(counter)