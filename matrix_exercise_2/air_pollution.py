matrix = [
    [5, 7, 72, 14, 4],
    [41, 35, 37, 27, 33],
    [23, 16, 27, 42, 12],
    [2, 20, 28, 39, 14],
    [16, 34, 31, 10, 24]
]
operations = ['breeze 1', 'gale 2', 'smog 25']

for action in operations:
    command, value = action.split()
    value = int(value)

    if command == "breeze":
        for x in range(5):
            matrix[value][x] -= 15
    elif command == "gale":
        for x in range(5):
            matrix[x][value] -= 20
    elif command == "smog":
        for x in range(5):
            for y in range(5):
                matrix[x][y] += value

polluted = []

for x in range(5):
    for y in range(5):
        if matrix[x][y] >= 50:
            z = f"[{x}-{y}]"
            polluted.append(z)

if polluted:
    print(', '.join(polluted))
else:
    print("No polluted areas")