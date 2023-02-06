line = input()

result = {}

for a in line:
    if a not in result:
        result[a] = 0
    result[a] += 1

sorted_result = sorted(result.items())
for key, value in sorted_result:
    print(f"{key}: {value} time/s")
