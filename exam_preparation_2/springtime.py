def start_spring(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value not in result:
            result[value] = []
        result[value].append(key)
    sorted_result = sorted(result.items(), key=lambda x: (-len(x[1]), x[0]))
    end_resut = ""
    for key, value in sorted_result:
        end_resut += f"{key}:\n"
        sorted_values = sorted(value)
        for element in sorted_values:
            end_resut += f"-{element}\n"
    return end_resut



example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))





