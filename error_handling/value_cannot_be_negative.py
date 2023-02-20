class ValueCannotBeNegative(Exception):
    """I write my documentation here. This is a docstring"""
    pass

for i in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative
