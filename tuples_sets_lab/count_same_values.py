input_line = [float(x) for x in input().split()]
result = {}
for number in input_line:
    if number not in result:
        result[number] = 0
    result[number] += 1

for key, value in result.items():
    print(f"{key} - {value} times")