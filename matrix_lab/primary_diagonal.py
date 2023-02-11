a = int(input())
matrix = []
for _ in range(a):
    matrix.append([int(x) for x in input().split()])

sum_diagonal_pro = sum([matrix[x][x] for x in range(a)])

print(sum_diagonal_pro)