from functools import reduce


def operate(operator, *kwargs):
    if operator == "+":
        return reduce(lambda x, y: x + y, kwargs)
    elif operator == "-":
        return reduce(lambda x, y: x - y, kwargs)
    elif operator == "*":
        return reduce(lambda x, y: x * y, kwargs)
    else:
        return reduce(lambda x, y: x / y, kwargs)


print(operate("*", 3, 4))