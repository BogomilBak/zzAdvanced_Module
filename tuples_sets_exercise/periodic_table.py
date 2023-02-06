lines = int(input())

result = set()

for x in range(lines):
    elements = input().split()
    for b in elements:
        result.add(b)

for a in result:
    print(a)
