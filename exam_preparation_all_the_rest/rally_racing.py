size = int(input())
name = input()
matrix = []
tunnel = []
pos_row = 0
pos_col = 0
for row in range(size):
    line = input().split()
    matrix.append(line)
    if "T" in line:
        tunnel.append([row, line.index("T")])
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
distance = 0
while True:
    command = input()
    if command == "End":
        print(f"Racing car {name} DNF.")
        break
    pos_row += directions[command][0]
    pos_col += directions[command][1]
    location = matrix[pos_row][pos_col]

    if location == "F":
        distance += 10
        print(f"Racing car {name} finished the stage!")
        break
    elif location == ".":
        distance += 10
    elif location == "T":
        for tun in tunnel:
            if not (tun[0] == pos_row and tun[1] == pos_col):
                matrix[pos_row][pos_col] = '.'
                pos_row = tun[0]
                pos_col = tun[1]
                matrix[pos_row][pos_col] = '.'
                distance += 30

matrix[pos_row][pos_col] = "C"
print(f"Distance covered {distance} km.")
[print(''.join(x)) for x in matrix]