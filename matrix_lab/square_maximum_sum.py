rows, columns = [int(x) for x in input().split(",")]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

squares = []
current_max = 0
for row in range(len(matrix) - 1):
    for column in range(len(matrix[row]) - 1):
        current_sum = 0
        one = matrix[row][column]
        two = matrix[row + 1][column]
        three = matrix[row + 1][column + 1]
        four = matrix[row][column + 1]
        current_sum += one + two + three + four
        squares.append((current_sum, row, column))

value, max_row, max_column = max(squares)
print(f"{matrix[max_row][max_column]} {matrix[max_row][max_column + 1]}")
print(f"{matrix[max_row + 1][max_column]} {matrix[max_row + 1][max_column + 1]}")
print(value)
