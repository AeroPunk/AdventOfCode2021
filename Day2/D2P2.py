from input import input

input = input.splitlines()

depth = 0
horizontalPos = 0
aim = 0

for instruction in input:
    direction, distance = instruction.split()
    if (direction == "forward"):
        horizontalPos += int(distance)
        depth += (aim * int(distance))
    elif (direction == "up"):
        aim -= int(distance)
    elif (direction == "down"):
        aim += int(distance)

print(f'Depth: {depth}')
print(f'Horizontal Position: {horizontalPos}')
print(f'Part 2 answer: {depth * horizontalPos}')