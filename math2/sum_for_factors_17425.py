import sys

MAX = 1000000
d = [1] * (MAX + 1)
for i in range(2, MAX + 1):
    for j in range(i, MAX + 1, i):
        d[j] += i

    d[i] += d[i - 1]

T = int(sys.stdin.readline())
ans = []
for _ in range(T):
    a = int(sys.stdin.readline())
    ans.append(d[a])
print('\n'.join(map(str, ans)) + '\n')