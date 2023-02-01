input_line = input().split()
result = []
for _ in range(len(input_line)):
    result.append(input_line.pop())

print(' '.join(result))
