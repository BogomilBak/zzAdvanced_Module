input_line = input()

opening = []
flag = True

for element in input_line:
    if element in ['{', '[', '(']:
        opening.append(element)

    elif element in ['}', ']', ')']:

        if not opening:
            flag = False
            break

        last_element = opening[-1]
        if element == '}' and last_element == '{':
            opening.pop()

        elif element == ']' and last_element == '[':
            opening.pop()

        elif element == ')' and last_element == '(':
            opening.pop()

        else:
            flag = False
            break

if flag:
    print("YES")
else:
    print("NO")
