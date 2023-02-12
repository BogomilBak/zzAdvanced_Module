# matrix = [
#     [5, 10, 15, 20],
#     [10, 10, 10, 10],
#     [10, 15, 10, 10],
#     [10, 10, 10, 10],
# ]
# coordinates = ['2,2', '0,1']

matrix = [
    [10, 10, 10],
    [10, 10, 10],
    [10, 10, 10]
]

coordinates = ['0,0']

damage = 0
count = 0

for c in coordinates:
    row, column = c.split(",")
    b_row = int(row)
    b_column = int(column)
    bomb_value = matrix[b_row][b_column]
    if bomb_value == 0:
        continue
    damage += bomb_value
    count += 1
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if row == b_row or row == b_row - 1 or row == b_row + 1:
                if column == b_column or column == b_column - 1 or column == b_column + 1:
                    matrix[row][column] -= bomb_value
                    if matrix[row][column] < 0:
                        matrix[row][column] = 0

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if not matrix[row][column] == 0:
            damage += matrix[row][column]
            count += 1

print(damage)
print(count)