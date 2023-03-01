from modules_lab.triangle.read_until_modules import read_until_command, parse_command, locate_number, create_sequence

input_line = read_until_command("Stop", map_func=parse_command)
for key, value in input_line:
    if key == "Create":
        print(f"{' '.join(create_sequence(value))}")
    elif key == "Locate":
        print(locate_number(value))
