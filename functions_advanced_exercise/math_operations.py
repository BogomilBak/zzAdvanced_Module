from collections import deque


def math_operations(*args, **kwargs):
    queue = deque(args)
    counter = 1
    while queue:
        number = queue.popleft()
        if number == 0:
            counter += 1
            continue

        if counter == 1:
            kwargs['a'] += number
        elif counter == 2:
            kwargs['s'] -= number
        elif counter == 3:
            kwargs['d'] /= number
        elif counter == 4:
            kwargs['m'] *= number

        counter += 1

        if counter == 5:
            counter = 1

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    result_string = ''

    for key, value in result:
        result_string += f"{key}: {value:.1f}" + "\n"

    return result_string



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))