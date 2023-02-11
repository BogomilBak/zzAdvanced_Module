rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for a in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    if not len(command) == 5 or not command[0] == "swap":
        print("Invalid input!")
        continue
    r1 = int(command[1])
    r2 = int(command[3])
    c1 = int(command[2])
    c2 = int(command[4])
    if r1 < 0 or r1 > rows or c1 < 0 or c1 > columns or r2 < 0 or r2 > rows or c2 < 0 or c2 > columns:
        print("Invalid input!")
        continue
    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
    for element in matrix:
        print(' '.join([str(x) for x in element]))