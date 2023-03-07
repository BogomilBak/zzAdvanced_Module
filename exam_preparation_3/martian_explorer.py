def check_position(pos):
    if pos < 0:
        return ROWS - 1
    elif pos >= ROWS:
        return 0
    return pos


ROWS = 6
matrix = [input().split() for x in range(ROWS)]
commands = input().split(", ")
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
pos_row = 0
pos_column = 0
for row in range(ROWS):
    for column in range(ROWS):
        if matrix[row][column] == "E":
            pos_row = row
            pos_column = column
            break

deposits = {
    "W": False,
    "M": False,
    "C": False,
}
print_deposits = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete",
}
for movement in commands:
    pos_row += directions[movement][0]
    pos_column += directions[movement][1]

    pos_row = check_position(pos_row)
    pos_column = check_position(pos_column)

    position = matrix[pos_row][pos_column]

    if position == "R":
        print(f"Rover got broken at ({pos_row}, {pos_column})")
    elif position in deposits:
        print(f"{print_deposits[position]} deposit found at ({pos_row}, {pos_column})")
        deposits[position] = True

if all(deposits.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
