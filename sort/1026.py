import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
s = []
a.sort()
b.sort(reverse=True)

for i in range(n):
    s.append(a[i]*b[i])
print(sum(s))
