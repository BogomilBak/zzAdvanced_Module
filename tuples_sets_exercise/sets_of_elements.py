line_1 = [int(x) for x in input().split()]

result_1 = {input() for _ in range(line_1[0])}
result_2 = {input() for _ in range(line_1[1])}

result = result_1.intersection(result_2)

for _ in result:
    print(_)
