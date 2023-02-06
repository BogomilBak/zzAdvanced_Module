lines = int(input())

odd_set = set()
even_set = set()

for line in range(1, lines + 1):
    name = input()
    name_value = sum([ord(x) for x in name])
    name_value = int(name_value / line)
    if name_value % 2 == 0:
        even_set.add(name_value)
    else:
        odd_set.add(name_value)

if sum(even_set) == sum(odd_set):
    union = even_set.union(odd_set)
    print(f"{''.join([str(x) for x in union])}")

elif sum(even_set) < sum(odd_set):
    diff = odd_set.difference(even_set)
    print(f"{', '.join([str(x) for x in diff])}")

else:
    diff = odd_set.symmetric_difference(even_set)
    print(f"{', '.join([str(x) for x in diff])}")
