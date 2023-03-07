def students_credits(*args):
    result = {}
    for element in args:
        line = element.split("-")
        name, credits, max_points, points = line[0], int(line[1]), int(line[2]), int(line[3])
        credits_taken = (points / max_points) * credits
        if name not in result:
            result[name] = 0
        result[name] = credits_taken
    sorted_result = sorted(result.items(), key=lambda x: -x[1])
    total_credits = sum(result.values())
    final_string = ""
    if total_credits >= 240:
        final_string += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        final_string += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"
    for key, value in sorted_result:
        final_string += f"{key} - {value:.1f}\n"
    return final_string


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)


