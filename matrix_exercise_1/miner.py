import sys

rows = int(input())
commands = input().split()
matrix = [input().split() for x in range(rows)]
total_coal = len([x for y in matrix for x in y if x == "c"])
current_coal = 0

row_position = 0
column_position = 0

for row in range(rows):
    for column in range(rows):
        if matrix[row][column] == "s":
            row_position = row
            column_position = column
            break

for command in commands:
    if command == "up":
        if 1 <= row_position:
            matrix[row_position][column_position] = '*'
            next_block = matrix[row_position - 1][column_position]
            if next_block == "e":
                print(f"Game over! ({row_position - 1}, {column_position})")
                sys.exit()
            elif next_block == "c":
                current_coal += 1
                matrix[row_position - 1][column_position] = "s"
            else:
                matrix[row_position - 1][column_position] = "s"
            row_position -= 1

    elif command == "right":
        if column_position < rows - 1:
            matrix[row_position][column_position] = '*'
            next_block = matrix[row_position][column_position + 1]
            if next_block == "e":
                print(f"Game over! ({row_position}, {column_position + 1})")
                sys.exit()
            elif next_block == "c":
                current_coal += 1
                matrix[row_position][column_position + 1] = "s"
            else:
                matrix[row_position][column_position + 1] = "s"
            column_position += 1

    elif command == "left":
        if column_position >= 1:
            matrix[row_position][column_position] = '*'
            next_block = matrix[row_position][column_position - 1]
            if next_block == "e":
                print(f"Game over! ({row_position}, {column_position - 1})")
                sys.exit()
            elif next_block == "c":
                current_coal += 1
                matrix[row_position][column_position -1] = "s"
            else:
                matrix[row_position][column_position - 1] = "s"
            column_position -= 1

    elif command == "down":
        if row_position < rows - 1:
            matrix[row_position][column_position] = '*'
            next_block = matrix[row_position + 1][column_position]
            if next_block == "e":
                print(f"Game over! ({row_position + 1}, {column_position})")
                sys.exit()
            elif next_block == "c":
                current_coal += 1
                matrix[row_position + 1][column_position] = "s"
            else:
                matrix[row_position + 1][column_position] = "s"
            row_position += 1

    if current_coal == total_coal:
        print(f"You collected all coal! ({row_position}, {column_position})")
        sys.exit()

coal_left = len([x for y in matrix for x in y if x == "c"])

row_position = 0
column_position = 0

for row in range(rows):
    for column in range(rows):
        if matrix[row][column] == "s":
            row_position = row
            column_position = column

print(f"{coal_left} pieces of coal left. ({row_position}, {column_position})")