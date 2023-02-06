lines = int(input())

result = set()

for line in range(lines):
    input_line = input().split("-")
    first = [int(x) for x in input_line[0].split(",")]
    second = [int(x) for x in input_line[1].split(",")]
    first_set = set()
    second_set = set()
    for a in range(first[0], first[1] + 1):
        first_set.add(a)
    for b in range(second[0], second[1] + 1):
        second_set.add(b)

    final_set = first_set.intersection(second_set)
    if len(final_set) > len(result):
        result = final_set

result = [x for x in result]
print(f"Longest intersection is {result} with length {len(result)}")
