rows = int(input())
matrix = [[int(x) for x in input().split()] for x in range(rows)]
coordinates = input().split()

for bomb in coordinates:
    row, column = bomb.split(",")
    b_row = int(row)
    b_column = int(column)
    value = matrix[b_row][b_column]
    if value <= 0:
        continue
    matrix[b_row][b_column] = 0

    for row in range(rows):
        for column in range(len(matrix[0])):
            if row == b_row - 1 or row == b_row or row == b_row + 1:
                if column == b_column - 1 or column == b_column or column == b_column + 1:

                    if row == b_row and column == b_column:
                        continue
                    if matrix[row][column] > 0:
                        matrix[row][column] -= value

active = len([x for y in matrix for x in y if x > 0])
sum_active = sum([x for y in matrix for x in y if x > 0])
print(f"Alive cells: {active}")
print(f"Sum: {sum_active}")
for element in matrix:
    print(' '.join([str(x) for x in element]))