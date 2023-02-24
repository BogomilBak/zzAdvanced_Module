file_path = './text.txt'

try:
    file = open(file_path, 'r')
    print("File found")
except FileNotFoundError:
    print("File not found")
