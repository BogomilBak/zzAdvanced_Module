from collections import deque

food = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])
finished_peaks = []
peaks = [
    [80, "Vihren"],
    [90, "Kutelo"],
    [100, "Banski Suhodol"],
    [60, "Polezhan"],
    [70, "Kamenitza"],
]

for day in range(7):
    if not peaks:
        break
    current_food = food.pop()
    current_stamina = stamina.popleft()
    power = current_stamina + current_food
    if power >= peaks[0][0]:
        finished_peaks.append(peaks[0][1])
        peaks.pop(0)

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if finished_peaks:
    print("Conquered peaks:")
    [print(x) for x in finished_peaks]
