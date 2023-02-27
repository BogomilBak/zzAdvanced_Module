import os
from os import remove
while True:
    command = input()
    if command == "End":
        break

    command = command.split('-')
    file_name = command[1]
    if command[0] == 'Create':
        file = open(f"./{command[1]}", "w")
        file.close()
    elif command[0] == "Add":
        with open(f"./{command[1]}", "a") as file:
            file.write(f"{command[2]}\n")
        file.close()
    elif command[0] == "Replace":
        try:
            with open(f"./{file_name}", "r") as file:
                text = file.readlines()
            file = open(f"./{file_name}", "w")

            for line in range(len(text)):
                text[line] = text[line].replace(command[2], command[3])
            file.write(''.join(text))
            file.close()
        except FileNotFoundError:
            print("An error occurred")
    elif command[0] == "Delete":
        try:
            os.remove(f"./{file_name}")
        except FileNotFoundError:
            print("An error occurred")