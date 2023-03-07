def forecast(*args):
    result = {}
    for key, value in args:
        if key not in result:
            result[key] = ""
        result[key] = value
    sorted_result = sorted(result.items(), key=lambda x: (x[1] != "Sunny", x[1] != "Cloudy", x[0]))
    final_string = ""
    for key, value in sorted_result:
        final_string += f"{key} - {value}\n"
    return final_string
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


