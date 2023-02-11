rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append(input())

symbol = input()
is_found = False
row_a = 0
column_a = 0
for row in range(len(matrix)):
    if is_found:
        break
    for column in range(len(matrix[row])):
        if matrix[row][column] == symbol:
            row_a = row
            column_a = column
            is_found = True
            break

if is_found:
    print(f"({row_a}, {column_a})")
else:
    print(f"{symbol} does not occur in the matrix")
