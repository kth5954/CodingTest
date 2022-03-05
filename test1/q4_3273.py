import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())


left, right = 0, n - 1
cnt = 0

while left < right:
    tmp = a[left] + a[right]
    if tmp == x:
        cnt += 1
    if tmp > x:
        right -= 1
    else:
        left += 1
print(cnt)
