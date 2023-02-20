def grocery_store(**kwargs):
    end_result = ''
    result = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for key, value in result:
        end_result += key + ': ' + str(value) + '\n'
    return end_result


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
