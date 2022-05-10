def solution(n):
    arr = []
    k = 0
    while len(arr) < n:
        switch = 0
        str_k = str(k)
        for i in ['3','5','6','7','8','9','0']:
            if i in str_k:
                switch = 1
        if not switch:
            arr.append(k)
        k += 1
    return arr.pop()

print(solution(10))

