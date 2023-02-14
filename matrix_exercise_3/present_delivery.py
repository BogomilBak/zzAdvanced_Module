presents = int(input())
rows = int(input())

matrix = [input().split() for x in range(rows)]

total_nice_kids = len([x for y in matrix for x in y if x == "V"])
given_presents = 0
santa_row = 0
santa_column = 0

valid_happy = [
    [-1, 0],
    [0, -1],
    [0, 1],
    [1, 0]
]
for row in range(rows):
    for column in range(rows):
        if matrix[row][column] == "S":
            santa_row = row
            santa_column = column

while presents > 0 and total_nice_kids > given_presents:
    command = input()

    if command == "Christmas morning":
        break

    elif command == "up":
        if 0 <=  santa_row - 1 < rows:
            matrix[santa_row][santa_column] = '-'
            santa_row -= 1
    elif command == "down":
        if 0 <= santa_row + 1 < rows:
            matrix[santa_row][santa_column] = '-'
            santa_row += 1
    elif command == "right":
        if 0 <= santa_column + 1 < rows:
            matrix[santa_row][santa_column] = '-'
            santa_column += 1
    elif command == "left":
        if 0 <= santa_column - 1 < rows:
            matrix[santa_row][santa_column] = '-'
            santa_column -= 1

    santa_next_position = matrix[santa_row][santa_column]

    if santa_next_position == "X":
        matrix[santa_row][santa_column] = "S"
    elif santa_next_position == "V":
        matrix[santa_row][santa_column] = "S"
        given_presents += 1
        presents -= 1
    elif santa_next_position == "C":
        matrix[santa_row][santa_column] = "S"
        for move in valid_happy:
            next_row = santa_row + move[0]
            next_column = santa_column + move[1]
            if presents == 0:
                break

            if matrix[next_row][next_column] == "V":
                matrix[next_row][next_column] = '-'
                given_presents += 1
                presents -= 1
            elif matrix[next_row][next_column] == "X":
                matrix[next_row][next_column] = '-'
                presents -= 1
    elif santa_next_position == "-":
        matrix[santa_row][santa_column] = "S"

remaining_kids = len([x for y in matrix for x in y if x == "V"])

if presents == 0 and total_nice_kids > given_presents:
    print("Santa ran out of presents!")
[print(*x) for x in matrix]
if remaining_kids > 0:
    print(f"No presents for {remaining_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {given_presents} happy nice kid/s.")