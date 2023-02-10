rows = int(input())

matrix = []

for _ in range(rows):
    matrix.extend([x for x in input().split()])

print(matrix)