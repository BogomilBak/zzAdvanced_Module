def my_func(*args):
    negatives = 0
    positives = 0
    for element in args[0]:
        if int(element) > 0:
            positives += int(element)
        else:
            negatives += int(element)
    if abs(negatives) > abs(positives):
        return f"{negatives}\n{positives}\nThe negatives are stronger than the positives"
    return f"{negatives}\n{positives}\nThe positives are stronger than the negatives"

print(my_func(input().split()))