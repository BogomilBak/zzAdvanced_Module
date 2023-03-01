def read_until_command(command, map_func=None):
    result = []
    while True:
        line = input()
        if line == command:
            break
        result.append(line)

    if map_func is None:
        return result
    return [map_func(x) for x in result]

def parse_command(command):
    parts = command.split(" ")
    if parts[0] == "Create":
        return "Create", int(parts[2])
    return "Locate", int(parts[1])

result = []
def create_sequence(number):
    result.clear()
    result.append(0)
    result.append(1)

    for _ in range(2, number):
        result.append(result[-1] + result[-2])
    return [str(x) for x in result]



def locate_number(number):
    if number in result:
        return f"The number - {number} is at index {result.index(number)}"
    return f"The number {number} is not in the sequence"