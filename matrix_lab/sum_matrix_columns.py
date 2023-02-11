a, b = [int(x) for x in input().split(", ")]

matrix = []

for c in range(a):
    matrix.append([int(x) for x in input().split()])

sum_elements = [0] * b

for c in range(len(matrix)):
    for d in range(len(matrix[c])):
        value = matrix[c][d]
        sum_elements[d] += value

[print(x) for x in sum_elements]