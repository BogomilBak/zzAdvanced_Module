rows, columns = [int(x) for x in input().split()]
matrix = []
pos_row = 0
pos_column = 0
for row in range(rows):
    line = input().split()
    matrix.append(line)
    if "B" in line:
        pos_row = row
        pos_column = line.index("B")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
total_players = len([x for y in matrix for x in y if x == "P"])
moves = 0
touches = 0

while touches < total_players:
    input_line = input()
    if input_line == "Finish":
        break

    pos_row += directions[input_line][0]
    pos_column += directions[input_line][1]

    if not 0 <= pos_row < rows or not 0 <= pos_column < columns:
        pos_row -= directions[input_line][0]
        pos_column -= directions[input_line][1]
    elif matrix[pos_row][pos_column] == "O":
        pos_row -= directions[input_line][0]
        pos_column -= directions[input_line][1]
    elif matrix[pos_row][pos_column] == "P":
        matrix[pos_row][pos_column] = "-"
        touches += 1
        moves += 1
    else:
        moves += 1

print("Game over!")
print(f"Touched opponents: {touches} Moves made: {moves}")
