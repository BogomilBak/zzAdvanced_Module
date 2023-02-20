def func_executor(*kwargs):
    result = ''
    for element in kwargs:
        name = element[0].__name__
        result += f"{name} - {element[0](*element[1])}"
        result += '\n'
    return result



def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))