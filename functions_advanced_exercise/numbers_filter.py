def even_odd_filter(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == "even":
            sorted_value = [x for x in value if x % 2 == 0]
        else:
            sorted_value = [x for x in value if x % 2 != 0]
        result[key] = sorted_value
    sorted_result = sorted(result.items(), key=lambda x: -len(x[1]))
    dict_result = {y:x for y,x in sorted_result}
    return dict_result


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
