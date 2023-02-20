def age_assignment(*args, **kwargs):
    result = {}
    end_result = ''
    for x in args:
        result[x] = 0
    for key, value in kwargs.items():
        for x, y in result.items():
            if x.startswith(key):
                result[x] = value
    sorted_result = sorted(result.items(), key=lambda x: x[0])
    for key, value in sorted_result:
       end_result += f"{key} is {value} years old." + '\n'
    return end_result



print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))