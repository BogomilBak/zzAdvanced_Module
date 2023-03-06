from collections import deque

turns = deque(input().split(", "))
matrix = [input().split() for x in range(6)]
input_line = input()

while input_line:
    row, column = int(input_line[1]), int(input_line[4])
    player = turns.popleft()
    if "X" in player:
        turns.append(player[:-1])
        input_line = input()
        continue
    elif matrix[row][column] == "E":
        print(f"{player} found the Exit and wins the game!" )
        break
    elif matrix[row][column] == "T":
        print(f"{player} is out of the game! The winner is {turns.pop()}." )
        break
    elif matrix[row][column] == "W":
        print(f"{player} hits a wall and needs to rest.")
        turns.append(player + "X")
        input_line = input()
        continue
    turns.append(player)
    input_line = input()