from input import input

input = list(map(int, input.splitlines()))

# Part 1
increasingValuesP1 = 0
i = 1

for scan in input[i:]:
    if(input[i-1] < scan):
        increasingValuesP1 +=1
    i +=1

print(f'Part 1: {increasingValuesP1}')

# Part 2
increasingValuesP2 = 0
ii = 3
for scan in input[ii:]:
    if((input[ii-3] + input[ii-2] + input[ii-1]) < (input[ii-2] + input[ii-1] + scan)):
        increasingValuesP2 +=1
    ii +=1

print(f'Part 2: {increasingValuesP2}')