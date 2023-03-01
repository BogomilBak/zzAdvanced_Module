from math import log

first_num = int(input())
second_num = input()
if not second_num.isdigit():
    print(f"{log(first_num):.2f}")
else:
    print(f"{log(first_num, int(second_num)):.2f}")