from collections import deque

textiles = deque([int(x) for x in input().split()])
medicament = [int(x) for x in input().split()]

items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

while textiles and medicament:
    current_textile = textiles.popleft()
    current_med = medicament.pop()
    total_sum = current_textile + current_med

    if total_sum == 30:
        items["Patch"] += 1
    elif total_sum == 40:
        items["Bandage"] += 1
    elif total_sum >= 100:
        items["MedKit"] += 1
        if medicament:
            medicament[-1] += total_sum - 100
    else:
        medicament.append(current_med + 10)

if not medicament and not textiles:
    print("Textiles and medicaments are both empty.")
elif not medicament:
    print("Medicaments are empty.")
else:
    print("Textiles are empty.")

sorted_result = sorted(items.items(), key=lambda x: (-x[1], x[0]))

for key, value in sorted_result:
    if value:
        print(f"{key} - {value}")

if medicament:
    print(f"Medicaments left: {', '.join([str(x) for x in medicament[::-1]])}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
