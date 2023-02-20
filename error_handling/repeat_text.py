try:
    message = input()
    times = int(input())
    print(message * times)
except:
    print("Variable times must be an integer")