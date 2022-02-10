def combinations(arr, m):
    n = len(arr)
    result = []
    if m == 0:
        return [[]]
    for i in range(n):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for c in combinations(rest_arr, m - 1):
            result.append([elem] + c)
    return result


def permutations(arr, m):
    n = len(arr)
    result = []
    if m == 0:
        return [[]]
    for i in range(n):
        elem = arr[i]
        rest_arr = arr[:i] + arr[i + 1:]
        for p in permutations(rest_arr, m - 1):
            result.append([elem] + p)
    return result



