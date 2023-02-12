# matrix = [
#     [5, 7, 72, 14, 4],
#     [41, 35, 37, 27, 33],
#     [23, 16, 27, 42, 12],
#     [2, 20, 28, 39, 14],
#     [16, 34, 31, 10, 24]
# ]
# operations = ['breeze 1', 'gale 2', 'smog 25']

# matrix = [
#     [5, 7, 3, 28, 32],
#     [41, 12, 49, 30, 33],
#     [3, 16, 20, 42, 12],
#     [2, 20, 10, 39, 14],
#     [7, 34, 4, 27, 24],
# ]
# operations = ['smog 11', 'gale 3', 'breeze 1', 'smog 2']

matrix = [
    [5, 7, 2, 14, 4],
    [21, 14, 2, 5, 3],
    [3, 16, 7, 42, 12],
    [2, 20, 8, 39, 14],
    [7, 34, 1, 10, 24]
]
operations = ['breeze 1', 'gale 2', 'smog 35']

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