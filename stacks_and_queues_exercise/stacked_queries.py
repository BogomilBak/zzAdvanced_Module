lines = int(input())

result = []
end_result = []
for _ in range(lines):
    input_line = input()

    if input_line.startswith('1'):
        input_line = input_line.split()
        result.append((int(input_line[1])))

    elif input_line == "2":
        if result:
            result.pop()

    elif input_line == "3":
        if result:
            print(max(result))

    elif input_line == "4":
        if result:
            print(min(result))

result = [str(x) for x in result]
while result:
    end_result.append((result.pop()))

print(', '.join(end_result))
