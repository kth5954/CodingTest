import sys
sys.setrecursionlimit(10**6)
def append_star(n):
    if n == 1:
        return ['*']

    Stars = append_star(n//3)
    L = []

    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S + ' '*(n//3) + S)
    for S in Stars:
        L.append(S*3)

    return L


N = int(sys.stdin.readline().strip())
print('\n'.join(append_star(N)))
