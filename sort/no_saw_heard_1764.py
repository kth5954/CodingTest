import sys

def intersection(a, b):
    a = set(a)
    b = set(b)
    return list(a - (a - b))


n, m = map(int, sys.stdin.readline().split())
no_saw = []
no_heard = []
for _ in range(n):
    no_saw.append(sys.stdin.readline().rstrip())
for _ in range(m):
    no_heard.append(sys.stdin.readline().rstrip())

res = sorted(intersection(no_saw, no_heard))
print(len(res))
for name in res:
    print(name)






