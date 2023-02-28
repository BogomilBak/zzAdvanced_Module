# from collections import deque
#
# player_one_symbol = "A"
# player_two_symbol = "B"
# turn = deque([
#     [1, player_one_symbol],
#     [2, player_two_symbol]
# ])
# rows, columns = 6, 7
# matrix = [["0" for x in range(columns)] for y in range(rows)]
# directions = [
#     [1, -1],
#     [1, 0],
#     [1, 1],
#     [0, -1],
#     [0, 1],
#     [-1, 0],
#     [-1, 1],
#     [-1, -1],
# ]
#
# while True:
#     [print(*x) for x in matrix]
#     current_player, current_player_symbol = turn[0]
#     player_column = int(input(f"\nPlayer {current_player}, please select a column: ")) - 1
#
#     if not 0 <= player_column < columns:
#         print(f"Please select a valid column in range (1, {columns})")
#
#     row = 0
#     if not matrix[row][player_column] == "0":
#         print("There are no empty spaces on that row!")
#         continue
#
#     while True:
#         if row == rows - 1 or not matrix[row + 1][player_column] == "0":
#             matrix[row][player_column] = current_player
#             break
#
#         row += 1