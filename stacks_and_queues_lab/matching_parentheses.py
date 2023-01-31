input_line = input()

starting = []

for index, value in enumerate(input_line):
    if value == "(":
        starting.append(index)

    elif value == ")":
        print(f"{input_line[starting.pop():index + 1]}")


