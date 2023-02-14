rows = int(input())
matrix = [list(input()) for x in range(rows)]
possible_moves = [
    [-2, -1],
    [-2, 1],
    [-1, -2],
    [-1, 2],
    [1, 2],
    [1, -2],
    [2, 1],
    [2, -1],
]

removed_knights = 0

while True:
    max_damage_knight = 0
    max_damage_knight_position = []

    for row in range(rows):
        for column in range(rows):
            if matrix[row][column] == "K":
                max_attack = 0

                for move in possible_moves:
                    attack_row = move[0] + row
                    attack_column = move[1] + column

                    if 0 <= attack_row < rows and 0 <= attack_column < rows:
                        if matrix[attack_row][attack_column] == "K":
                            max_attack += 1

                if max_attack > max_damage_knight:
                    max_damage_knight = max_attack
                    max_damage_knight_position = [row, column]

    if max_damage_knight == 0:
        break

    matrix[max_damage_knight_position[0]][max_damage_knight_position[1]] = 0
    removed_knights += 1

print(removed_knights)


