def print_triangle(size):
    for row in range(1, size + 1):
        for column in range(1, row + 1):
            print(column, end=" ")
        print()
    for row in range(size - 1, -1, -1):
        for column in range(1, row + 1):
            print(column, end=" ")
        print()
