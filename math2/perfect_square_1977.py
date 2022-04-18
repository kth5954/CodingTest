import sys
import math

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

arr = [0] * 10001
for i in range(1, 101):
    arr[i * i] = True

sum_ = 0
min_ = 0
for num in range(m, n + 1):
    if arr[num]:
        sum_ += num
        if not min_:
            min_ = num

if min_:
    print(sum_)
    print(min_)
else:
    print(-1)


