rows = int(input())
matrix = [input().split() for x in range(rows)]

location = []
for row in range(rows):
    for column in range(rows):
        if matrix[row][column] == "B":
            location = [row, column]
            matrix[row][column] = "0"

direction = {
    0: (-1, 0, 'up'),
    1: (1, 0, 'down'),
    2: (0, -1, 'left'),
    3: (0, 1, 'right'),
}
best_so_far = 0
best_coordinates = []
best_direction = ''
for interration in range(4):
    current_max = 0
    current_max_location = []
    r = location[0]
    c = location[1]
    while True:
        r += direction[interration][0]
        c += direction[interration][1]

        if not (0 <= r < rows and 0 <= c < rows):
            break
        elif matrix[r][c] == "X":
            break
        else:
            current_max += int(matrix[r][c])
            current_max_location.append([r, c])

    if current_max >= best_so_far:
        best_so_far = current_max
        best_coordinates = current_max_location
        best_direction = direction[interration][2]

print(best_direction)
[print(x) for x in best_coordinates]
print(best_so_far)