# 지나온 것은 내림차순이 아니면 False

import sys

n = int(sys.stdin.readline())

stack = []
res = []
temp = True
count = 1

for i in range(n):
    num = int(sys.stdin.readline())
    while count <= num:
        res.append("+")
        stack.append(count)
        count += 1
    if stack[-1] == num:
        res.append("-")
        stack.pop()
    else:
        temp = False
if not temp:
    print("NO")
else:
    for i in res:
        print(i)
