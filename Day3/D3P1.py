from input import input

input = input.splitlines()

length = len(input)
positions = [0] * len(input[0])

for line in input:
    for pos, val in enumerate(line):
        if (val == "1"):
            positions[pos] += 1

gamma = ""
epsilon = ""
for pos in positions:
    if (pos > length/2):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print("Gamma: " + str(int(gamma, 2)))
print("Epsilon: " + str(int(epsilon, 2)))
print("Power: " + str(int(gamma, 2)*int(epsilon, 2)))