import sys
from collections import deque

player_one_symbol = "1"
player_two_symbol = "2"
rows, cols = 6, 7
turn = deque([
    [1, player_one_symbol],
    [2, player_two_symbol]
])
directions = [
    [0, -1],
    [0, 1],
    [1, 0],
    [1, -1],
    [1, 1],
    [-1, 0],
    [-1, -1],
    [-1, 1],
]
board = [[["0"] * cols for row in range(rows)]]

while True:
    [print(f"[ {', '.join(row)} ]") for row in board]

    player_number, player_symbol = turn[0]
    player_col = int(input(f"\nPlayer {player_number}, please choose a column: ")) - 1

    if not 0 <= player_col < cols:
        print(f"Select a valid number in the range ({1} {cols}")
        continue

    row = 0

    if not board[row][player_col] == "0":
        print("No empty spaces on that row!")
        continue

    while True:
        if row == rows - 1 or not board[row + 1][player_col] == "0":
            board[row][player_col] = player_symbol
            break

        row += 1

    for coordinates in directions:
        r, c = row, player_col

        for _ in range(3):
            r, c = r + coordinates[0], c + coordinates[1]

            if not (0 <= r < rows and 0 <= c < cols):
                break

            if not board[r][c] == player_symbol:
                break
        else:
            [print(f"[ {', '.join(row)} ]") for row in board]
            print("!!!!!")
            print("!!!!!")
            print(f"The winner is player: {player_number}")
            print("!!!!!")
            print("!!!!!")
            sys.exit()

    turn.append(turn.popleft())
