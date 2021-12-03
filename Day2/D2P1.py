from input import input

input = input.splitlines()

depth = 0
horizontalPos = 0

for instruction in input:
    direction, distance = instruction.split()
    if (direction == "forward"):
        horizontalPos += int(distance)
    elif (direction == "up"):
        depth -= int(distance)
    elif (direction == "down"):
        depth += int(distance)

print(f'Depth: {depth}')
print(f'Horizontal Position: {horizontalPos}')
print(f'Part 1 answer: {depth * horizontalPos}')