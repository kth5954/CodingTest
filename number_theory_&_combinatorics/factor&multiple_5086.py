a, b = -1, -1
while True:
    if a == 0 and b == 0:
        break
    a, b = map(int, input().split())
    try:
        if a % b == 0:
            print("multiple")
        elif b % a == 0:
            print("factor")
        else:
            print("neither")
    except ZeroDivisionError:
        break