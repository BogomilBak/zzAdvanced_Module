from collections import deque

boxes = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

done_presents = {}

toys = False

while boxes and magics:
    box = boxes.pop()
    magic = magics.popleft()

    if box == 0 and magic == 0:
        continue
    elif box == 0:
        magics.appendleft(magic)
        continue
    elif magic == 0:
        boxes.append(box)
        continue

    multiplication = box * magic

    if multiplication in presents:
        current_present = presents[multiplication]
        if current_present not in done_presents:
            done_presents[current_present] = 0
        done_presents[current_present] += 1

    else:
        if multiplication < 0:
            boxes.append(box + magic)
        elif multiplication > 0:
            boxes.append(box + 15)

    if ('Doll' in done_presents and 'Wooden train' in done_presents) or \
            ('Teddy bear' in done_presents and 'Bicycle' in done_presents):
        toys = True

if toys:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {', '.join([str(x) for x in boxes[::-1]])}")
if magics:
    print(f"Magic left: {', '.join([str(x) for x in magics])}")

for key, value in sorted(done_presents.items()):
    print(f"{key}: {value}")