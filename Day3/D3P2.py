from input import input

input = input.splitlines()

def getMostUsedValue(values, pos, type):
    length = len(values)
    hits = 0
    for line in values:
        if (line[pos] == "1"):
            hits += 1

    if (( type == 'Oxygen' ) and ( hits >= length/2)) or (( type == 'CO2' ) and ( hits < length/2)):
        return '1'
    else:
        return '0' 

def filterList(values, pos, type):
    keepValue = getMostUsedValue(values, pos, type)
    newValues = []
    for line in values:
        if (line[pos] == keepValue):
            newValues.append(line)
    
    print(f'Values left: {len(newValues)}')
    pos += 1

    if (len(newValues) > 1):
        return filterList(newValues, pos, type)
    else:
        print(f'{type}: {int(newValues[0], 2)}')
        return int(newValues[0], 2)

print(f'Values left: {len(input)}')
o2 = filterList(input, 0, 'Oxygen')
print()
print(f'Values left: {len(input)}')
co2 = filterList(input, 0, 'CO2')
print()
print(f'Life support rating: {o2 * co2}')