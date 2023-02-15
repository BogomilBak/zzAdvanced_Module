def multiply(*args):
    result = 1
    for element in args:
        result *= element
    return result

print(multiply(2, 0, 1000, 5000))