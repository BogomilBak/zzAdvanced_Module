clothes = [int(x) for x in input().split()]
rack = int(input())
current_rack = rack
result = 0

while clothes:
    element = clothes[-1]

    if element <= current_rack:
        clothes.pop()
        current_rack -= element
    else:
        current_rack = rack
        clothes.pop()
        result += 1
        current_rack -= element

print(result)
