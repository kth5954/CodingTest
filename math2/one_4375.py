while True:
    try:
        n = int(input())
    except EOFError:
        break
    one = '1'
    while True:
        if not int(one) % n:
            print(len(one))
            break
        else:
            one += '1'