def even_odd(*args):
    my_list, operator = args[:-1], args[-1]
    if operator == "even":
        return [x for x in my_list if x % 2 == 0]
    return [x for x in my_list if not x % 2 == 0]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))