from collections import deque

seats = deque(input().split(", "))
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])
taken_seats = []
rotations = 0

while len(taken_seats) < 3 and rotations < 10:
    first = first_sequence.popleft()
    second = second_sequence.pop()
    rotations += 1
    letter = chr(first + second)
    first_seat, second_seat = (str(first) + letter), (str(second) + letter)

    if first_seat in seats:
        taken_seats.append(first_seat)
        seats.remove(first_seat)
    elif second_seat in seats:
        taken_seats.append(second_seat)
        seats.remove(second_seat)
    elif (first_seat, second_seat) not in taken_seats:
        first_sequence.append(first)
        second_sequence.appendleft(second)


print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")