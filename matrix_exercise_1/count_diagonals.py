rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

columns = len(matrix[0])
primary = []
secondary = []
for row in range(rows):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][rows - row - 1])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")