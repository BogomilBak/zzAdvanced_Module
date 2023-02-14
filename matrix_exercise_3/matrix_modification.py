rows = int(input())
matrix = [[int(x) for x in input().split()] for x in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    command, row, column, value = command.split()
    row = int(row)
    column = int(column)

    if not 0 <= row < rows - 1 or not 0 <= column < len(matrix[0]) - 1:
        print("Invalid coordinates")
    elif command == "Add":
        matrix[row][column] += int(value)
    elif command == "Subtract":
        matrix[row][column] -= int(value)

for element in matrix:
    print(' '.join([str(x) for x in element]))