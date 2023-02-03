lines = int(input())

result = {}

for _ in range(lines):
    name, grade = input().split()
    grade = float(grade)
    if name not in result:
        result[name] = []
    result[name].append(grade)

for key, value in result.items():
    scores = ' '.join([f'{x:.2f}' for x in value])
    average = sum(value) / len(value)
    print(f"{key} -> {scores} (avg: {average:.2f})")
