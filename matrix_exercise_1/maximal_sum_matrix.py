rows, columns = [int(x) for x in input().split()]
matrix = [[int(a) for a in input().split()] for a in range(rows)]

biggest_sum = -9999999
biggest_matrix = []

for r in range(rows - 2):
    for c in range(columns - 2):
        sum_element = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + \
                matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2] + \
                      matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
        if sum_element > biggest_sum:
            biggest_sum = sum_element
            biggest_matrix = [[matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]], \
                [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]], \
                      [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]]

print(f"Sum = {biggest_sum}")
for element in biggest_matrix:
    print(' '.join([str(x) for x in element]))