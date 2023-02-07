first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

lines = int(input())

for _ in range(lines):
    input_line = input().split()

    if input_line[0] == "Add" and input_line[1] == "First":
        [first.add(int(x)) for x in input_line[2:]]

    elif input_line[0] == "Add" and input_line[1] == "Second":
        [second.add(int(x)) for x in input_line[2:]]

    elif input_line[0] == "Remove" and input_line[1] == "First":
        current_set = set([int(x) for x in input_line[2:]])
        first = first.difference(current_set)

    elif input_line[0] == "Remove" and input_line[1] == "Second":
        current_set = set([int(x) for x in input_line[2:]])
        second = second.difference(current_set)

    else:
        print(first.issubset(second) or second.issubset(first))

first = sorted(first)
second = sorted(second)
print(f"{', '.join([str(x) for x in first])}")
print(f"{', '.join([str(x) for x in second])}")