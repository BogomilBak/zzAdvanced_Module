file_path = './numbers.txt'

file = open(file_path, 'r')
result = 0

for element in file:
    result += int(element)

print(result)