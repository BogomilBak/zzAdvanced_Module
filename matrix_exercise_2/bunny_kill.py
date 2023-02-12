# matrix = [
#     [5, 10, 15, 20],
#     [10, 10, 10, 10],
#     [10, 15, 10, 10],
#     [10, 10, 10, 10],
# ]
# coordinates = ['2,2', '0,1']

matrix = [
    [10, 10, 10],
    [10, 10, 10],
    [10, 10, 10]
]

coordinates = ['0,0']

damage = 0
count = 0

for c in coordinates:    # wartq prez koordinatite
    row, column = c.split(",")   # wadq redq i kolonata na bombata
    b_row = int(row)  # prawq gi na integer
    b_column = int(column)
    bomb_value = matrix[b_row][b_column]    # wzimam stoinostta
    if bomb_value == 0:   # ako e 0 - wrashtam cikyla otna4alo shoto e gramnala bomba weche
        continue
    damage += bomb_value   # wdigam stoinostta na damage
    count += 1  # smqtam go za ubito
    for row in range(len(matrix)):   # sprqmo teq stoinostti wartq prez matricata za wsqka bomba otna4alo
        for column in range(len(matrix[row])):
            # gledam tekushtata iteraciq dali e okolo bombata
            # moje bi ima po hityr nachin da se napishe towa, malko botsko sym go naprawil
            if row == b_row or row == b_row - 1 or row == b_row + 1:
                if column == b_column or column == b_column - 1 or column == b_column + 1:
                    # ako ima sawpadenie maham ot stoinostta
                    matrix[row][column] -= bomb_value
                    if matrix[row][column] < 0:
                        # ako stane pod 0 wrashtam na 0 da iz4islq ako e bomba dali e gramnala
                        matrix[row][column] = 0

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        # wartq nanowo prez matricata da ubiq ocelelite
        # ako stoinostta ne e rawna na 0 - na4i garmq drugite
        if not matrix[row][column] == 0:
            damage += matrix[row][column]
            count += 1

print(damage)
print(count)