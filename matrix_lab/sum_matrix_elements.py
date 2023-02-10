n, m = [int(x) for x in input().split(",")]

matrix = []

for a in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

total_sum = 0

for element in matrix:
    total_sum += sum(element)
