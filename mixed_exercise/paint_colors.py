from collections import deque

lines = deque(input().split())
result = []
main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']

while lines:
    first = lines.popleft()
    second = lines.pop() if lines else ''
    combined = first + second
    combined_reversed = second + first

    if combined in main_colors or combined in secondary_colors:
        result.append(combined)
    elif combined_reversed in main_colors or combined_reversed in secondary_colors:
        result.append(combined_reversed)
    else:
        first = first[:-1]
        second = second[:-1]
        middle = len(lines) // 2
        if second:
            lines.insert(middle, second)
        if first:
            lines.insert(middle, first)

needed_colors = {
    'purple': ['red', 'blue'],
    'orange': ['red', 'yellow'],
    'green': ['blue', 'yellow']
}

for color in result:
    if color in secondary_colors:
        current_color = needed_colors[color]
        is_valid = all([x in result for x in current_color])
        if not is_valid:
            result.remove(color)

print(result)