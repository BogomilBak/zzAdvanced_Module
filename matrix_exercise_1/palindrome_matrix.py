rows, columns = [int(x) for x in input().split()]
matrix = []

for r in range(rows):
    row = []
    for c in range(columns):
        first = chr(97 + r)
        second = chr(97 + r + c)
        word = f"{first}{second}{first}"
        row.append(word)
    print(' '.join(row))

